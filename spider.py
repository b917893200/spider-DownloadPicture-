import requests
import re
import os
import random
import queue
import time

q = queue.Queue()

Host = input("请输入网站域名\n")
response =  requests.get(Host)
response.encoding = "utf-8"
#


# href="https://www.ilemiss.net/japan/"
#提取所有html放到队列中
pattern = "https:.*?.html|http:.*?.html|https:.*?.net|http:.*?.net"
re.compile(pattern)
urll = re.findall(pattern,response.text)
#列表去重
urll=list(set(urll))
#print(urll) #测试

for Url1 in urll: #html的url
    q.put(Url1)
if (os.path.exists("E:\\python_spider")):
    pass
else:
    os.makedirs("E:\\python_spider")

i=0
#print(q.qsize())  测试
pattern = "http:.*?.jpg"
re.compile(pattern)
while(not q.empty()):
        print(q.qsize())
        Url2 = q.get() #弹出一个html的url
        response = requests.get(Url2)#获取网页源代码
        Url_jpg = re.findall(pattern,response.text)#返回一个列表
        for Url3 in Url_jpg:
             i = i+1
             path = "E:\python_spider/"+str(i)+".jpg"
             with open(path,"wb") as f:
                response = requests.get(Url3)
                f.write(response.content)
                #time.sleep(5) 测试用
                print("执行一次完毕")
        Url2 = q.get()
