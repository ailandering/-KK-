#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: ai
#mail:ai@landering.com
from aip import AipOcr
#百度文字识别密钥，自己填吧
APP_ID = ''
API_KEY = '' 
SECRET_KEY = ''
#百度官方代码
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
options = {
	'detect_direction': 'true',
	'language_type': 'CHN_ENG',
}

def baidu_scan_py():
	result = aipOcr.basicGeneral(get_file_content('general.png'), options)
	words_result =result['words_result']

	scan_txt_list = []
	for i in range (len(words_result)):
		words_result_temp = words_result[i]['words']
		scan_txt_list.append(words_result_temp)
		#print words_result_temp 


	#这里把第一个字符给删除掉了
	scan_txt_list[0] = scan_txt_list[0][1:-1]  
	scan_txt_list_final = [] 
	#print len(scan_txt_list)

	#题目识别板块，一般情况下题目是2行，答案是3行，总共5行，有时候题目太长，或者只有1行，也得识别准确
	#从而方便把题目和答案放在分属的字典中
	if len(scan_txt_list) == 5:
		print 'len(scan_txt_list) = 5'
		question = scan_txt_list[0] + scan_txt_list[1]
		ans1 = scan_txt_list[2]
		ans2 = scan_txt_list[3]
		ans3 = scan_txt_list[4]
	elif len(scan_txt_list) == 6:
		print 'len(scan_txt_list) = 6'
		question = scan_txt_list[0] + scan_txt_list[1] + scan_txt_list[2]
		ans1 = scan_txt_list[3]
		ans2 = scan_txt_list[4]
		ans3 = scan_txt_list[5]		
	elif len(scan_txt_list) == 4:
		print 'len(scan_txt_list) = 4'
		question,ans1,ans2,ans3 = scan_txt_list[0],scan_txt_list[1],scan_txt_list[2],scan_txt_list[3]
	else:
		print 'too many words'

	#print question.encode('utf')
	#print ans1,ans2,ans3
	return question,ans1,ans2,ans3
