"""
@Time ： 2024-06-11 08:46
@Auth ： Mr. Wang 86894073
@Company ：wmq @testing.com.cn
@Function ：模拟登录
"""

# 导入requests库，用于发送HTTP请求
import requests
# 导入re库，用于正则表达式匹配
import re
# 导入etree库，用于解析HTML文档
from lxml import etree
# 导入Chaojiying_Client类，用于处理验证码
from class04_验证码.chaojiying import Chaojiying_Client

'''
http/https协议特性:无状态。
没有请求到对应页面数据的原因:
    发起的第二次基于个人主页页面请求的时候，服务器端并不知道该此请求是基于登录状态下的请求
cookie:用来让服务器端记录客户端的相关状态。
    1.手动处理:通过抓包工具获取cookie值，将该值封装到headers中。(不建议)
    2.自动处理:
        1.cookie值的来源是哪里?
            模拟登录post请求后，由服务器端创建。
        2.session会话对象:
            作用:
                1.可以进行请求的发送。
                2.如果请求过程中产生了cookie，则该cookie会被自动存储/携带在该session
        3.使用
            创建-个session对象:session=requests.Session()
            使用session对象进行模拟登录post请求的发送(cookie就会被存储在session对象中)
            session对象对个人主页对应的get请求进行发送(携带了cookie)

使用Session有以下几点主要优势：
1.保持会话状态：Session对象可以在多个请求之间保持某些参数（如cookies），这对于需要登录认证的网站特别重要。当你登录后，
            Session会自动管理cookie，这样在后续的请求中就不需要手动管理这些cookie信息了，使得连续的请求更像是浏览器中的浏览行为，
            有助于通过那些基于cookie的身份验证机制。
2.性能优化：Session对象会在底层自动处理和重用TCP连接，这在进行大量请求时可以减少建立和关闭连接的开销，从而提高效率。
3.简化代码：如果你需要在多个请求间复用相同的设置（如headers），使用Session可以避免重复代码，
        因为这些设置只需要配置一次，在该Session实例的所有请求中都会应用。
'''

# 定义古诗文网登录页面的URL，用于后续的请求
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
# 设置请求头，模拟浏览器访问，以获取正确的响应
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 Safari/537.36'
}
# 创建会话对象，用于保持会话状态
session = requests.Session()
# 发送GET请求，获取登录页面的内容
result = session.get(url=url, headers=headers).text
# 通过正则表达式提取VIEWSTATE值
VIEWSTATE = re.findall(r'id="__VIEWSTATE" value="(.*?)" />', result)[0]
# 通过正则表达式提取VIEWSTATEGENERATOR值
VIEWSTATEGENERATOR = re.findall(r'id="__VIEWSTATEGENERATOR" value="(.*?)" />', result)[0]
# 打印VIEWSTATE和VIEWSTATEGENERATOR的值
# print(VIEWSTATE)
# print(VIEWSTATEGENERATOR)
# 使用lxml库的HTML解析器，将获取的页面内容解析为HTML树结构
tree = etree.HTML(result)
# 通过XPath表达式，获取验证码图片的src属性值
img_list = tree.xpath('//img[@id="imgCode"]/@src')
# 构造验证码图片的完整URL，并发送GET请求，下载图片
img_url = 'https://so.gushiwen.cn' + img_list[0]
# 下载验证码图片
img_result = session.get(url=img_url).content
# 将下载的验证码图片保存到本地文件
with open(file='./verify/verify.jpg', mode='wb') as f:
    f.write(img_result)
# 初始化超级鹰验证码平台的客户端
chaojiying = Chaojiying_Client('wuqingfqng', 'wuqing&fqng', '904357')  # 用户中心>>软件ID 生成一个替换 96001
# 读取本地保存的验证码图片文件，并转换为二进制数据
im = open('./verify/verify.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
# 调用超级鹰客户端的PostPic方法，上传验证码图片，获取验证码文字
verify_result = chaojiying.PostPic(im, 1902)  # 1902 验证码类型 常见4~6位英文数字	  官方网站>>价格体系 3.4+版 print 后要加()
# 输出超级鹰返回的结果，以及其中的验证码文字
# print(f'超级鹰返回值：{verify_result}')
# print(f'验证码为：{verify_result.get("pic_str")}')
verify_code = verify_result.get("pic_str")
# 定义登录数据
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
data = {
    '__VIEWSTATE': VIEWSTATE,
    '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
    'from': 'https://www.gushiwen.cn/',
    'email': '86894073@qq.com',
    'pwd': '!QAZ2wsx',
    'code': verify_code,
    'denglu': '登录'
}
# 发送登录请求
# session=requests.session()
login_result = session.post(url=login_url, data=data)
# 打印登录结果的状态码和内容
# print(login_result.status_code)
# print(login_result.text)
# 将登录结果保存到文件
with open(file='./登录结果.html', mode='w', encoding='utf8') as f:
    f.write(login_result.text)

collect_result = session.get(url='https://so.gushiwen.cn/user/collect.aspx').text
with open(file='./个人收藏.html', mode='w', encoding='utf8') as f:
    f.write(collect_result)
