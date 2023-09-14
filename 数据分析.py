import jieba
import wordcloud
import re
import requests
import imageio

#读取弹幕数据
f = open('前20弹幕.txt', encoding='utf-8')
text = f.read()
#分词，分割词汇
text_list = jieba.lcut(text)
print(text_list)
#列表变成字符串
text_str = ' '.join(text_list)
print(text_str)
#词云图配置
wc = wordcloud.WordCloud(
    width=500,
    height=500,
    background_color='white',
    font_path='msyh.ttc'
)
wc.generate(text_str)
wc.to_file('词云.png')



