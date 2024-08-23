"""
@Time ： 2024-06-11 14:03
@Auth ： Mr. Wang 86894073
@Company ：wmq @testing.com.cn
@Function ：多进程
"""
import random
import re
import requests
from multiprocessing import Process
from lxml import etree


'''
高性能异步爬虫
    目的:在爬虫中使用异步实现高性能的数据爬取操作，
    异步爬虫的方式:
        1.多线程，多进程(不建议):
            好处:可以为相关阻塞的操作单独开启线程或者进程，阻塞操作就可以异步执行。
            弊端:无法无限制的开启多线程或者多进程。
        2.线程池、进程池(适当的使用):
            好处:我们可以降低系统对进程或者线程创建和销毁的一个频率，从而很好的降低系统的开销
            弊端:池中线程或进程的数量是有上限。
            
        3.单线程+异步协程(推荐)
        
        event loop:事件循环，相当于 一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足某些条件的时候，函数就会被循环执行。
        
        coroutine:协程对象，我们可以将协程对象注册到事件循环中，它会被事件循环调用。可以使用 async 关键字来定义一个方法，
                这个方法在调用时不会立即被执行，而是返回 一个协程对象。
                
        task:任务，它是对协程对象的进一步封装，包含了任务的各个状态。
        
        future:代表将来执行或还没有行的任务，实际上和 task 没有本质区
        
        async 定义一个协程
        
        await
        用来挂起阻塞方法的执行。
'''

# 定义请求头，模拟浏览器访问，以避免被网站识别为自动化请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 Safari/537.36'
}

def download_image(url):
    """
    下载网络图像。
    参数:url (str): 图像的URL地址。
    该函数使用requests库下载指定URL的图像，并将其保存为随机文件名的JPEG格式文件。
    """

    pic_result = requests.get(url=url, headers=headers)
    image_id = random.randint(1, 1000)
    with open(f'{image_id}.jpg', 'wb') as f:
        f.write(pic_result.content)

if __name__ == '__main__':
    url = 'https://www.pearvideo.com/category_1'
    logo_result = requests.get(url=url, headers=headers)
    logo_result.encoding = logo_result.apparent_encoding

    # 解析页面获取图片样式链接
    tree = etree.HTML(logo_result.text)
    video_detail = tree.xpath('//div[@class="category-top"]//li//div[@class="img"]/@style')

    # 初始化一个进程列表，用于存储后续创建的下载进程
    # 使用多进程下载图片
    processes = []
    for style_url in video_detail:
        true_url = re.findall(r'url\((.*?)\);', style_url)[0]
        p = Process(target=download_image, args=(true_url,))
        p.start()
        processes.append(p)

    # 等待所有下载进程完成
    # 等待所有进程完成
    for p in processes:
        p.join()

    print("所有图片下载完成。")

