"""
@Time ： 2024-06-09 15:46
@Auth ： Mr. Wang 86894073
@Company ：wmq @testing.com.cn
@Function ：爬取肯德基位置
"""
import json

import requests

if __name__ == '__main__':
    # 1.准备请求数据
    url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/125.0.0.0 Safari/537.36',
    }
    pageIndex = int(input('请输入页码：'))
    city = input('请输入城市：')
    data = {
        'cname': '',
        'pid': '',
        'keyword': city,
        'pageIndex': pageIndex,
        'pageSize': '10'
    }
    # 2.模拟发送请求数据
    response = requests.post(url=url, headers=headers, data=data)
    print(response.text)
    # 3.解析响应数据并持久化保存到文件
    with open('../data/肯德基.json', 'w', encoding='utf-8') as fp:
        json.dump(response.text, fp=fp, ensure_ascii=False)
