#coding=utf-8
from PIL import Image  
import pylab
import os
import time
import random

cut = 'adb shell screencap -p /sdcard/autojump.png'
push = 'adb pull /sdcard/autojump.png . '
jump = 'adb shell input swipe {x} {y} {x} {y} {time}'

while True:
    #手机截屏
    os.system(cut)
    time.sleep(0.01)

    #截图上传
    os.system(push)
    time.sleep(0.03)

    pic = Image.open('autojump.png')
    #获取屏幕像素
    (w,h) = pic.size

    #手指点击位置一般在中间偏下。取随机值混淆系统检测

    w = int(w*random.uniform(0.45,0.55))
    h = int(h*random.uniform(0.7,0.8))

    #打开图片
    im = pylab.array(pic)  
    pylab.imshow(im)

    #读取两个点  
    (x1,x2) =pylab.ginput(2)  

    #两点距离公式
    s = ((x1[0]-x2[0])**2 + (x1[1] - x2[1])**2)**0.5
    #print(s)1.38 2.05

    #分辨率与按压时间(ms)的系数
    ratio = 1.38

    #随机更改按压时间使他不是一个整百数
    s = s*ratio + random.randint(-20,20)  
    s = int(s)

    #pylab.close()
    #像手机发送跳远按压时间
    os.system(jump.format(x=w,y=h,time=s))
    time.sleep((s+500)/1000)
