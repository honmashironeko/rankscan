from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd
import tldextract
import requests
import argparse
import json
import re

def extract_domain(domain):
    return tldextract.extract(domain).registered_domain

def detect_domain(text):
    if not isinstance(text, str):
        raise ValueError("输入必须是字符串类型")
    domain_pattern = r'(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'
    results = re.findall(domain_pattern, text)
    return results

def aizhan_rank(domain):
    brrank = mbrrank = prrank = ' '
    url = f"https://www.aizhan.com/cha/{domain}/"
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            patterns = {
                'brrank': r'<img src="//statics\.aizhan\.com/images/br/(\d+)\.png"',
                'mbrrank': r'<img src="//statics\.aizhan\.com/images/mbr/(\d+)\.png"',
                'prrank': r'<img src="//statics\.aizhan\.com/images/pr/(\d+)\.png"'
            }
            ranks = {'brrank': ' ', 'mbrrank': ' ', 'prrank': ' '}
            for rank_type, pattern in patterns.items():
                match = re.search(pattern, response.text)
                if match and match.group(1).isdigit() and 1 <= int(match.group(1)) <= 10:
                    ranks[rank_type] = match.group(1)
            brrank, mbrrank, prrank = ranks['brrank'], ranks['mbrrank'], ranks['prrank']
            if brrank != ' ' or mbrrank != ' ' or prrank != ' ':
                print(f"{domain.ljust(35)}百度权重：{brrank.ljust(5)}移动权重：{mbrrank.ljust(5)}谷歌权重：{prrank}")
            else:
                brrank = mbrrank = prrank = 0
        else:
            brrank = mbrrank = prrank = 0
    except:
        print("爱站请求失败，请检查网络")
        brrank = mbrrank = prrank = 0

    return brrank, mbrrank, prrank

def resources_zoomeye(zoomeye_key):
    url = 'https://api.zoomeye.org/resources-info'
    headers = {"API-KEY" : zoomeye_key}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            remain_quota = data.get('quota_info', {}).get('remain_total_quota', 0)
            return remain_quota if remain_quota >= 30 else 0
    except Exception as e:
        print(f"ZoomEye请求失败: {e}")
    return 0

def get_subdomain(domain,zoomeye_key,pages=None):
    global control
    headers = {"API-KEY" : zoomeye_key}
    if pages is None:
        pages = 1
    names = []
    for page in range(1, int(pages) + 1):
        url = f"https://api.zoomeye.org/domain/search?q={domain}&type=1&page={page}"
        response = requests.get(url,headers=headers, timeout=10)
        if response.status_code == 200:
            data = json.loads(response.text)
            if data.get('status') == 401:
                quota = resources_zoomeye(zoomeye_key)
                control = False
                print(f"Zoomeye 余额不足，请更换API-KEY，剩余配额：{quota}")
                break
            else:
                names.extend([item['name'] for item in data['list']])
                if len(data['list']) < 30:
                    break
    return names

def fetch_subdomain_ranks(subdomain):
    def get_valid_rank(rank):
        try:
            rank_int = int(rank)
            if 1 <= rank_int <= 10:
                return rank_int
        except ValueError:
            pass
        return " "

    brrank, mbrrank, prrank = aizhan_rank(subdomain)
    
    brrank_valid = get_valid_rank(brrank)
    mbrrank_valid = get_valid_rank(mbrrank)
    prrank_valid = get_valid_rank(prrank)
    
    if brrank_valid == " " and mbrrank_valid == " " and prrank_valid == " ":
        return {'域名': subdomain, '百度权重': brrank_valid, '移动权重': mbrrank_valid, '谷歌权重': prrank_valid}, True
 
    return {'域名': subdomain, '百度权重': brrank_valid, '移动权重': mbrrank_valid, '谷歌权重': prrank_valid}, False




control = True
def process_domains(listdomain, zoomeye_key, pages, thread):
    domain_cache = {}
    df = pd.DataFrame(columns=['域名', '百度权重', '移动权重', '谷歌权重'])
    df_not_ranked = pd.DataFrame(columns=['域名', '百度权重', '移动权重', '谷歌权重'])
    query_failed = []

    with ThreadPoolExecutor(max_workers=int(thread)) as executor:
        future_to_subdomain = {}
        for domain in listdomain:
            domain = detect_domain(domain)[0]
            if zoomeye_key:
                domaindj = extract_domain(domain)
                if domaindj not in domain_cache:
                    subdomain_list = []
                    if domaindj != '':
                        if control == True:
                            try:
                                subdomain_list = get_subdomain(domaindj, zoomeye_key, pages)
                            except:
                                query_failed.append(domain)
                                continue
                        else:
                            query_failed.append(domain)
                    subdomain_list.append(domain)
                    domain_cache[domaindj] = subdomain_list
                else:
                    subdomain_list = domain_cache[domaindj]
            else:
                subdomain_list = [domain]
            for subdomain in subdomain_list:
                future = executor.submit(fetch_subdomain_ranks, subdomain)
                future_to_subdomain[future] = subdomain
                
        for future in as_completed(future_to_subdomain):
            result, is_not_ranked = future.result()
            if is_not_ranked:
                df_not_ranked = pd.concat([df_not_ranked, pd.DataFrame(result, index=[0])], ignore_index=True)
            else:
                df = pd.concat([df, pd.DataFrame(result, index=[0])], ignore_index=True)
                
    return df, df_not_ranked, query_failed

