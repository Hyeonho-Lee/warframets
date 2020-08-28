import os
import math
import json
import pandas as pd
import numpy as np
from datetime import date, timedelta
#https://m.kodex.com/calculator3.do
def read_csv_file(path):
    get_path = path
    if os.path.isfile(get_path):
        result = pd.read_csv(get_path, index_col = 0)
        result = result.reset_index()
        return result
    else:
        print('파일이 없습니다.')

def find_item(path):
    item_data = read_csv_file(path)

    #result = item_data['avg_price']
    #list_r = result.tolist()
    #value = get_mdd(list_r)
    #mnd = test['datetime'][value[0]]
    #mnd_date = datetime.strptime(mnd, '%Y-%m-%d')

    #today_date = datetime.today()
    #result_date = int((today_date - mnd_date).days)
    return item_data

value = find_item('/workspace/crawling/data/csv/warframe/ash_prime_set/ash_prime_set.csv')

input_first_date = '2020-06-01'
input_second_date = '2020-08-01'
input_cash = 3200
input_count_0 = 0

####################################################################################

search_date = value[(value['datetime'] == input_first_date) | (value['datetime'] == input_second_date)]

search_index = search_date.index
search_index = search_index.tolist()

####################################################################################
search_all_date = value[(value.index >= search_index[0]) & (value.index <= search_index[1])]

input_first_price = search_date['avg_price'][search_index[0]]
input_second_price = search_date['avg_price'][search_index[1]]
input_count = math.trunc(input_cash / input_first_price) #소지가능 갯수

cal_price_0 = round((input_first_price * input_count), 2) #지불한 플레티넘
cal_price_1 = input_cash - cal_price_0 #지불후 남는 플레티넘
cal_price_2 = round((input_first_price - input_second_price) * -1, 2) #개당 이윤
cal_price_3 = cal_price_2 * input_count #총 이윤
cal_price_4 = cal_price_3 + input_cash #최종 소지 플레티넘
cal_percent = round(float(cal_price_3) / float(cal_price_0) * 100, 2)



print('##############################################')
print('기본 소지 플레티넘: ' + str(input_cash))
print('6월 애쉬프라임 플레티넘: ' + str(input_first_price))
print('최대 소지가능 갯수: ' + str(input_count))
print('구매 하는데 들어간 총 플레티넘: ' + str(cal_price_0))
print('지불후 플레티넘: ' + str(cal_price_1))
print('##############################################')
print('기본 소지 플레티넘: ' + str(input_cash))
print('8월 애쉬프라임 플레티넘: ' + str(input_second_price))
print('개당 이윤 플레티넘: ' + str(cal_price_2))
print('총 이윤 플레티넘: ' + str(cal_price_3))
print('총 이윤 퍼센트: ' + str(cal_percent))
print('최종 소지 플레티넘: ' + str(cal_price_4))
print('##############################################')

#first_price = value[first_date]['avg_price']
#search_max.append(first_price)

#second_date = value['datetime'] == input_second_date
#second_price = value[second_date]['avg_price']
#search_max.append(second_price)