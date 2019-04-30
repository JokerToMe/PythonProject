# 使用第三方模块

# pip安装：
# windows：需要在安装python的时候勾选
# Mac和Linux：自带无需安装

# 安装一个三方模块，需要知道模块的名字
# Pillow：强大的处理图像的工具模块

from PIL import Image

# 打开图片
im = Image.open('suolong.jpg')
print(im.format,im.size,im.mode)
# 设置图片的大小
im.thumbnail((150,100))
# 生成缩略图
im.save('temp.jpg','JPEG')