def main(file_path, zoomeye_key, pages, thread):
    try:
        with open(file_path, 'r') as f:
            listdomain = f.read().splitlines()
    except FileNotFoundError as e:
        print(f"文件路径错误：{e}")
        return
    
    df, df_not_ranked, query_failed = process_domains(listdomain, zoomeye_key, pages, thread)
    df.to_excel('Rank_Results.xlsx', index=False)
    df_not_ranked.to_excel('Not_Rank.xlsx', index=False)
    if query_failed:
        with open('query_failed.txt', 'w') as f:
            for domain in query_failed:
                f.write(f"{domain}\n")

    print("查询完成，结果保存在Rank_Results.xlsx、Not_Rank.xlsx和query_failed.txt")

def update_module():
    try:
        icpscan_time = "2024-05-28"
        url = "https://y.shironekosan.cn/1.html"
        response = requests.get(url)
        pattern = r'<div\s+class="nc-light-gallery"\s+id="image_container">(.*?)</div>'
        matches = re.search(pattern, response.text, re.DOTALL)
        content_array = []
        
        if matches:
            inner_content = matches.group(1)
            p_matches = re.findall(r'<p>(.*?)</p>', inner_content)
            content_array.extend(p_matches)
        if icpscan_time == content_array[5]:
            pass
        else:
            text1 = """
            ICPScan存在最新更新，请前往以下任意地址获取更新：
            https://pan.quark.cn/s/39b4b5674570#/list/share
            https://github.com/honmashironeko/rankscan
            https://pan.baidu.com/s/1C9LVC9aiaQeYFSj_2mWH1w?pwd=13r5
            """
            print(text1)
            input("请输入回车键继续运行工具")
    except Exception as e:
        print(f"更新模块运行过程中发生异常：{e}")
        print(f"""
            检查更新失败，请前往下载地址查看更新：
            https://pan.quark.cn/s/39b4b5674570#/list/share
            https://github.com/honmashironeko/rankscan
            https://pan.baidu.com/s/1C9LVC9aiaQeYFSj_2mWH1w?pwd=13r5
              """)

def print_rankscan_banner():
    print("=" * 67)
    print("""
  _____            _   _ _  __   _____  _____          _   _ 
 |  __ \     /\   | \ | | |/ /  / ____|/ ____|   /\   | \ | |
 | |__) |   /  \  |  \| | ' /  | (___ | |       /  \  |  \| |
 |  _  /   / /\ \ | . ` |  <    \___ \| |      / /\ \ | . ` |
 | | \ \  / ____ \| |\  | . \   ____) | |____ / ____ \| |\  |
 |_|  \_\/_/    \_\_| \_|_|\_\ |_____/ \_____/_/    \_\_| \_|                                                           
""")
    print("\t\t\t\t\t\t\tVersion:0.3")
    print("\t\t\t\t\t微信公众号:樱花庄的本间白猫")
    print("\t\t\t\t博客地址：https://y.shironekosan.cn")
    print("=" * 67)
    print("\t\tRankscan开始执行")

if __name__ == "__main__":
    update_module()
    print_rankscan_banner()
    parser = argparse.ArgumentParser(description='Rankscan由本间白猫开发,旨在快速查询域名及子域名的百度权重、移动权重、谷歌权重')
    parser.add_argument('-f', dest='file_path', required=True, help='指定使用的路径文件 -f url.txt')
    parser.add_argument('-key', dest='zoomeye_key', help='指定ZoomEye的API-KEY认证信息 -key API-KEY')
    parser.add_argument('-pages', dest='pages', help='指定查询的页数,一页30条子域名,默认1页 -pages 5')
    parser.add_argument('-t', dest='thread', help='指定线程数,默认10 -thread 10')
    args = parser.parse_args()
    file_path = args.file_path
    zoomeye_key = args.zoomeye_key
    pages = args.pages
    thread = args.thread
    if thread is None:
        thread = 10
    main(file_path, zoomeye_key, pages, thread)