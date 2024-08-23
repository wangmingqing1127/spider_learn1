"""
@Time ： 2024-06-09 14:56
@Auth ： Mr. Wang 86894073
@Company ：wmq @testing.com.cn
@Function ：百度翻译
"""
import json

import requests

if __name__ == '__main__':
    # Ajax异步请求 局部刷新 找准请求地址即可
    # 1.准备测试数据
    url = 'https://fanyi.sogou.com/reventondc/suggV3'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        # 'Referer':'https://fanyi.sogou.com/text?keyword=test&transfrom=auto&transto=en&model=general',
        # 'Origin': 'https://fanyi.sogou.com'

    }
    words = input('请输入要翻译的内容：')
    data = {
        'text': words,
        'addSugg': 'on',
        'pid': 'sogou-dict-vr'
        # 'client':'web',
        # 'from': 'en',
        # 'to': 'zh-CHS',
        # 'uuid':'799163a4-228e-49cb-9c3c-b006d6c9ac35',
    }
    # 2.模拟请求发送数据
    responses = requests.post(url=url, headers=headers, data=data)
    # 3.解析相应数据并保存
    print(responses.text)
    # 使用with语句打开文件，确保文件操作的安全性
    # 文件路径使用字符串格式化方法，动态生成，方便后续扩展
    # 文件模式设置为'w'，表示写入模式，打开文件后将覆盖原有内容
    # 编码方式设置为'utf8'，确保处理中文字符时不会出现乱码
    with open(f'../data/{words}.json', mode='w', encoding='utf8') as f:
        # 使用json.dump函数将responses中的json数据写入到打开的文件中
        # ensure_ascii=False参数确保中文字符能够正常输出，不会被转义
        json.dump(responses.json(), fp=f, ensure_ascii=False)
