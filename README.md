# 冲顶大会百万赢家百万英雄KK直播芝士超人答题助手（平均用时 3秒）
## 核心思路
1.利用quicktime，将iphone同步显示到mac，放在屏幕左上角（0.5秒之内）  
2.利用百度云文字识别接口，将题目答案保存编辑到字典（利用正则化把部分无用关键词给剔除，可以提升问题答案识别精准率和识别速度）（1秒之内）  
3.调取爬虫，爬取百度搜索第一页结果  
4.将第二步识别的答案在第三步所有文字内容进行匹配，重复率最高的为推荐答案（1.5秒）（答案会给出ABC中的一个，如果其中有两个概率相同，会同时推荐，如AB AC BC，再碰到没法计算的问题时，给X）  
5.利用keyboard maestro，将结果粘贴复制到微信群窗口（这一步用python也可以完成，懒得写代码了，所以直接调取接口录了个程序开跑了）  

## 使用说明
1.quicktime同步iphone的界面放在桌面左边，延边摆放  
2.微信窗口放在桌面右上角  
3.ai_master.py  是主算法，直接跑即可，里面涉及到题目文字正则化、百度爬虫、答案推荐等核心步骤  
4.baidu_scan.py 代用百度云文字识别接口，对图片进行文字转化  
5.get_pic.py 对同步窗口的图片进行截图，不同的平台有不同的截图参数  
6.screen_cap.py 这个没什么用，为了方便分析一些题目做的快速截屏代码，可弃

## 待改进之处及解决思路
1.微信群用户如果本身网络不好，会有1-2秒收信息延迟现象，建议开桌面端看答案  
2.根据核心的查答案的逻辑，在碰到带有否定词的问题时，（如：以下选项不是……）就容易出现正确率颠倒的情况，其实很容易理解原因，当然，我们可以设置条件，一旦有关键词，推荐答案反着来即可  
3.答案太长时准确率为0，因为我用的是精准匹配，所以，有时候实际上部分关键词切中了，但因为没有完全匹配，答案会给X，这个问题可以通过模糊匹配算法或者结巴切词溢出关键字再进行匹配也可以提高准确率  
4.在线学习机制，我研究过不同平台的题目，很多题目其实是重复出的，甚至不同平台都有重合的，所以，理论上把这些问题和答案导入到本地字典不仅可以减少爬虫时间（预估1秒），还可以提高准确率，不过这个要提前爬取不同公众号和网页的数据，并且还要建立数据库，所以我就没折腾了  
5.完整的操作基于mac平台，windows平台，一方面是编码格式比较头疼，还有模拟器的延时比较严重，而且还有几个平台不支持模拟器登录  

## 其他说明
1.这个程序从开始开发到微信群组群落地，时间是10个小时，时间是2018年1月10日 11:00 开始有想法然后半夜就落地了，不过热点问题，大家跟进都很快，特别是搜狗也乘机做了波广告，流量稀释，这东西只能算是小打小闹朋友们娱乐了  
2.从答案精准率角度来说，一般12个题目能够对8题已经不错，要有更高精准率，就得有更多的题目设计思路，而且花很多时间可能就提高1题精准率，不是不能做，性价比不高，淘宝要上线这东西也很快，不过用户在你没答对12题的时候，永远是不满意的，所以也没啥意思  
3.微信群采用裂变群二维码，速度会非常更快，如果想要收费，在有较大用户数量基础条件下，也可以有一笔收入（不过再怎么做，收入也就那一些，所以这个算法就给朋友们拿来玩儿了）  
4.代码仅供娱乐，到1月14日已经停止更新，这两天抽空开源，也是希望有其他有意思的项目或者竞赛，能和更多人一起交流

欢迎邮件沟通 ai@landering.com

