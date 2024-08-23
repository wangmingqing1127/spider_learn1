"""
@Time ： 2024-06-11 10:09
@Auth ： Mr. Wang 86894073
@Company ：wmq @testing.com.cn
@Function ：代理服务器
"""
import requests

'''
代理:破解封IP这种反爬机制。
什么是代理:代理服务器。
代理的作用:
    1.突破自身IP访问的限制。
    2.隐藏自身真实IP
代理相关的网站:
    快代理
    西祠代理
    www.goubanjia.com
代理ip的匿名度:
    透明:服务器知道该次请求使用了代理，也知道请求对应的真实ip
    匿名:知道使用了代理，不知道真实ip
    高匿:不知道使用了代理，更不知道真实的ip
'''

# 创建一个requests的会话对象，用于后续的HTTP请求
session = requests.Session()

# 定义请求的URL，用于搜索IP相关信息
url = 'https://www.baidu.com/s?wd=ip'

# 定义请求头，模拟浏览器访问，避免被识别为爬虫
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 Safari/537.36'
}

# 定义代理服务器，用于通过代理访问网页
proxy = {
    'https': '127.0.0.1'
}

# 设置会话的代理，使用定义的代理服务器
session.proxies = proxy

# 发起GET请求，获取搜索结果页面内容
baidu_result = session.get(url=url, headers=headers)

# 打印响应头，用于查看服务器返回的HTTP信息
print(baidu_result.headers)

# 将搜索结果页面内容写入到文件中
with open(file='./ip.html', mode='w', encoding='utf8') as f:
    f.write(baidu_result.text)
