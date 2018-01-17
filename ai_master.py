#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:ai 
#mail:ai@landering.com

from __future__ import division 
import urllib
import urllib2
import re
from bs4 import BeautifulSoup as BS
from baidu_scan import baidu_scan_py
import datetime
from get_pic import window_capture_list
from PIL import ImageGrab
import re
import datetime
import subprocess
import os

d1 = datetime.datetime.now()


'''已经设置好不同平台的截屏参数，需要哪个平台，把其他平台删除标注即可'''
#window_capture_list('kk')
window_capture_list('huajiao') 
#window_capture_list('xigua')
#window_capture_list('chongding')
#window_capture_list('yinke')

d_name = datetime.datetime.now()
im = ImageGrab.grab()
d_name = re.sub(':','',str(d_name))
name = '%s.png' %d_name
im.save(name) 


def setClipboardData(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    p.communicate()

list_sum = baidu_scan_py()  

question = list_sum[0].encode('utf-8')
ans1 = list_sum[1].encode('utf-8')
ans2 = list_sum[2].encode('utf-8')
ans3 = list_sum[3].encode('utf-8')

#将题目和回答中无用的词语剔除
def sub_del(del_item):
    dict_del={'《':'','》':'','？':'','哪个':'','以下':'','"':'','“':'','”':'','1.':'','2.':'','3.':'','4.':'','5.':'','6.':'','7.':'','8.':'','9.':'','10.':'','11.':'','12.':''}
    for key,value in dict_del.items():
        #print 'key',key
        if key in del_item:
            del_item = re.sub(key,value,del_item)
    return del_item

question = sub_del(question)
ans1 = sub_del(ans1)
ans2 = sub_del(ans2)
ans3 = sub_del(ans3)

print question,ans1,ans2,ans3

#开始百度搜索程序
baseUrl = 'http://www.baidu.com/s'
page = 1 
word = question  

data = {'wd':word,'pn':str(page-1)+'0','tn':'baidurt','ie':'utf-8','bsst':'1'}
data = urllib.urlencode(data)
url = baseUrl+'?'+data

try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
except urllib2.HttpError,e:
    print e.code
    exit(0)
except urllib2.URLError,e:
    print e.reason
    exit(0)

html = response.read()
soup = BS(html,"lxml")
td = soup.find_all(class_='f')
list_to_print = []
for t in td:
    #print 'ceshi1',t.h3.a.get_text()
    fist_to_input = t.h3.a.get_text()
    #print 'type1=',type(fist_to_input)
    list_to_print.append(fist_to_input)
    #print t.h3.a['href']
    
    font_str = t.find_all('font',attrs={'size':'-1'})[0].get_text()
    start = 0 #后面需要更多页面可以在这里变更数据
    realtime = t.find_all('div',attrs={'class':'realtime'})
    if realtime:
        realtime_str = realtime[0].get_text()
        start = len(realtime_str)
    end = font_str.find('...')
    second_to_input = font_str[start:end]
    list_to_print.append(second_to_input)

c = [''.join(list_to_print)]
d = c[0].encode('utf-8').strip()

ans1_pipei = d.count(ans1)
ans2_pipei = d.count(ans2)
ans3_pipei = d.count(ans3)

print ans1_pipei
print ans2_pipei
print ans3_pipei
'''
if ans1_pipei+ans2_pipei+ans3_pipei == 0:
    correct_rate = 'error'#'no answer'
    ans1_pipei_rate = 0
    ans2_pipei_rate = 0
    ans3_pipei_rate = 0
else:
    ans1_pipei_rate = ans1_pipei/(ans1_pipei+ans2_pipei+ans3_pipei)
    ans2_pipei_rate = ans2_pipei/(ans1_pipei+ans2_pipei+ans3_pipei)
    ans3_pipei_rate = ans3_pipei/(ans1_pipei+ans2_pipei+ans3_pipei)
    #ans1_pipei_rate = str(ans1_pipei_rate*100)+'%'
    '''
#correct_rate = (str(ans1_pipei_rate*100)+'%'),(str(ans2_pipei_rate*100)+'%'),(str(ans3_pipei_rate*100)+'%')
#之前的导出结果是对三个答案给正确率百分比，然而实际应用时，从用户角度来说，直接给答案效果更好
if ans1_pipei == ans2_pipei and ans3_pipei == ans1_pipei:
    correct_rate = 'X'
elif ans1_pipei > ans2_pipei and ans1_pipei > ans3_pipei:
    correct_rate = 'A'
elif ans2_pipei > ans3_pipei and ans2_pipei > ans1_pipei:
    correct_rate = 'B'
elif ans3_pipei > ans2_pipei and ans3_pipei > ans1_pipei:
    correct_rate = 'C'
elif ans1_pipei == ans2_pipei and ans1_pipei > ans3_pipei:
    correct_rate = 'AB'
elif ans1_pipei == ans3_pipei and ans1_pipei > ans2_pipei:
    correct_rate = 'AC'
elif ans2_pipei == ans3_pipei and ans2_pipei > ans1_pipei:
    correct_rate = 'BC'


#将结果导出到系统剪贴板
setClipboardData(str(correct_rate))

#这个是调用了macro的程序，模拟鼠标点击，将结果输出到微信群，这里不防止maestro的配置，因为实在太简单
os.system("""osascript -e 'tell application "Keyboard Maestro Engine" to do script "微信点击、粘贴并enter"'""")

print correct_rate
print question,ans1,ans2,ans3
print ans1_pipei,ans2_pipei,ans3_pipei


d2 = datetime.datetime.now()
#计算结束时间
print 'windows_capture',(d3-d1).seconds,'seconds'
print 'baidu_scan_py',(d4-d3).seconds,'seconds'
print 'sum_time',(d2-d1).seconds,'seconds'


