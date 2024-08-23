"""
@Time ： 2024-06-09 14:30
@Auth ： Mr. Wang 86894073
@Company ：wmq @testing.com.cn
@Function ：动态爬取网页信息
"""
import requests

if __name__ == '__main__':
    # 1.准备测试数据
    url = 'https://www.sogou.com/web'
    word = input('请输入要爬取的内容关键字：')
    params = {
        'query': word
    }
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    # 2.模拟发送请求数据
    response = requests.get(url=url, params=params, headers=headers)
    # 3.解析相应数据并保存
    print(response.text)
    with open(file=f'../data/{word}.html', mode='w', encoding='utf8') as f:
        f.write(response.text)
