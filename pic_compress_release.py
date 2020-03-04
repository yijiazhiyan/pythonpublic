#coding=utf-8
import os
from PIL import Image

def get_filelist():
    try:
        filenames = sorted((fn for fn in os.listdir('.')
                            if fn.endswith('.png')
                            or fn.endswith('.PNG')
                            or fn.endswith('.jpg')
                            or fn.endswith('.JPG')
                            or fn.endswith('.BMP')
                            or fn.endswith('.bmp')
                            or fn.endswith('.jpeg')
                            or fn.endswith('.JPEG')
                            ))
        return filenames
    except:
        pass

def compress(img_list,w1):
    i = 1
    total = len(img_list)
    try:
        for fn in img_list:
            img = Image.open(fn)
            w,h=img.size
            h1=int((w1*h)/w)
            img.resize((w1, h1), Image.ANTIALIAS).save("result/"+ str(fn))
            print("当前处理第[%d/%d]张图片." % (i, total))
            i+=1
    except Exception as e:
        print(e)

if __name__=="__main__":
    if os.path.exists('result'):
        pass
    else:
        os.mkdir("result")
    try:
        w0 = input("[请输入压缩后图片的宽度(整数），(长度将按比例自动缩放)]: ")
        w1 = int(w0.strip())
        img_list = get_filelist()
        compress(img_list, w1)
        msg = input("处理完毕！任意键退出！")
    except:
        print("请输入整数！")
        msg = input("异常退出！")

