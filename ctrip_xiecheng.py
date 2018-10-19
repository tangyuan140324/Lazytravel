#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/18 10:29
# @Author : HyDady
# @Site : 
# @File : ctrip_xiecheng.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import re



def get_sightAndjourneysUrl(keyword):
    qure_city_url = 'http://m.ctrip.com/restapi/h5api/searchapp/search?action=autocomplete&source=globalonline&keyword={}'.format(keyword)
    res = requests.get(qure_city_url).json()
    city_url = res['data'][0]['url']
    headers = {
        'Host': "you.ctrip.com",
        'Connection': "keep-alive",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://www.ctrip.com/?utm_source=baidu&utm_medium=cpc&utm_campaign=baidu81&campaign=CHNbaidu81&adid=index&gclid=&isctrip=T",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        #'Cookie': "Union=SID=155952&AllianceID=4897&OUID=baidu81|index|||; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _abtest_userid=b6b741b5-a565-4a09-b771-51665afce3cb; _bfa=1.1539827719883.hu3lm.1.1539827719883.1539827719883.1.1; _bfs=1.1; gad_city=b82f0154257a2ce862c5ae5da9f81b79; _RF1=49.77.226.81; _RSG=ocKyNkFq9bEXO8zxiD_4mB; _RDG=288609652e633423972c781c6c22134806; _RGUID=e949d0fb-97f1-49b2-bc04-fcdb3bf48621; _ga=GA1.2.1315960574.1539827723; _gid=GA1.2.836371662.1539827723; _gat=1; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1539827722759%7D%5D; traceExt=campaign=CHNbaidu81&adid=index; __zpspc=9.1.1539827722.1539827722.1%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _jzqco=%7C%7C%7C%7C1539827722829%7C1.1559878609.1539827722778.1539827722778.1539827722778.1539827722778.1539827722778.0.0.0.1.1; _bfi=p1%3D100101991%26p2%3D0%26v1%3D1%26v2%3D0; MKT_Pagesource=PC",
        'cache-control': "no-cache"
        }
    response = requests.request("GET", city_url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html,'lxml')
    url_info = soup.find('div',class_='innerbox')
    urls = url_info.findAll('li')
    url_list = []
    for i in urls:
        url_list.append(i.a['href'])
    basic_url = 'http://you.ctrip.com'
    sight_url = basic_url + url_list[3]
    journeys_url = basic_url + url_list[-3]
    return sight_url,journeys_url

