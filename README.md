# 工具介绍

- 支持子域名、主域名批量查询权重。
- 支持提取主域名后，快速获取其他子域名。
- 支持百度、移动、谷歌三种权重都为 0 时，不显示在CMD中。
- 将结果自动保存在 Excel 中，方便后续操作和记录。
- 白嫖余额不足时只停止子域名查询，并记录剩余未查询的域名。（待完成）
- 与 [icpscan](https://github.com/honmashironeko/icpscan) 工具可以联合使用，快速获取备案归属及权重信息。（目前手动，自动化待完成）

# 下载地址

- Github：https://github.com/honmashironeko/rankscan/releases

- 夸克网盘：https://pan.quark.cn/s/39b4b5674570#/list/share

- 百度网盘：https://pan.baidu.com/s/1C9LVC9aiaQeYFSj_2mWH1w?pwd=13r5/


**求 Github 点一下 Star，非常感谢您**

# 使用帮助

- 安装相关依赖库：`pip install -r requirements.txt`

- 查看工具帮助：`python RANKscan-v0.2.py -h`

- ![Clip_2024-05-27_16-56-50](./assets/Clip_2024-05-27_16-56-50.png)


- 执行基础功能：`python RANKscan-v0.2.py -f domain.txt` 这样将会查询您提供的 TXT 文件中所有域名的权重。

- 执行进阶功能:`python RANKscan-v0.2.py -f domain.txt -key XXXXX` 这样将会自动反查子域名，并在后续步骤中查询权重。


# 工具截图

![Clip_2024-05-27_16-59-40](./assets/Clip_2024-05-27_16-59-40.png)

![Clip_2024-05-27_17-00-05](./assets/Clip_2024-05-27_17-00-05.png)

# 为爱发电

本项目及其他项目并不要求大家付费，但是应部分师傅好意，因此留下打赏码，如果您觉得工具好用，欢迎大家打赏一下，支持作者~

![img](https://private-user-images.githubusercontent.com/139044047/331065651-50ffc1be-6c2a-45cc-8e19-4e8606e96f60.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTY4MDA3NjQsIm5iZiI6MTcxNjgwMDQ2NCwicGF0aCI6Ii8xMzkwNDQwNDcvMzMxMDY1NjUxLTUwZmZjMWJlLTZjMmEtNDVjYy04ZTE5LTRlODYwNmU5NmY2MC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNTI3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDUyN1QwOTAxMDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yMDRkYmM1NWZiNWNmMDRjZmZlN2IwN2Q1NDkxZWU1ZThiMGY2Yjg4ODY0OGMxMjliMTgwOTk4NzFkOTViMDRjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.BpBCk1Aeyanh9F1kChMvxtRuJlPAwY7E-XEMwaeLvj4)

![img](https://private-user-images.githubusercontent.com/139044047/331065673-ffa9661d-caaf-4840-b95d-3309d636fce9.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTY4MDA3NjQsIm5iZiI6MTcxNjgwMDQ2NCwicGF0aCI6Ii8xMzkwNDQwNDcvMzMxMDY1NjczLWZmYTk2NjFkLWNhYWYtNDg0MC1iOTVkLTMzMDlkNjM2ZmNlOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNTI3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDUyN1QwOTAxMDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wODhiYWI3MTc3ZDdkNjNjOTM4YmFlMmVmYzkyMGMyMWM1NzY5Zjc5OGQxZGNmZmYzYjlkZjk5ZWFjZmY5NzAyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Rt21MhJZu2AOD_AFr37GtVyui0nMsMGKmgWEUfyO97g)

# 联系方式

![樱花庄_搜索联合传播样式-标准色版](./assets/%E6%A8%B1%E8%8A%B1%E5%BA%84_%E6%90%9C%E7%B4%A2%E8%81%94%E5%90%88%E4%BC%A0%E6%92%AD%E6%A0%B7%E5%BC%8F-%E6%A0%87%E5%87%86%E8%89%B2%E7%89%88-1716800434440-4.png)

# 更新日志

**2024年5月27日**

1. 发布首个测试版本。