#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/11 15:20
# @Author : HyDady
# @Site : 
# @File : about_hotel.py
# @Software: PyCharm
import re
import requests
import json
from bs4 import BeautifulSoup

with open('pingyin_city.txt', 'r', encoding='UTF-8') as f:
    data_pingyi = f.read()  # .encode('utf-8')
dict_new = json.loads(data_pingyi)
with open('number_city.txt', 'r', encoding='UTF-8') as g:
    data_number = g.read()  # .encode('utf-8')
city_comparison_table = json.loads(data_number)

# def get_city_id():
#     url = "http://hotels.ctrip.com/Domestic/Tool/AjaxGetCitySuggestion.aspx"
#     headers = {
#         'host': "hotels.ctrip.com",
#         'connection': "keep-alive",
#         'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
#         'accept': "*/*",
#         'referer': "http://hotels.ctrip.com/",
#         'accept-encoding': "gzip, deflate",
#         'accept-language': "zh-CN,zh;q=0.9",
#         #'cookie': "Union=SID=155952&AllianceID=4897&OUID=baidu81|index|||; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _abtest_userid=bb253239-c268-4792-b2f9-b6370562d7b0; gad_city=b82f0154257a2ce862c5ae5da9f81b79; traceExt=campaign=CHNbaidu81&adid=index; _gat=1; ASP.NET_SessionSvc=MTAuMjguMTEyLjE1NHw5MDkwfGppbnFpYW98ZGVmYXVsdHwxNTM3NDk5NzE1NjQy; IntHotelCityID=splitsplitsplit2018-10-13split2018-10-14splitsplitsplit0splitsplit; __utmt=1; __utma=13090024.1562554692.1539309419.1539309424.1539309424.1; __utmb=13090024.2.10.1539309424; __utmc=13090024; __utmz=13090024.1539309424.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _RF1=49.77.226.81; _RSG=SlKIJMnzFlDtiXmtcQOEc8; _RDG=28b48f42c0678c21f919f2811eae25d510; _RGUID=dbcff715-9349-4bdc-898e-61a9b7c21b37; _ga=GA1.2.1562554692.1539309419; _gid=GA1.2.1420859181.1539309419; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1539309428441%7D%5D; __zpspc=9.1.1539309419.1539309428.3%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _jzqco=%7C%7C%7C%7C1539309419509%7C1.252987513.1539309419399.1539309422791.1539309428459.1539309422791.1539309428459.0.0.0.3.3; _bfi=p1%3D102001%26p2%3D0%26v1%3D4%26v2%3D0; MKT_Pagesource=PC; appFloatCnt=1; manualclose=1; _bfa=1.1539309416714.1eh6l2.1.1539309416714.1539309416714.1.5; _bfs=1.5",
#         'cache-control': "no-cache"
#         }
#     response = requests.request("GET", url, headers=headers)
#     #print(response.text)
#     return response.text

