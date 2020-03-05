#coding=utf-8
from PIL import Image
import os

def get_filelist(folder):
    try:
        filenames = sorted((fn for fn in os.listdir(folder)
                            if fn.endswith('.png')
                            or fn.endswith('.PNG')
                            or fn.endswith('.jpg')
                            or fn.endswith('.JPG')
                            or fn.endswith('.BMP')
                            or fn.endswith('.bmp')
                            or fn.endswith('.jpeg')
                            or fn.endswith('.JPEG')
                            or fn.endswith('.gif')
                            or fn.endswith('.GIF')
                            ))
        return filenames
    except:
        pass

def add_watermask(img_list,logo,position):
    i = 1
    total = len(img_list)
    for fn in img_list:
        img = Image.open("images/"+fn)
        img_water = Image.open(logo)
        W, H = img.size
        w1, h1 = img_water.size

        if position == "1":
            img.paste(img_water, (10, 10))
        elif position == "2":
            img.paste(img_water, (int((W - w1) / 2), 10))
        elif position == "3":
            img.paste(img_water, (W - w1 - 10, 10))
        elif position == "4":
            img.paste(img_water, (10,int((H-h1)/2)))
        elif position == "5":
            img.paste(img_water, (int((W-w1)/2),int((H-h1)/2)))
        elif position == "6":
            img.paste(img_water, (W-w1-10,int((H-h1)/2)))
        elif position == "7":
            img.paste(img_water, (10,H-h1-10))
        elif position == "8":
            img.paste(img_water, (int((W-w1)/2),H-h1-10))
        elif position == "9":
            img.paste(img_water, (W-w1-10,H-h1-10))
        else:
            print("====位置数字无效，未添加水印！====")
        img.save("result/"+ str(fn))
        print("当前处理第[%d/%d]张图片." % (i, total))
        i += 1

def add_instruction():
    f=open("使用说明.txt","w")
    f.write("===========使用说明===========\n"
            "本程序用来批量添加水印。\n"
            "首先，将水印图片(一张)和程序放在同一目录。\n"
            "首次使用请执行程序，生成两个文件夹images和result。\n"
            "将要添加水印的图片放到images里。\n"
            "然后再执行程序，选择水印添加的位置（9宫格）。回车确认，\n"
            "即可快速批量添加水印。\n"
            "请到result里查看结果。\n"
            "https://ayxwenwan.taobao.com/\n"
            "============================")
    f.close()

if __name__=="__main__":
    if os.path.exists('result'):
        pass
    else:
        os.mkdir("result")
    if os.path.exists('images'):
        pass
    else:
        os.mkdir("images")
    if os.path.exists("使用说明.txt"):
        pass
    else:
        add_instruction()
    try:
        img_list=get_filelist("images")
        logo_list = get_filelist(".")
        if len(logo_list)==0:
            msg = input("未检测到水印文件，请确保水印图和程序同一目录!")
        else:
            logo=logo_list[0]
        #logo = input("[1-输入水印图片名（包括后缀）后回车，确保水印图和程序同一目录。]:")
        print("[1-检测到水印文件: %s]\n"
              "(请确保程序同目录下只有一个水印文件)\n" %logo)
        print("[2-请选择水印的位置后回车：]\n")
        print("|__1__|__2___|__3__|\n"
              "|__4__|__5___|__6__|\n"
              "|__7__|__8___|__9__|\n")
        position = input("1-左上，2-上中，3-上右，\n"
                         "4-中左，5-中心，6-中右，\n"
                         "7-左下，8-下中，9-右下。\n"
                         "请选择:")
        print(position)
        add_watermask(img_list,logo,position)
        msg = input("处理完毕！任意键退出！")
    except:
        pass


