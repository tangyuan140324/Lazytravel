#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/15 11:13
# @Author : HyDady
# @Site : 
# @File : travel_main.py
# @Software: PyCharm
import json

from about_gaode import gaode_main
from about_hotel import main_hotel, get_json_info
from plane_XieCheng import get_plane_num, get_query_planeurl, query_plane_info
from train_12306 import getStation, get_query_url, query_train_info

if __name__ == '__main__':
    json_1 = {"depart_date": "2018-10-18", "back_date": "2018-10-21", "origin_city": "南京",
              "destination_city": "重庆", "trip_mode": "train"}

    depart_date = json_1['depart_date']
    origin_city = json_1['origin_city']
    destination_city = json_1['destination_city']
    trip_mode = json_1['trip_mode']
    if trip_mode == "train":
        with open('code_train.txt', 'r') as j:
            text = j.read()
        url = get_query_url(text, depart_date, origin_city, destination_city)
        lis = query_train_info(url, text, origin_city, destination_city)
        i = 0
        while True:
            if lis == ' 输出信息有误，请重新输入' and i < 6:
                lis = query_train_info(url, text, origin_city, destination_city)
                i+=1
            else:
                train_info = lis
                print('--------------------train_info-------------------------')
                print(train_info)
                break
    if  trip_mode == "plane":
        with open('plane_code.txt', 'r') as l:
            text = l.read()
        text1 = json.loads(text)
        url = get_query_planeurl(text1, depart_date, origin_city, destination_city)
        plane_info = query_plane_info(url)
        print('--------------------plane_info-------------------------')
        print(plane_info)

    json_2_info,regiony_comparison_table = get_json_info(destination_city)
    print('--------------------json_2_info-------------------------')
    print(json_2_info)

    json_2 = {'zone':'观音桥/九街',"location":"XX区","sl":"XX火车站","metro":"XX线"}
    zone = json_2['zone']
    hotel_info = main_hotel(destination_city, zone)
    print('--------------------hotel_info-------------------------')
    print(hotel_info)
    print('--------------------taxi or bus info-------------------------')
    destination_city = '三亚'
    or_address = '三亚凤凰机场'
    de_address = '三亚四季海庭酒店'
    bus_info = gaode_main(or_address, de_address, destination_city)
    print('--------------------bus_info-------------------------')
    print(bus_info)

    pass