def get_region_id(cityNumber):
    url = "http://hotels.ctrip.com/Domestic/Tool/AjaxGetHotKeyword.aspx"

    querystring = {"cityid": cityNumber}

    headers = {
        'host': "hotels.ctrip.com",
        'connection': "keep-alive",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        'accept': "*/*",
        'referer': "http://hotels.ctrip.com/",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9",
        #'cookie': "Union=SID=155952&AllianceID=4897&OUID=baidu81|index|||; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _abtest_userid=bb253239-c268-4792-b2f9-b6370562d7b0; gad_city=b82f0154257a2ce862c5ae5da9f81b79; traceExt=campaign=CHNbaidu81&adid=index; _gat=1; ASP.NET_SessionSvc=MTAuMjguMTEyLjE1NHw5MDkwfGppbnFpYW98ZGVmYXVsdHwxNTM3NDk5NzE1NjQy; IntHotelCityID=splitsplitsplit2018-10-13split2018-10-14splitsplitsplit0splitsplit; __utmt=1; __utma=13090024.1562554692.1539309419.1539309424.1539309424.1; __utmb=13090024.2.10.1539309424; __utmc=13090024; __utmz=13090024.1539309424.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _RF1=49.77.226.81; _RSG=SlKIJMnzFlDtiXmtcQOEc8; _RDG=28b48f42c0678c21f919f2811eae25d510; _RGUID=dbcff715-9349-4bdc-898e-61a9b7c21b37; _ga=GA1.2.1562554692.1539309419; _gid=GA1.2.1420859181.1539309419; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1539309428441%7D%5D; __zpspc=9.1.1539309419.1539309428.3%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _jzqco=%7C%7C%7C%7C1539309419509%7C1.252987513.1539309419399.1539309422791.1539309428459.1539309422791.1539309428459.0.0.0.3.3; _bfi=p1%3D102001%26p2%3D0%26v1%3D4%26v2%3D0; MKT_Pagesource=PC; appFloatCnt=1; manualclose=1; _bfa=1.1539309416714.1eh6l2.1.1539309416714.1539309416714.1.5; _bfs=1.5",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text

def join_hotel_url(cityId,locationInfo):
    url = 'http://hotels.ctrip.com/hotel/{}/{}'.format(cityId,locationInfo)
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    hotels_info = soup.find('div',id='hotel_list')
    name_infos = hotels_info.findAll('h2',class_='hotel_name')
    prices = soup.findAll('span',class_='J_price_lowList')
    hotel_priceList = []
    for i in prices:
        hotel_priceList.append(i.getText())
    hotel_nameList = []
    for item in name_infos:
        hotel_name = re.findall(r'title="(.*?)" tracekey',str(item))[0]
        hotel_nameList.append(hotel_name)
    if len(hotel_nameList) == len(hotel_priceList):
        hotel_result = dict(zip(hotel_nameList, hotel_priceList))
        return hotel_result
    else:
        return "The length of hotel_nameList is not equal to hotel_priceList."

def get_json_info(city):
    '''
    获取城市信息编号。
    '''

    '''
        获取行政区域、热门商圈等信息编号。
        '''
    cityNumber = city_comparison_table[city]
    # print('------------------------cityNumber---------------------')
    # print(cityNumber)
    data = get_region_id(cityNumber)
    info = data.split('.jsonpResponse.suggestion=')[1]
    # print(info)
    # print(type(info))
    json_data = eval(info)
    part_one = json_data['zoneId']['data']
    json_info = []
    lix = []
    for item in part_one:
        lix.append((item['name'], 'zone' + item['id']))
        json_info.append(('zone', item['name']))
    part_two = json_data['locationId']['data']
    for item in part_two:
        lix.append((item['name'], "location" + item['id']))
        json_info.append(('location', item['name']))
    part_three = json_data['sl']['data']
    for item in part_three:
        lix.append((item['name'], "sl" + item['id']))
        json_info.append(('sl', item['name']))
    try:
        part_four = json_data['metroId']['data']
        for item in part_four:
            lix.append((item['name'], "metro" + item['id']))
            json_info.append(('metro', item['name']))
    except KeyError:
        lix.append(('metro', "NO METOR INFOMATION !"))
        print("NO METOR INFOMATION !")
    regiony_comparison_table = dict(lix)
    return regiony_comparison_table ,json_info

def main_hotel(city,zone = '',location = '',sl = '',metro = ''):
    city = city#'三亚'
    zone = zone#'大东海'
    location = location#''
    sl = sl
    metro = metro
    # r = get_city_id()
    # pingy = re.findall(r'data:"(.*?)\|([\u4e00-\u9fa5]+)\|', r)
    # pingy_table = dict(pingy)
    # dict_new = {value: key for key, value in pingy_table.items()}
    # pattern = u'([\u4e00-\u9fa5]+)\|([0-9]+)'
    # result = re.findall(pattern, r)
    # city_comparison_table = dict(result)
    regiony_comparison_table,json_info = get_json_info(city)
    '''
    拼接最后详细酒店信息的url。
    '''

    cityId = dict_new[city] + str(city_comparison_table[city])
    locationInfo = []
    if zone != '':
        locationInfozone = regiony_comparison_table[zone]
        locationInfo.append(locationInfozone)
    if sl != '':
        locationInfosl = regiony_comparison_table[sl]
        locationInfo.append(locationInfosl)
    if location != '':
        locationInfolocation = regiony_comparison_table[location]
        locationInfo.append(locationInfolocation)
    if metro != '':
        if regiony_comparison_table[metro] != 'NO METOR INFOMATION !':
            locationInfometro = regiony_comparison_table[location]
            locationInfo.append(locationInfometro)
    locationInfoStr = ''.join(locationInfo)
    hotel_result = join_hotel_url(cityId, locationInfoStr)
    return hotel_result

if __name__=='__main__':
    city = '三亚'
    zone = '大东海'
    location = ''
    sl = ''
    metro = ''

    hotel_result = main_hotel(city,zone)
    print(hotel_result)


    pass