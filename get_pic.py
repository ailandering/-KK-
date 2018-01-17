#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:ai
# mail: ai@landering.com

# get_pic.py的核心作用就是截图
from PIL import Image
from PIL import ImageGrab

def window_capture_list(app_name): 
    chicun = ()
    if app_name == 'kk':  #其他平台先根据花椒的来设置变动再说  还没弄
        chicun = (18,140,458,550)
    elif app_name == 'huajiao':  #已经设置完毕
        chicun = (18,140,458,550)
    elif app_name == 'xigua': #已经设置完毕
        chicun = (18,150,458,610)  
    elif app_name == 'yinke': #还没弄
        chicun = (18,140,458,510)  
    else:    #冲顶大会，已经设置完毕
        chicun = (18,150,458,610)
    im = ImageGrab.grab(chicun)
    im.save('general.png') 




