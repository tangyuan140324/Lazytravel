#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/15 11:13
# @Author : HyDady
# @Site : 
# @File : travel_main.py
# @Software: PyCharm
import json
import time
from about_gaode import gaode_main
from about_hotel import main_hotel, get_json_info
from ctrip_xiecheng import get_sightAndjourneysUrl, summary_sights, get_journeysDetailUrl, summary_journeys
from plane_XieCheng import get_plane_num, get_query_planeurl, query_plane_info
from train_12306 import getStation, get_query_url, query_train_info

if __name__ == '__main__':
    json_1 = {"depart_date": "2018-10-20", "back_date": "2018-10-21", "origin_city": "郑州",
              "destination_city": "长春", "trip_mode": "train"}

    depart_date = json_1['depart_date']
    origin_city = json_1['origin_city']
    destination_city = json_1['destination_city']
    trip_mode = json_1['trip_mode']
    time.sleep(0.5)
    if trip_mode == "train":
        with open('code_train.txt', 'r', encoding='UTF-8') as j:
            text1 = j.read()  # .encode('utf-8')
        text = json.loads(text1)
        with open('train_KVchage.txt', 'r', encoding='UTF-8') as u:
            infod = u.read()
        com_table = json.loads(infod)
        url = get_query_url(text, depart_date, origin_city, destination_city)
        train_info = query_train_info(depart_date, url, com_table, origin_city, destination_city)
        print('--------------------train_info-------------------------')
        if isinstance(train_info,str):
            print('\033[1;31m' + train_info + '\033[0m')
        else:
            print(train_info)
        # i = 0
        # while True:
        #     if lis == ' 输出信息有误，请重新输入' and i < 6:
        #         lis = query_train_info(depart_date, url, com_table, origin_city, destination_city)
        #         i+=1
        #     else:
        #         train_info = lis
        #         print('--------------------train_info-------------------------')
        #         print(train_info)
        #         break
    if  trip_mode == "plane":
        with open('plane_code.txt', 'r', encoding='UTF-8') as l:
            text = l.read()
        text1 = json.loads(text)
        url = get_query_planeurl(text1, depart_date, origin_city, destination_city)
        plane_info = query_plane_info(url)
        print('--------------------plane_info-------------------------')
        print(plane_info)
    keyword  = destination_city
    basic_url = 'http://you.ctrip.com'
    sight_url, journeys_url = get_sightAndjourneysUrl(keyword)
    find_sight_info = []
    for i in range(1, 3):
        url_page = sight_url.split('.html')[0]+'/s0-p{}.html'.format(str(i))
        sightsList = summary_sights(url_page)
        find_sight_info.append(sightsList)
    print('--------------------find_sight_info-------------------------')
    print(find_sight_info)
    every_urls = get_journeysDetailUrl(journeys_url)
    find_journeys_info = []
    for every_url_part in every_urls:
        every_url = basic_url + every_url_part
        tem = summary_journeys(every_url)
        find_journeys_info.append(tem)
    print('--------------------find_journeys_info-------------------------')
    print(find_journeys_info)


    json_2_info,regiony_comparison_table = get_json_info(destination_city)
    print('--------------------json_2_info-------------------------')
    print(json_2_info)
    json_2 = {'zone':'动植物公园',"location":"XX区","sl":"XX火车站","metro":"XX线"}
    zone = json_2['zone']
    hotel_info = main_hotel(destination_city, zone)
    print('--------------------hotel_info-------------------------')
    print(hotel_info)
    print('--------------------taxi or bus info-------------------------')
    destination_city = '长春'
    or_address = '龙嘉国际机场'
    de_address = '长春华丽达大酒店'
    bus_info = gaode_main(or_address, de_address, destination_city)
    print('--------------------bus_info-------------------------')
    print(bus_info)

    pass