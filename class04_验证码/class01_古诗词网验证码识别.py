"""
@Time ： 2024-06-11 07:42
@Auth ： Mr. Wang 86894073
@Company ：wmq @testing.com.cn
@Function ：验证码识别
"""
import requests
from lxml import etree

from class04_验证码.chaojiying import Chaojiying_Client

'''
实战:识别古诗文网登录页面中的验证码。
使用打码平台识别验证码的编码流程:
    1.将验证码图片进行本地下载
    2.调用平台提供的示例代码进行图片数据识别
'''
# 定义古诗文网登录页面的URL，用于后续的请求
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

# 设置请求头，模拟浏览器访问，以获取正确的响应
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 Safari/537.36'
}

# 发送GET请求，获取登录页面的内容
result = requests.get(url=url, headers=headers).text

# 使用lxml库的HTML解析器，将获取的页面内容解析为HTML树结构
tree = etree.HTML(result)

# 通过XPath表达式，获取验证码图片的src属性值
img_list = tree.xpath('//img[@id="imgCode"]/@src')

# 构造验证码图片的完整URL，并发送GET请求，下载图片
img_url = 'https://so.gushiwen.cn' + img_list[0]
img_result = requests.get(url=img_url, headers=headers).content

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
print(f'超级鹰返回值：{verify_result}')
print(f'验证码为：{verify_result.get("pic_str")}')
