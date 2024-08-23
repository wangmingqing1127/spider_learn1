"""
@Time ： 2024-06-10 15:34
@Auth ： Mr. Wang 86894073
@Company ：wmq @testing.com.cn
@Function ：xpath
"""
import os
import requests
from lxml import etree

'''
xpath解析:最常用且最便捷高效的一种解析方式。通用性。
    xpath解析原理:
        1.实例化etree对象，且要将被解析的页顶源码数据加载到该对象中。
        2.调用etree对象的xpath方法，传入xpath表达式。
        
    环境的安装:
        pip install lxml
        
    如何实例化-个etree对象:from lxml import etree
        1.将本地的html文档中的源码数据加载到etree对象中:
            etree.parse(filePath)
        2.可以将从互联网上获取的源码数据加载到该对象中
            etree.HTML('page text')
        3. xpath('xpath表达式')
    - xpath表达式:
         /:表示的是从根节点开始定位。表示的是一个层级。
        //:表示的是多个层级。可以表示从任意位置开始定位。
        属胜定位://div[@class='song']   tag[@attrName="attrValue"]
        索引定位://div[@class="song"]/p[3]  索引是从1开始的。
        取文本:
            /text(): 获取的是标签中直系的文本内容
            //text(): 标签中非直系的文本内容(所有的文本内容)
        取属性:
            /@attrName  ==>img/src

'''


# 从汽车之家网站获取二手车的数据
def get_car_data():
    # 定义汽车之家北京212吉普车页面的URL
    url = 'https://car.autohome.com.cn/2sc/china/beiqizhizao/bj212/a0_0msdgscncgpi1lto2cspex/'
    # 定义请求头，模拟浏览器访问，以避免被网站识别为自动化请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/114.0.0.0 Safari/537.36'
    }
    # 发送GET请求，获取网页内容
    result = requests.get(url=url, headers=headers)
    # 使用lxml库的HTML解析器，将获取的网页内容解析为HTML树结构
    tree = etree.HTML(result.text)
    # 使用XPath表达式，从HTML树中提取车辆标题
    car_title = tree.xpath('//div[@class="piclist"]//li//div[@class="title"]/a/text()')
    # 使用XPath表达式，从HTML树中提取车辆价格
    car_price = tree.xpath('//div[@class="piclist"]//li//div[@class="detail-r"]/span/text()')
    # 打开文件，准备将提取到的车辆数据写入文本文件
    car_info = open(file='../data/car_data.txt', mode='w', encoding='utf-8')
    # 将车辆标题和价格进行组合，形成元组的列表
    zip_list = zip(car_title, car_price)
    data = list(zip_list)
    # 遍历数据列表，将每辆车的标题和价格写入文件
    for i in data:
        car_info.write(f'{i[0]}    价格为：￥{i[1]}万\n')
    # 关闭文件
    car_info.close()


def get_wallpaper_from_web():
    """
    从网络下载动态壁纸。
    该函数首先检查是否存在名为pictures的目录，如果不存在，则创建它。
    然后，它会访问一个网页并下载页面中列出的图片。
    """
    # 检查是否存在图片目录，不存在则创建
    if not os.path.exists('./pictures'):
        os.mkdir('./pictures')

    # 设置请求头，伪装为Chrome浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/114.0.0.0 Safari/537.36'
    }

    # 循环遍历页面，目前设定为遍历2个页面
    for number in range(1, 3):
        # 构造页面URL
        url = f'https://pic.netbian.com/4kdongman/index_{number}.html'
        # 第一页使用特定URL
        if number == 1:
            url = 'https://pic.netbian.com/4kdongman/index.html'

        # 发送HTTP请求，获取页面内容
        result = requests.get(url=url, headers=headers)
        # 自动识别并设置编码方式，解决乱码问题
        result.encoding = result.apparent_encoding
        # 使用lxml解析HTML页面
        tree = etree.HTML(result.text)

        # 查找并获取所有图片元素
        li_list = tree.xpath('//div[@class="slist"]//li')
        for li in li_list:
            # 构造图片URL
            # [0] 在这里的作用是提取 XPath 查询结果中的第一个匹配项
            img_url = 'https://pic.netbian.com/' + li.xpath('./a//img/@src')[0]
            # 从图片元素中获取图片名称，并替换不允许的字符
            # windows不让用*
            img_name = (li.xpath('./a//img/@alt')[0]).replace("*", "") + '.jpg'

            # 发送HTTP请求，获取图片内容
            img_result = requests.get(url=img_url, headers=headers)
            # 自动识别并设置编码方式
            img_result.encoding = img_result.apparent_encoding

            # 拼接图片保存的路径
            path = './pictures/' + img_name
            # 以二进制写入模式打开文件，保存图片内容
            with open(file=path, mode='wb') as f:
                print(f'正在下载:{img_name}')
                f.write(img_result.content)


def get_weather_data():
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/114.0.0.0 Safari/537.36'
    }
    result = requests.get(url=url, headers=headers).text
    tree = etree.HTML(result)
    city_list = tree.xpath('//div[@class="row"]/div[1]//li//a//text()')
    print(f'城市总数量为：{len(list(set(city_list)))}')
    print(f'城市列表为：{list(set(city_list))}')


if __name__ == '__main__':
    get_car_data()
    get_wallpaper_from_web()
    get_weather_data()
