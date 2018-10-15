#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/15 11:13
# @Author : HyDady
# @Site : 
# @File : travel_main.py
# @Software: PyCharm
from about_baidu import gaode_main
from about_hotel import main_hotel
from plane_XieCheng import get_plane_num, get_query_planeurl, query_plane_info
from train_12306 import getStation, get_query_url, query_train_info

if __name__ == '__main__':
    json_1 = {"depart_date": "2018-10-15", "back_date": "2018-10-1", "origin_city": "南京",
              "destination_city": "重庆", "trip_mode": "train"}

    depart_date = json_1['depart_date']
    origin_city = json_1['origin_city']
    destination_city = json_1['destination_city']

    if "trip_mode" == "train":
        text = getStation()
        url = get_query_url(text, depart_date, origin_city, destination_city)
        lis = query_train_info(url, text, origin_city, destination_city)
        while True:
            if lis == ' 输出信息有误，请重新输入':
                lis = query_train_info(url, text, origin_city, destination_city)
            else:
                train_info = lis
                break
    if  "trip_mode" == "plane":
        text = get_plane_num()
        url = get_query_planeurl(text, depart_date, origin_city, destination_city)
        plane_info = query_plane_info(url)

    json_2 = {'zone':'XX景区',"location":"XX区","sl":"XX火车站","metro":"XX线"}
    zone = 'XX景区'
    or_address = '三亚凤凰机场'
    de_address = '三亚四季海庭酒店'
    hotel_info = main_hotel(origin_city, zone)
    bus_info = gaode_main(or_address, de_address, origin_city)

    pass