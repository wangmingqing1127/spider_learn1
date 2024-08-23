"""
@Time ： 2024-06-09 15:33
@Auth ： Mr. Wang 86894073
@Company ：wmq @testing.com.cn
@Function ：爬取豆瓣电影动作片排行榜
"""
import json

import requests

if __name__ == '__main__':
    # ajax 异步请求
    # 1.准备请求数据
    url='https://movie.douban.com/j/chart/top_list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/125.0.0.0 Safari/537.36',
    }
    params = {
        'type': '5',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20',
    }
    # 2.模拟发送数据
    response = requests.get(url=url, params=params, headers=headers)
    # 3.解析数据并持久化存储
    print(response.json())
    with open('../data/douban_movie.json', 'w', encoding='utf-8') as fp:
        json.dump(response.json(), fp=fp, ensure_ascii=False)