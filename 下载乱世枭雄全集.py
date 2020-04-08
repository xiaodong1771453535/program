#coding=utf-8
import requests
from lxml import etree
import urllib
from bs4 import BeautifulSoup
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 请求的首部信息
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
co = 0
for i in range(17):
    print(i);
    
    url ='https://www.ximalaya.com/xiangsheng/3820/'
    if(i > 0):
        url = url + 'p'+str(i+1)+'/'
    
    html = requests.get(url, headers=headers)

    # BeautifulSoup对象接收html文档字符串
    # lxml是html解析器
    soup = BeautifulSoup(html.text, 'lxml')

    # 找出class属性值为news-list的div
    news_list = soup.find('div', {'class': 'sound-list _Qp'})

    # 找出news_list下的所有li标签
    news = news_list.find_all('li',{'class':'_Vc'})
    
    for t in news:
        co=co+1
        title = t.find('div',{'class':'text _Vc'}) #得到A把标签的里面囊括的内容
        nameStr = title.find('a')['title']
        herfStr = title.find('a')['href']
        hf = herfStr.split('/')[3].strip()
        #print(nameStr+" : "+ hf)
        
        herfUrl = 'https://www.ximalaya.com/revision/play/v1/audio?id='+hf+'&ptype=1'
        src = requests.get(herfUrl, headers=headers)
        jd = json.loads(src.text) 
        jd = jd['data']
        imgUrl = jd['src']
        path = 'D://luanshi//'
        #print('src: '+imgUrl)
        try:
            urllib.request.urlretrieve(imgUrl,path+str(co)+nameStr+'.m4a')    #保存图片 下载图片
        except:
            print(nameStr +' error--------------------')
        print(str(co)+'-')