#-*- coding:utf-8 -*-
# Author : 7secondsFish
# Data : 18-10-8 下午5:32


import json

from train_12306 import getStation, get_query_url, query_train_info

json_1 = {"depart_date":"","back_date":"","origin_city":"","destination_city":"","trip_mode":""}

# trip mode
train_url = 'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2018-10-10&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
bus_url = ''
plane_url = ''
self_drive_url = ''

# depart date
depart_date = ''

# back date
back_date = ''

# origin city
origin_city = ''

# destination city
destination_city = ''

# urban transport
urban_transport = ''





if __name__ == '__main__':
    depart_date = '2018-10-19'
    origin_city = '南京'
    destination_city = '重庆'
    with open('code_train.txt', 'r', encoding='UTF-8') as j:
        text1 = j.read()  # .encode('utf-8')
    text = json.loads(text1)
    with open('train_KVchage.txt', 'r', encoding='UTF-8') as u:
        infod = u.read()
    com_table = json.loads(infod)
    url = get_query_url(text,depart_date,origin_city,destination_city)
    print(url)
    lis = query_train_info(depart_date,url, com_table,origin_city,destination_city)
    print(lis)