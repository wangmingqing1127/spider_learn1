"""
@Time ： 2024-06-10 09:47
@Auth ： Mr. Wang 86894073
@Company ：wmq @testing.com.cn
@Function ：图片爬取
"""
import os.path
import re

import requests

'''
<span class="wallpapers__canvas">
  <img class="wallpapers__image" src="https://images.wallpaperscraft.com/image/single/girl_smile_fish_1005833_300x168.jpg" alt="Preview wallpaper girl, smile, fish, anime, colorful">
</span>
<span class="wallpapers__canvas">
  <img class="wallpapers__image" src="https://images.wallpaperscraft.com/image/single/piano_silhouette_space_156662_300x168.jpg" alt="Preview wallpaper piano, silhouette, space, illusion, anime">
</span>

请求地址
https://wallpaperscraft.com/catalog/anime/3840x2160/page1
预览图片地址
https://images.wallpaperscraft.com/image/single/girl_smile_fish_1005833_300x168.jpg
https://images.wallpaperscraft.com/image/single/piano_silhouette_space_156662_300x168.jpg
'''

if __name__ == '__main__':
    # 检查是否存在名为wallpapers的目录，如果不存在，则创建它
    # 保存数据到指定的文件夹
    if not os.path.exists('./wallpapers'):
        os.mkdir('./wallpapers')
    # 定义请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.75 Safari/537.36'
    }
    # 遍历网页
    for number in range(1, 3):
        # 构造请求URL，获取指定页面的壁纸列表
        url = f'https://wallpaperscraft.com/catalog/anime/3840x2160/page{number}'

        # 发送请求，获取网页内容
        result = requests.get(url=url, headers=headers).text  # text(字符串)、json(json数据对象)、content(二进制)
        # 使用正则表达式提取网页中的图片URL
        pic_list = re.findall(r'<img class="wallpapers__image" src="(.*?)" alt=', result)
        print(f'当前第{number}页，需要下载{len(pic_list)}张图片！')
        # 遍历提取到的图片URL，下载每张图片
        for pic in pic_list:
            pic_url = pic
            pic_name = pic.split('/')[-1]
            # 发送请求，获取图片内容
            # 3.解析响应数据并保存到本地
            pic_current = requests.get(url=pic_url, headers=headers).content
            # 将图片内容写入到本地文件
            with open(f'./wallpapers/{pic_name}', 'wb') as f:
                print(f'正在下载：{pic_name}')
                f.write(pic_current)
