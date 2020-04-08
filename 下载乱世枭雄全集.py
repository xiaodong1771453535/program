#coding=utf-8
import requests
from lxml import etree
import urllib
from bs4 import BeautifulSoup
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# ������ײ���Ϣ
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

    # BeautifulSoup�������html�ĵ��ַ���
    # lxml��html������
    soup = BeautifulSoup(html.text, 'lxml')

    # �ҳ�class����ֵΪnews-list��div
    news_list = soup.find('div', {'class': 'sound-list _Qp'})

    # �ҳ�news_list�µ�����li��ǩ
    news = news_list.find_all('li',{'class':'_Vc'})
    
    for t in news:
        co=co+1
        title = t.find('div',{'class':'text _Vc'}) #�õ�A�ѱ�ǩ����������������
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
            urllib.request.urlretrieve(imgUrl,path+str(co)+nameStr+'.m4a')    #����ͼƬ ����ͼƬ
        except:
            print(nameStr +' error--------------------')
        print(str(co)+'-')