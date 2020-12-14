#https://docs.google.com/document/d/1121cjBNN4BeZdMBGil6Qbuqse-sWpEXPpitQH5fb_Fo/edit#heading=h.1f16oau3p0p9
import os
import re
import time
import datetime
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dateutil.parser import parse
from bs4 import BeautifulSoup as bs

######################################################
import input_warframe
import pandas_value
#import data_result
######################################################

def warframe_crawling(item, path, path_0):

    get_item = item
    get_path = path
    get_path_0 = path_0

    site = 'https://api.warframe.market/v1/items/{get_item}/statistics'.format(get_item = get_item)
    res = requests.get(site)

    html = res.text
    soup = bs(html, 'html.parser')
    
    with open('/workspace/crawling/data/json/warframe_data_v2.json', 'w') as file:
        data = str(soup)
        json_data = json.loads(data)
        json_data_1 = json.dumps(json_data, indent = 4)
        file.write(json_data_1)

    warframe_data = json_data_1
    
    json_data = json.loads(warframe_data)

    result_data = pd.DataFrame(json_data['payload']['statistics_closed']['90days'])
    
    result_data = result_data[(result_data['mod_rank'] == 0)]
    #print(result_data)
    
    datetime = []
    avg_price = []
    volume = []

    for i in result_data['datetime']:
        datecut = str(i)
        datetime.append(datecut[0:10])

    for i in result_data['moving_avg']:
        avg_price.append(str(i))

    for i in result_data['volume']:
        volume.append(str(i))

    all_data_list = pd.DataFrame({'datetime' : datetime, 'avg_price' : avg_price, 'volume' : volume})
    #all_data_list = all_data_list[::-1]
    
    def make_file(item, path):
        get_item = item
        get_path = path
        if os.path.isfile(get_path):
            all_data_list.to_csv(get_path, mode = 'a', header = False)
            re_result = pd.read_csv(get_path, index_col = 0, error_bad_lines = False)
            all_result = re_result.drop_duplicates('datetime', keep = 'first')
            all_result.to_csv(get_path, mode = 'w')
            value = pandas_value.pandas_value(get_item, 'mod')
            value.to_csv(get_path, mode = 'w')
            #print('데이터 업데이트를 완료했습니다.')
        else:
            all_data_list.to_csv(get_path, mode = 'w')
            value = pandas_value.pandas_value(get_item, 'mod')
            value.to_csv(get_path, mode = 'w')
            #print('새로운 데이터를 저장했습니다.') 

    if os.path.isdir(get_path_0):
        make_file(get_item, get_path)
    else:
        #print('폴더가 없음으로 새로 만들었습니다.')
        os.makedirs(get_path_0)
        make_file(get_item, get_path)

    print(str(get_item) + ' 업데이트를 하였습니다.')

######################################################

startTime = time.time()

input_items = input_warframe.input_item('aura_mods')

for i, v in enumerate(input_items):
    item = str(v)
    path = '/workspace/crawling/data/csv/mod/' + item + '/' + item + '.csv'
    path_0 = '/workspace/crawling/data/csv/mod/' + item
    save_data = warframe_crawling(item, path, path_0)
    endTime = time.time() - startTime
    print(str(round(i / len(input_items) * 100)) + "% 완료했습니다. 시간: " + str(round(endTime)) + "초")

input_items = input_warframe.input_item('warframe_mods')

for i, v in enumerate(input_items):
    item = str(v)
    path = '/workspace/crawling/data/csv/mod/' + item + '/' + item + '.csv'
    path_0 = '/workspace/crawling/data/csv/mod/' + item
    save_data = warframe_crawling(item, path, path_0)
    endTime = time.time() - startTime
    print(str(round(i / len(input_items) * 100)) + "% 완료했습니다. 시간: " + str(round(endTime)) + "초")

input_items = input_warframe.input_item('weapon_mods')

for i, v in enumerate(input_items):
    item = str(v)
    path = '/workspace/crawling/data/csv/mod/' + item + '/' + item + '.csv'
    path_0 = '/workspace/crawling/data/csv/mod/' + item

    save_data = warframe_crawling(item, path, path_0)
    endTime = time.time() - startTime
    print(str(round(i / len(input_items) * 100)) + "% 완료했습니다. 시간: " + str(round(endTime)) + "초")

print("업데이트가 모두 완료했습니다.")

######################################################