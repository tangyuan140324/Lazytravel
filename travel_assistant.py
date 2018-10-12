#-*- coding:utf-8 -*-
# Author : 7secondsFish
# Data : 18-10-8 下午5:32

import requests
from bs4 import BeautifulSoup
import re
import time
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
    depart_date = '2018-10-10'
    origin_city = '南京'
    destination_city = '成都'
    text = getStation()
    print(text)
    exit()
    url = get_query_url(text,depart_date,origin_city,destination_city)
    lis = query_train_info(url, text)
    for item in lis:
        print(item)
    pass