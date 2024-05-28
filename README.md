# 工具介绍

- 支持子域名、主域名批量查询权重。
- 支持提取主域名后，快速获取其他子域名。
- 支持百度、移动、谷歌三种权重都为 0 时，不显示在CMD中便于阅读。
- 将有权重和没有权重的结果分别自动保存在 Excel 中，方便后续操作和记录。
- 白嫖余额不足时只停止子域名查询，并记录剩余未查询的域名。
- 增加线程数控制，可根据网络环境提高运行效率，默认 10 线程。
- 与 [icpscan](https://github.com/honmashironeko/icpscan) 工具可以联合使用，快速获取备案归属及权重信息。（目前手动，自动化待完成）

# 下载地址

- Github：https://github.com/honmashironeko/rankscan/releases

- 夸克网盘：https://pan.quark.cn/s/39b4b5674570#/list/share

- 百度网盘：https://pan.baidu.com/s/1C9LVC9aiaQeYFSj_2mWH1w?pwd=13r5/

**求 Github 点一下 Star，非常感谢您**

# 使用帮助

- 安装相关依赖库：`pip install -r requirements.txt`

- 查看工具帮助：`python RANKscan-v0.3.py -h`

  ![Clip_2024-05-28_11-05-22](https://github.com/honmashironeko/rankscan/assets/139044047/70392207-acfe-4f78-bd6f-a4efd092412e)


- 执行基础功能：`python RANKscan-v0.3.py -f domain.txt` 这样将会查询您提供的 TXT 文件中所有域名的权重。

- 执行进阶功能:`python RANKscan-v0.3.py -f domain.txt -key XXXXX` 这样将会自动反查子域名，并在后续步骤中查询权重。

# 工具截图

![Clip_2024-05-28_11-05-51](https://github.com/honmashironeko/rankscan/assets/139044047/f3986acb-509c-49f0-a1a7-6e9c6af99801)

![Clip_2024-05-28_11-08-03](https://github.com/honmashironeko/rankscan/assets/139044047/134c5fa8-d77b-499b-a8d5-310c35936996)

![Clip_2024-05-28_11-08-14](https://github.com/honmashironeko/rankscan/assets/139044047/c2115a99-fba6-4758-9e2d-42b1a866774e)

# 为爱发电

本项目及其他项目并不要求付费，如果您觉得工具好用，欢迎大家打赏一下，支持作者~

# 联系方式

![樱花庄_搜索联合传播样式-标准色版](https://github.com/honmashironeko/rankscan/assets/139044047/968215a8-1b3e-4e43-bbc5-c36a907b3e82)

# 特别鸣谢

感谢以下师傅们为本项目的大力支持！（排名不分先后）

- 夜のとばりの翼

# 更新日志

**2024年5月28日**

1. 新增功能白嫖余额不足时只停止子域名查询，并记录剩余未查询的域名。
2. 增加没有权重的结果保存到 Excel 表格中。
3. 增加线程数控制，可根据网络环境提高运行效率，默认 10 线程。
4. 优化代码运行逻辑。

**2024年5月27日**

1. 发布首个测试版本。
