#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:ai
# mai: ai@landering.com
from PIL import ImageGrab
import re
import datetime
d_name = datetime.datetime.now()
##print str(d1)
im = ImageGrab.grab()
d_name = re.sub(':','',str(d_name))
name = '%s.png' %d_name
print name
im.save(name) 

#为了方便查看和保存全屏结果，简单写了个截图代码，实战中用处不大