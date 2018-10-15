#-*- coding:utf-8 -*-
# Author : 7secondsFish
# Data : 18-10-9 下午1:33

'''
获取12306城市名和城市代码的数据
文件名： parse_station.py
'''
import requests
import re
import json


# 关闭https证书验证警告
requests.packages.urllib3.disable_warnings()


def getStation():
    # 12306的城市名和城市代码js文件url
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
    r = requests.get(url, verify=False)
    pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
    result = re.findall(pattern, r.text)
    print(result)
    station = dict(result)  # {'北京北': 'VAP', '北京东': 'BOP', '北京': 'BJP',
    # print(station)
    return station


'''
查询两站之间的火车票信息
输入参数： <date> <from> <to>
12306 api:
'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-07-18&leftTicketDTO.from_station=NJH&leftTicketDTO.to_station=SZH&purpose_codes=ADULT'
'''


# 生成查询的url
def get_query_url(text,depart_date,origin_city,destination_city):
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
    url = (
        'https://kyfw.12306.cn/otn/leftTicket/queryA?'
        'leftTicketDTO.train_date={}&'
        'leftTicketDTO.from_station={}&'
        'leftTicketDTO.to_station={}&'
        'purpose_codes=ADULT'
    ).format(date, from_station, to_station)
    #print(url)

    return url


# 获取信息
def query_train_info(url, text,origin_city,destination_city):
    '''
    查询火车票信息：
    返回 信息查询列表
    '''

    info_list = []
    headers = {
        'host': "kyfw.12306.cn",
        'connection': "keep-alive",
        'cache-control': "no-cache",
        'accept': "*/*",
        'x-requested-with': "XMLHttpRequest",
        'if-modified-since': "0",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        'referer': "https://kyfw.12306.cn/otn/leftTicket/init",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        #'cookie': "JSESSIONID=EB09BEC7A6C4A405CFC33F906E5F7A37; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=31719946.64545.0000; RAIL_EXPIRATION=1539348054364; RAIL_DEVICEID=EFrAs10tQrANUiNSbzpPD67viZgHRY68PCFMzlPFeO6yaxQK0X308VTA6vdU47MSNMFAaBHffJDVEqeVZaTHvxsm99HZ2I9WU1um8GWYV9W2ErBY8VzspakOIgRLttxTE8TYQwA4yPw1mW-AJM6DzNBodyekwOqG; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2018-10-10; _jc_save_toDate=2018-10-09; _jc_save_wfdc_flag=dc"
    }
    try:
        r = requests.get(url, verify=False)
        # 获取返回的json数据里的data字段的result结果
        raw_trains = r.json()['data']['result']
        for raw_train in raw_trains:
            # 循环遍历每辆列车的信息
            data_list = raw_train.split('|')

            # 车次号码
            train_no = data_list[3]
            # 出发站
            from_station_code = data_list[6]
            from_station_name = text[origin_city]
            # 终点站
            to_station_code = data_list[7]
            to_station_name = text[destination_city]
            # 出发时间
            start_time = data_list[8]
            # 到达时间
            arrive_time = data_list[9]
            # 总耗时
            time_fucked_up = data_list[10]
            # 一等座
            first_class_seat = data_list[31] or '--'
            # 二等座
            second_class_seat = data_list[30] or '--'
            # 软卧
            soft_sleep = data_list[23] or '--'
            # 硬卧
            hard_sleep = data_list[28] or '--'
            # 硬座
            hard_seat = data_list[29] or '--'
            # 无座
            no_seat = data_list[26] or '--'

            # 打印查询结果
            info = (
            '车次:{}\n出发站:{}\n目的地:{}\n出发时间:{}\n到达时间:{}\n消耗时间:{}\n座位情况：\n 一等座：「{}」 \n二等座：「{}」\n软卧：「{}」\n硬卧：「{}」\n硬座：「{}」\n无座：「{}」\n\n'.format(
                train_no, from_station_name, to_station_name, start_time, arrive_time, time_fucked_up, first_class_seat,
                second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat))
            info_list.append(info)
        return info_list
    except:
        return ' 输出信息有误，请重新输入'

#  获取全国各地车站编码
text = getStation()
# url = get_query_url(text)
# lis = query_train_info(url, text)

if __name__ == '__main__':
    pass