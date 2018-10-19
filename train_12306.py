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
        'https://kyfw.12306.cn/otn/leftTicket/queryO?'
        'leftTicketDTO.train_date={}&'
        'leftTicketDTO.from_station={}&'
        'leftTicketDTO.to_station={}&'
        'purpose_codes=ADULT'
    ).format(date, from_station, to_station)
    #print(url)

    return url


# 查询每趟列车的票价。
def get_trainPrice(train_date,train_no,from_station_no,to_station_no,seat_types):
    seat_tables = {"A1": "硬座", "A2": "软座", "A3": "硬卧", "A4": "软卧", "A6": "高级软卧", "F": "动卧", "O": "二等座", "WZ": "无座",
                   "M": "一等座", "A9": "商务座特等座"}
    table_list = list(seat_tables.keys())
    price_list = []
    url = "https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice"

    querystring = {"train_no": train_no, "from_station_no": from_station_no, "to_station_no": to_station_no, "seat_types": seat_types,
                   "train_date": train_date}

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
    }

    response = requests.request("GET", url, headers=headers,verify = False, params=querystring)
    try:
        data = response.json()['data']
    except json.decoder.JSONDecodeError:
        data = '列车停运'
        return data
    for item in table_list:
        try:
            info = data[item]
            tnp = (seat_tables[item], info)
            price_list.append(tnp)
        except KeyError:
            #print("NO SUCH KEY。")
            pass
        finally:
            price_table = dict(price_list)
    return price_table
# 获取信息
def query_train_info(depart_date,url, com_table,origin_city,destination_city):
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
    r = requests.get(url, headers=headers, verify=False)
    try:
        # 获取返回的json数据里的data字段的result结果
        raw_trains = r.json()['data']['result']
    except KeyError:
        raw_trains = 'ERROR : No response data return ,place try again'
        #train_info = main(depart_date, origin_city, destination_city)
        return  raw_trains
    #print(raw_trains)
    train_ticksList= []
    train_date = depart_date
    for raw_train in raw_trains:
        tem = {}
        # 循环遍历每辆列车的信息
        data_list = raw_train.split('|')
        #print(data_list)
        '''
        train_no ,from_station_no , to_station_no and seat_types is for get price of this train. 
        '''
        train_no = data_list[2]
        from_station_no = data_list[16]
        to_station_no =  data_list[17]
        seat_types = data_list[-2]
        price_info = get_trainPrice(train_date, train_no, from_station_no, to_station_no, seat_types)
        tem['price_info'] = price_info
        # 车次号码
        train_no = data_list[3]
        tem['train_no'] = train_no
        # 出发站
        from_station_code = data_list[6]
        from_station_name = com_table[from_station_code]
        tem['from_station_name'] = from_station_name
        # 终点站
        to_station_code = data_list[7]
        to_station_name = com_table[to_station_code]
        tem['to_station_name'] = to_station_name
        # 出发时间
        start_time = data_list[8]
        tem['start_time'] = start_time
        # 到达时间
        arrive_time = data_list[9]
        tem['arrive_time'] = arrive_time
        # 总耗时
        time_fucked_up = data_list[10]
        tem['time_fucked_up'] = time_fucked_up
        # 一等座
        first_class_seat = data_list[31] or '--'
        tem['first_class_seat'] = first_class_seat
        # 二等座
        second_class_seat = data_list[30] or '--'
        tem['second_class_seat'] = second_class_seat
        # 软卧
        soft_sleep = data_list[23] or '--'
        tem['soft_sleep'] = soft_sleep
        # 硬卧
        hard_sleep = data_list[28] or '--'
        tem['hard_sleep'] = hard_sleep
        # 硬座
        hard_seat = data_list[29] or '--'
        tem['hard_seat'] = hard_seat
        # 无座
        no_seat = data_list[26] or '--'
        tem['no_seat'] = no_seat
        # 打印查询结果
        # info = (
        # '车次:{}\n出发站:{}\n目的地:{}\n出发时间:{}\n到达时间:{}\n消耗时间:{}\n座位情况：\n 一等座：「{}」 \n二等座：「{}」\n软卧：「{}」\n硬卧：「{}」\n硬座：「{}」\n无座：「{}」\n\n'.format(
        #     train_no, from_station_name, to_station_name, start_time, arrive_time, time_fucked_up, first_class_seat,
        #     second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat))
        # info_list.append(info)
        train_ticksList.append(tem)
    return train_ticksList
    # except:
    #     return ' 输出信息有误，请重新输入'


if __name__ == '__main__':
    pass