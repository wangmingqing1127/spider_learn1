"""
@Time ： 2024-06-09 13:52
@Auth ： Mr. Wang 86894073
@Company ：wmq @testing.com.cn
@Function ：requests
"""
import requests

'''
requests请求步骤：
    1.准备请求数据
    2.模拟请求发送数据
    3.解析相应数据，并保存
'''

# 爬取百度首页数据

# 1.准备请求数据
url = 'https://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

# 2.模拟请求发送数据
responses = requests.get(url=url, headers=headers)

# 3.解析相应数据，并保存
print(responses.text)
with open(file='../data/百度首页.html', mode='w', encoding='utf8') as f:
    f.write(responses.text)
