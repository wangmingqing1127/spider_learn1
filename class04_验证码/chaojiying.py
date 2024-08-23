#!/usr/bin/env python
# coding:utf-8

import requests
from hashlib import md5


class Chaojiying_Client(object):
    """
    超级鹰客户端类，用于与超级鹰API进行交互，包括上传图片、上传Base64编码的图片和报告错误。

    初始化时需要提供用户名、密码和软件ID。
    """

    def __init__(self, username, password, soft_id):
        """
        初始化客户端。

        :param username: 用户名
        :param password: 密码，将被加密处理
        :param soft_id: 软件ID
        """
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()  # 对密码进行MD5加密
        self.soft_id = soft_id
        self.base_params = {  # 基本参数，包含用户名、加密后的密码和软件ID
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {  # HTTP请求头，伪装为IE 8浏览器
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        上传图片文件。

        :param im: 图片字节
        :param codetype: 图片的类型代码 参考 http://www.chaojiying.com/price.html
        :return: 服务器返回的JSON数据
        """

        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)  # 更新基本参数
        files = {'userfile': ('ccc.jpg', im)}  # 构造文件上传信息
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def PostPic_base64(self, base64_str, codetype):
        """
        上传Base64编码的图片。

        :param base64_str: Base64编码的图片内容 参考 http://www.chaojiying.com/price.html
        :param codetype: 图片的类型代码
        :return: 服务器返回的JSON数据
        """

        params = {
            'codetype': codetype,
            'file_base64': base64_str  # 添加Base64编码的图片内容
        }
        params.update(self.base_params)  # 更新基本参数
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        报告错误的图片。

        :param im_id: 错误图片的ID
        :return: 服务器返回的JSON数据
        """

        params = {
            'id': im_id,  # 错误图片的ID
        }
        params.update(self.base_params)  # 更新基本参数
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    chaojiying = Chaojiying_Client('wuqingfqng', 'wuqing&fqng', '904357')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('a.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    print(chaojiying.PostPic(im, 1902))  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    # print chaojiying.PostPic(base64_str, 1902)  #此处为传入 base64代码
