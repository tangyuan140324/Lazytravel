#-*- coding:utf-8 -*-
# Author : 7secondsFish
# Data : 18-10-9 下午2:29

import re
import requests
import json
import time


def get_plane_num():
    url = 'https://flights.ctrip.com/itinerary/api/poi/get'
    res = requests.get(url)
    text = res.json()['data']
    str1 = json.dumps(text, ensure_ascii=False)
    pattern = u'\|(.*?)\|([0-9]+)\|'
    result = re.findall(pattern, str1)
    li = [x[0] for x in result]
    lix = []
    for item in li:
        city_name = item.split('(')[0]
        city_number = re.findall(r'\(([A-Z]+)\)',item)
        lix.append((city_name,''.join(city_number)))
    station = dict(lix)
    return station

def get_query_planeurl(text,depart_date,origin_city,destination_city):
    # 城市名代码查询字典
    # key：城市名 value：城市代码
    try:
        date = depart_date
        from_station_name = origin_city
        to_station_name = destination_city
        from_station = text[from_station_name]
        to_station = text[to_station_name]
    except:
        date, from_station, to_station = '--', '--', '--'
        # 将城市名转换为城市代码

    # api url 构造
    #url = 'https://flights.ctrip.com/itinerary/oneway/{}-{}?date={}'.format(from_station,to_station,date)
    url = 'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?'\
                  + 'DCity1='+ from_station + '&ACity1=' + to_station +'&SearchType=S' + '&DDate1=' + date
        #print(url)

    return url

def query_plane_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
        'Host': 'flights.ctrip.com', 'Referer': 'http://flights.ctrip.com/booking/TAO-SJW-day-1.html?DDate1={}'.format(time.strftime("%Y-%m-%d", time.localtime()))}
    res = requests.get(url,headers=headers)
    return_json = res.json()
    flight_list = return_json['fis']
    flight_nums = len(flight_list)
    lix = []
    als = return_json['als']
    for i in range(flight_nums):
        tmp = {}
        airline = flight_list[i]['alc']
        tmp['airline'] = als[airline]
        flight_no = flight_list[i]['fn']
        tmp['flight_no'] = flight_no
        begin_time = flight_list[i]['dt']
        tmp['begin_time'] = begin_time
        arrive_time = flight_list[i]['at']
        tmp['arrive_time'] = arrive_time
        dpbn = flight_list[i]['dpbn']
        tmp['dpbn'] = dpbn
        apbn = flight_list[i]['apbn']
        tmp['apbn'] = apbn
        price_list = [each['p'] for each in flight_list[i]['scs'] if each['hotel'] is None]
        tmp['price_list'] = price_list
        lix.append(tmp)
    #print(lix)
    return lix


if __name__ == '__main__':
    origin_city = '北京'
    destination_city = '三亚'
    depart_date = '2018-10-18'
    with open('plane_code.txt', 'r') as l:
        text = l.read()
    text1 = json.loads(text)
    url = get_query_planeurl(text1, depart_date, origin_city, destination_city)
    plane_info = query_plane_info(url)
    print(plane_info)
    pass