def summary_sights(sight_url):
    url = sight_url
    headers = {
        'Host': "you.ctrip.com",
        'Connection': "keep-alive",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://you.ctrip.com/place/61.html",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    infos = soup.find_all('div',class_='list_mod2')
    sightsList = []
    for item in infos:
        tem = {}
        tem['sight_name'] = item.find('div',class_='rdetailbox').dl.dt.a.getText()
        tem['sight_location'] = item.find('dd', class_='ellipsis').getText().replace('\r','').replace('\n','').replace('  ','')
        data = item.findAll('dd')[1].getText().replace('\r','').replace('\n','').replace('  ','')
        pattern = u'A{1,5}级景区'
        try:
            tem['sight_grade'] = re.findall(pattern,data)[0]
        except IndexError:
            tem['sight_grade'] = 'zero grade'
        try:
            tem['sight_price'] = item.find('span',class_='price').getText()
        except AttributeError:
            tem['sight_price'] = 'No price'
        tem['sight_score'] = item.find('a',class_='score').getText().replace('\xa0分','')
        tem['sight_review'] = item.findAll('li')[2].a.getText().replace('\r','').replace('\n','').replace('  ','')
        sightsList.append(tem)
    return sightsList

def get_journeysDetailUrl(journeys_url):
    url = journeys_url
    headers = {
        'Host': "you.ctrip.com",
        'Connection': "keep-alive",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://you.ctrip.com/sight/sanya61.html",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        #'Cookie': "Union=SID=155952&AllianceID=4897&OUID=baidu81|index|||; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _abtest_userid=b6b741b5-a565-4a09-b771-51665afce3cb; gad_city=b82f0154257a2ce862c5ae5da9f81b79; ASP.NET_SessionSvc=MTAuOC4xODkuNjZ8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTUzNzQzMjQ5NzMxOQ; bdshare_firstime=1539827728974; appFloatCnt=2; manualclose=1; traceExt=campaign=CHNbaidu81&adid=index; Customer=HAL=ctrip_uk; _ctm_t=ctrip; _bfa=1.1539827719883.hu3lm.1.1539827719883.1539842195722.2.45; _bfs=1.2; _RF1=49.77.226.81; _RSG=ocKyNkFq9bEXO8zxiD_4mB; _RDG=288609652e633423972c781c6c22134806; _RGUID=e949d0fb-97f1-49b2-bc04-fcdb3bf48621; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1539842204954%7D%5D; _ga=GA1.2.1315960574.1539827723; _gid=GA1.2.836371662.1539827723; __zpspc=9.5.1539842198.1539842204.2%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _jzqco=%7C%7C%7C%7C1539827722829%7C1.1559878609.1539827722778.1539842198016.1539842204989.1539842198016.1539842204989.undefined.0.0.32.32; MKT_Pagesource=PC; _bfi=p1%3D290546%26p2%3D290555%26v1%3D45%26v2%3D44",
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    infos = soup.findAll('div',class_='journeys_v2box cf')
    journeysUrlLsit = []
    for item in infos:
        journeysUrlLsit.append(item.a['href'])
    return journeysUrlLsit

def summary_journeys(every_url):
    url = every_url
    headers = {
        'Host': "you.ctrip.com",
        'Connection': "keep-alive",
        'Cache-Control': "max-age=0",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://you.ctrip.com/journeys/sanya61.html",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        #'Cookie': "Union=SID=155952&AllianceID=4897&OUID=baidu81|index|||; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _abtest_userid=b6b741b5-a565-4a09-b771-51665afce3cb; gad_city=b82f0154257a2ce862c5ae5da9f81b79; ASP.NET_SessionSvc=MTAuOC4xODkuNjZ8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTUzNzQzMjQ5NzMxOQ; bdshare_firstime=1539827728974; appFloatCnt=2; manualclose=1; traceExt=campaign=CHNbaidu81&adid=index; Customer=HAL=ctrip_uk; _ctm_t=ctrip; _bfa=1.1539827719883.hu3lm.1.1539827719883.1539842195722.2.47; _bfs=1.4; _ga=GA1.2.1315960574.1539827723; _gid=GA1.2.836371662.1539827723; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1539842693809%7D%5D; __zpspc=9.5.1539842198.1539842693.4%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _jzqco=%7C%7C%7C%7C1539827722829%7C1.1559878609.1539827722778.1539842349753.1539842693864.1539842349753.1539842693864.undefined.0.0.34.34; _RF1=49.77.226.81; _RSG=ocKyNkFq9bEXO8zxiD_4mB; _RDG=288609652e633423972c781c6c22134806; _RGUID=e949d0fb-97f1-49b2-bc04-fcdb3bf48621; MKT_Pagesource=PC; _bfi=p1%3D290595%26p2%3D290555%26v1%3D47%26v2%3D46",
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    tem = {}
    data = soup.find('div',class_='jv2_info').findAll('li')
    tem['days'] = data[0].findAll('span')[0].getText()
    tem['places'] = data[0].findAll('span')[1].getText()
    tricps = soup.findAll('div',class_='singleday')
    li = []
    for tricp in tricps:
        tn = {}
        infomations = tricp.find('div',class_='poiwrap cf').dl
        # print('-----------------infomations-----------------')
        # print(infomations)
        try:
            tn['location'] = infomations.dt.a.getText()
        except AttributeError:
            tn['location'] = 'No found location infomation'
        try:
            tn['grade'] = infomations.dd.a.getText()
        except AttributeError:
            tn['grade'] = 'No found grade infomation'
        try:
            tn['review'] = infomations.dd.findAll('a')[1].getText()
        except AttributeError:
            tn['review'] = 'No found review infomation'
        try:
            tn['labeltext'] = infomations.find('dd',class_='ddcomment').getText()
        except AttributeError:
            tn['labeltext'] = 'No found labeltext infomation'
        try:
            tn['time'] = infomations.findAll('dd')[2].getText()
        except IndexError:
            tn['time'] = 'No found time infomation'
        try:
            tn['open_time'] = infomations.findAll('dd')[3].getText()
        except IndexError:
            tn['open_time'] = 'No found open_time infomation'
        try:
            variableinfo = infomations.findAll('dd')[4].getText()
            tn['price'] = re.findall(r'￥([0-9]+)', variableinfo)[0]
        except IndexError:
            tn['price'] = 'No price'
        li.append(tn)
    tem['tricps'] = li
    return tem


if __name__=='__main__':
    keyword  = '南京'
    basic_url = 'http://you.ctrip.com'
    sight_url, journeys_url = get_sightAndjourneysUrl(keyword)
    for i in range(1, 3):
        url_page = sight_url.split('.html')[0]+'/s0-p{}.html'.format(str(i))
        sightsList = summary_sights(url_page)
        print(sightsList)
    every_urls = get_journeysDetailUrl(journeys_url)
    for every_url_part in every_urls:
        every_url = basic_url + every_url_part
        tem = summary_journeys(every_url)
        print(tem)
    pass