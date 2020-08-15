import os
import json
import pandas as pd
import numpy as np
from datetime import date, timedelta

######################################################
import input_warframe
######################################################

def read_csv(path):
    get_path = path
    if os.path.isfile(get_path):
        result = pd.read_csv(get_path, index_col = 0)
        result = result.reset_index()
        return result
    else:
        print('파일이 없습니다.')

def get_all():
    all_item = []
    all_path = []
    all_path_0 = []

    input_items_0 = input_warframe.input_item('warframes')

    for i, v in enumerate(input_items_0):
        item = str(v) + '_set'
        path = '/workspace/crawling/data/csv/warframe/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/warframe/' + item
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)

    input_items_1 = input_warframe.input_item('weapons')

    for i, v in enumerate(input_items_1):
        item = str(v) + '_set'
        path = '/workspace/crawling/data/csv/weapon/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/weapon/' + item
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
        
    input_items_2 = input_warframe.input_item('weapons_etc')

    for i, v in enumerate(input_items_2):
        item = str(v)
        path = '/workspace/crawling/data/csv/weapon/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/weapon/' + item
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
        
    input_items_3 = input_warframe.input_item('aura_mods')

    for i, v in enumerate(input_items_3):
        item = str(v)
        path = '/workspace/crawling/data/csv/mod/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/mod/' + item
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)

    input_items_4 = input_warframe.input_item('warframe_mods')

    for i, v in enumerate(input_items_4):
        item = str(v)
        path = '/workspace/crawling/data/csv/mod/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/mod/' + item
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)

    input_items_5 = input_warframe.input_item('items_etc')

    for i, v in enumerate(input_items_5):
        item = str(v)
        path = '/workspace/crawling/data/csv/etc/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/etc/' + item
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
    
    input_items_6 = input_warframe.input_item('weapon_mods')

    for i, v in enumerate(input_items_6):
        item = str(v)
        path = '/workspace/crawling/data/csv/mod/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/mod/' + item
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)


    return all_item, all_path, all_path_0

def date_count():
    today = date.today()
    today = str(today.strftime('%Y-%m-%d'))
    yesterday = date.today() - timedelta(1)
    yesterday = str(yesterday.strftime('%Y-%m-%d'))
    return yesterday

def make_file(get_path):
    if os.path.isfile(get_path):
        last_tf.to_csv(get_path, mode = 'a', header = False)
        result = pd.read_csv(get_path, index_col = 0, error_bad_lines = False)
        results = result.drop_duplicates('name', keep = 'first')
        results.to_csv(get_path, mode = 'w')
    else:
        last_tf.to_csv(get_path, mode = 'w')
        make_file(get_path)

def reset(value):
    path = '/workspace/crawling/data/csv/result/{value}.csv'.format(value = value)
    if os.path.isfile(path):
        os.remove(r"/workspace/crawling/data/csv/result/{value}.csv".format(value = value))
    else:
        reset = open(path, 'w')
        os.remove(r"/workspace/crawling/data/csv/result/{value}.csv".format(value = value))

item, path, path_0 = get_all()
yesterday = date_count()

path_1 = '/workspace/crawling/data/csv/result/result.csv'
path_all_top = '/workspace/crawling/data/csv/result/all_top.csv'
path_all_bottom = '/workspace/crawling/data/csv/result/all_bottom.csv'
path_today_top = '/workspace/crawling/data/csv/result/today_top.csv'
path_today_bottom = '/workspace/crawling/data/csv/result/today_bottom.csv'
path_today_volume = '/workspace/crawling/data/csv/result/today_volume.csv'

reset('result')

for i, v in enumerate(item):
    value = read_csv(path[i])
    last_value = value.tail(1)
    last_tf = last_value.loc[last_value['datetime'] == yesterday]
    last_tf['name'] = item[i]
    make_file(path_1)

result_today = read_csv(path_1)

del result_today['level_0']
del result_today['index']
remove_data = result_today[result_today['avg_price'] <= 30].index
result_today = result_today.drop(remove_data)
remove_datas = result_today[result_today['volume'] < 10].index
result_today = result_today.drop(remove_datas)

result = result_today.sort_values(by='lank', axis = 0, ascending = False)
result = result.reset_index()
all_top = result.head(10)
result = result_today.sort_values(by='lank', axis = 0)
all_bottom = result.head(10)

result = result_today.sort_values(by='day_percent', axis = 0, ascending = False)
today_top = result.head(10)
result = result_today.sort_values(by='day_percent', axis = 0)
today_bottom = result.head(10)

result = result_today.sort_values(by='volume', axis = 0, ascending = False)
today_volume = result.head(10)

reset('all_top')
reset('all_bottom')
reset('today_top')
reset('today_bottom')
reset('today_volume')

all_top.to_csv(path_all_top, mode = 'w')
all_bottom.to_csv(path_all_bottom, mode = 'w')
today_top.to_csv(path_today_top, mode = 'w')
today_bottom.to_csv(path_today_bottom, mode = 'w')
today_volume.to_csv(path_today_volume, mode = 'w')