import requests#数据请求模块
import re#正则表达式模块

#发送请求
url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=1169811085'#修改该网址爬取弹幕
#headers 请求头 把Python代码进行伪装，模拟出浏览器去发送请求
#user-agent 浏览器基本身份标识
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
#通过requsets模块里面get请求方法，对url地址发送请求，并且携带headers请求头，最后用response变量去接收返回数据
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding

#获取数据并将数据存放在弹幕.txt中
#（）精确匹配，表示想要的数据  泛匹配.*？
data_list = re.findall('<d p=".*?">(.*?)</d>',response.text)
for index in data_list:
    #mode 保存方式 encoding 编码
    with open('弹幕.txt', mode='a', encoding='utf-8') as f:
        f.write(index)
        f.write('\n')
        print(index)
