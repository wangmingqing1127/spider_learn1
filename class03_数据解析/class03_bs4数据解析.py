"""
@Time ： 2024-06-10 10:53
@Auth ： Mr. Wang 86894073
@Company ：wmq @testing.com.cn
@Function ：BeautifulSoup
"""
import requests
from bs4 import BeautifulSoup

'''
bs4进行数据解析
    - 数据解析的原理:
        1.标签定位
        2.提取标签、标签属性中存储的数据值
    - bs4数据解析的原理:
        1.实例化一个Beautifulsoup对象，并且将页面源码数据加载到该对象中
        2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
    - 环境安装:
        pip install Beautifulsoup

    - 如何实例化BeautifulSoup对象:
        - from bs4 import BeautifulSoup
        - 对象的实例化:
            1.将本地的html文档中的数据加载到该对象中
                file=open('./file.html','r',encoding='utf8')
                soup=BeautifulSoup(file,'html.parser')
            2.将互联网上获取的页面源码加载到该对象中
                page_text=response.text
                soup=BeautifulSoup(page_text,'html.paser')
        - BeautifulSoup常用的属性和方法
            soup.标签名称:返回的是文档中第一次出现的标签
            - soup.find():
                - find('标签名称'):等同于soup.div
                - 属性定位:
                    soup.find('div',标签/class_/id/attr='song')
                - soup.find_all('标签名称'):返回符合要求的所有标签(列表)
                    find_all(name, attrs, recursive, text, **kwargs)
                        目的: 该方法用于查找文档中匹配给定条件的所有标签。
                        参数:
                        name: 标签名，可以是字符串也可以是正则表达式，如果省略，则匹配所有标签。
                        attrs: 一个字典或True，用于匹配HTML元素的属性，如{'class': 'special'}。
                        recursive: 布尔值，默认为True，决定是否在子孙节点中递归搜索。
                        text: 字符串或函数，用于匹配元素的文本内容。
                        其他关键字参数可用于更复杂的筛选条件。
                        返回值: 返回一个包含所有匹配元素的列表。

            select:
                - select('CSS选择器(id #，class .，标签...选择器)'),返回的是一个列表
                    select(selector)
                        目的: 该方法基于CSS选择器来查找文档中的元素，提供了更强大且灵活的选择能力。
                        参数:
                        selector: 一个字符串，表示CSS选择器表达式，如'#myId .myClass'。
                        返回值: 同样返回一个包含所有匹配元素的列表
                - 层级选择器:
                    - soup.select('.tang>ul>li>a'):>表示的是一个层级
                    - soup.select('.tang>ula'):空格表示的多个层级
            获取标签之间的文本数据:
                - soup.a.text/string/get text()
                -text/get text():可以获取某一个标签中所有的文本内容
                -string:只可以获取该标签下面直系的文本内容
            获取标签中属性值:
                soup.al['href']
'''

# 定义访问的URL，此处为目标网站的首页地址
url = 'https://www.baidu.com/'

# 定义请求头，模拟浏览器访问，以避免被网站识别为自动化请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 Safari/537.36'
}

# 发送HTTP GET请求，获取网页内容，并将其转换为文本格式
# 这里使用requests库的get方法来发送HTTP请求，并获取响应的文本内容
res = requests.get(url=url, headers=headers).text

# 将获取的网页内容写入到文件中，以供后续分析或离线查看
# 使用with语句确保文件正确打开和关闭，并指定编码格式为UTF-8
with open('../data/baidu.html', 'w', encoding='utf8') as f:
    f.write(res)

# 使用BeautifulSoup库解析HTML响应内容，以便进行网页解析和数据提取
soup = BeautifulSoup(res, 'lxml')

# 输出网页的标题，用于确认当前解析的网页主题
print(soup.title)

# 尝试获取页面中class为'bg s_btn'的input元素，用于获取或操作按钮等交互元素
print(soup.find('input', class_='bg s_btn'))

# 获取所有link元素，这些通常用于引入CSS样式文件或图标等资源
print(soup.find_all('link'))

# 选择id为'lg'的元素下的map元素下的所有area元素，用于处理图像映射中的链接
print(soup.select('#lg > map > area'))

# 直接访问soup中的input元素的'value'属性，用于获取输入字段的默认值
print(soup.input['value'])

# 获取class为'bg s_btn'的input元素的'value'属性，用于获取按钮的具体文本或值
print(soup.find('input', class_='bg s_btn')['value'])

# 爬取红楼梦 https://www.shicimingju.com/book/hongloumeng.html

# 定义请求的URL和请求头
url = 'https://www.shicimingju.com/book/hongloumeng.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 Safari/537.36'
}

# 发送GET请求并获取响应
result = requests.get(url=url, headers=headers)

# 使用BeautifulSoup解析HTML内容，指定解析器和编码
# 使用content属性和BeautifulSoup来自动检测正确的编码
soup = BeautifulSoup(result.content, 'lxml', from_encoding=result.apparent_encoding)

# 选择所有章节链接的列表项
l_list = soup.select('.book-mulu > ul > li')

# 打开目标文件，用于写入爬取的内容
fp = open('../data/hongloumeng.txt', 'w', encoding='utf8')

# 定义基础详情页URL
base_detail_url = 'https://www.shicimingju.com'

# 遍历列表项，爬取每个章节的内容
for li in l_list:
    # 提取章节标题
    title = li.a.text
    # 提取章节链接
    detail_url = li.a['href']
    # 发送GET请求获取章节详情页内容
    detail_result = requests.get(url=f'{base_detail_url}{detail_url}', headers=headers)
    # 解析章节详情页内容
    detail_soup = BeautifulSoup(detail_result.content, 'lxml', from_encoding=result.apparent_encoding)
    # 提取章节内容
    content = detail_soup.find('div', class_='chapter_content').text
    # 打印当前章节标题，用于调试反馈
    print(f'正在爬取：{title}')
    # 将章节标题和内容写入文件
    fp.write(f'{title}\n{content}\n\n')

# 关闭文件
fp.close()
