import os
import json
import pandas as pd
import numpy as np
from datetime import date, timedelta

######################################################
import input_warframe
######################################################

def input_item(etc):
    item = str(etc)
    path = '/workspace/crawling/data/json/{etc}.json'.format(etc = item)
    with open(path, "r") as json_file:
        json_data = json.load(json_file)

    name_data = []

    for i in json_data[item]:
        name_data.append(str(i["name"]))

    return name_data

def read_csv(path):
    get_path = path
    if os.path.isfile(get_path):
        result = pd.read_csv(get_path, index_col = 0)
        result = result.reset_index()
        return result
    else:
        print('파일이 없습니다.')

def get_all_item():
    all_item = []
    all_item_kr = []
    all_item_en = []
    all_path = []
    all_path_0 = []
    all_path_1 = []
    all_type = []
    all_type_kr = []
    all_type_en = []

    input_items_0 = input_item('warframes')

    for i, v in enumerate(input_items_0):
        item = str(v) + '_set'
        path = '/workspace/crawling/data/csv/warframe/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/warframe/' + item
        img = str(v.title())
        path_1 = 'image/item_image/warframe/' + img + '/' + img + '.png'
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
        all_path_1.append(path_1)

    input_items_1 = input_item('weapons')

    for i, v in enumerate(input_items_1):
        item = str(v) + '_set'
        path = '/workspace/crawling/data/csv/weapon/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/weapon/' + item
        img = str(v.title())
        path_1 = 'image/item_image/weapon/' + img + '/' + img + '.png'
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
        all_path_1.append(path_1)

    input_items_2 = input_item('weapons_etc')

    for i, v in enumerate(input_items_2):
        item = str(v)
        path = '/workspace/crawling/data/csv/weapon/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/weapon/' + item
        img = str(v.title())
        path_1 = 'image/item_image/weapon/' + img + '/' + img + '.png'
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
        all_path_1.append(path_1)

    input_items_3 = input_item('aura_mods')

    for i, v in enumerate(input_items_3):
        item = str(v)
        path = '/workspace/crawling/data/csv/mod/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/mod/' + item
        img = str(v.title())
        path_1 = 'image/item_image/mod/' + img + '/' + img + '.png'
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
        all_path_1.append(path_1)

    input_items_4 = input_item('warframe_mods')

    for i, v in enumerate(input_items_4):
        item = str(v)
        path = '/workspace/crawling/data/csv/mod/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/mod/' + item
        img = str(v.title())
        path_1 = 'image/item_image/mod/' + img + '/' + img + '.png'
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
        all_path_1.append(path_1)

    input_items_5 = input_item('items_etc')

    for i, v in enumerate(input_items_5):
        item = str(v)
        path = '/workspace/crawling/data/csv/etc/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/etc/' + item
        img = str(v.title())
        path_1 = 'image/item_image/etc/' + img + '/' + img + '.png'
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
        all_path_1.append(path_1)

    input_items_6 = input_item('weapon_mods')

    for i, v in enumerate(input_items_6):
        item = str(v)
        path = '/workspace/crawling/data/csv/mod/' + item + '/' + item + '.csv'
        path_0 = '/workspace/crawling/data/csv/mod/' + item
        img = str(v.title())
        path_1 = 'image/item_image/mod/' + img + '/' + img + '.png'
        all_item.append(item)
        all_path.append(path)
        all_path_0.append(path_0)
        all_path_1.append(path_1)

    return all_item, all_path, all_path_0, all_path_1

def make_file(get_path):
    if os.path.isfile(get_path):
        make.to_csv(get_path, mode = 'a', header = False)
        result = pd.read_csv(get_path, index_col = 0, error_bad_lines = False)
        results = result.drop_duplicates('name', keep = 'first')
        results.to_csv(get_path, mode = 'w')
    else:
        make.to_csv(get_path, mode = 'w')
        make_file(get_path)

def reset(date, value):
    path = '/workspace/crawling/data/csv/result/date/{date}/{value}.csv'.format(date = date, value = value)
    if os.path.isfile(path):
        os.remove(r"/workspace/crawling/data/csv/result/date/{date}/{value}.csv".format(date = date, value = value))
    else:
        reset = open(path, 'w')
        os.remove(r"/workspace/crawling/data/csv/result/date/{date}/{value}.csv".format(date = date, value = value))

all_item, all_path, all_path_0, all_path_1 = get_all_item()

date_item = []
date_path = []
date_value = "2020-03-08"
date_dir = "/workspace/crawling/data/csv/result/date/" + date_value + "/"

for i, v in enumerate(all_item):
    value = read_csv(all_path[i])
    for i in range(0, len(value)):
        if value['datetime'].values[i] == date_value:
            date_item.append(v)
            break

get_item = []
get_path = []
etc_path = '../data/csv/etc'
mod_path = '../data/csv/mod'
warframe_path = '../data/csv/warframe'
weapon_path = '../data/csv/weapon'

for i, v in enumerate(os.listdir(etc_path)):
    path_name = '/workspace/crawling/data/csv/etc/' + str(v) + '/' + str(v) + '.csv'
    get_item.append(v)
    get_path.append(path_name)
for i, v in enumerate(os.listdir(mod_path)):
    path_name = '/workspace/crawling/data/csv/mod/' + str(v) + '/' + str(v) + '.csv'
    get_item.append(v)
    get_path.append(path_name)
for i, v in enumerate(os.listdir(warframe_path)):
    path_name = '/workspace/crawling/data/csv/warframe/' + str(v) + '/' + str(v) + '.csv'
    get_item.append(v)
    get_path.append(path_name)
for i, v in enumerate(os.listdir(weapon_path)):
    path_name = '/workspace/crawling/data/csv/weapon/' + str(v) + '/' + str(v) + '.csv'
    get_item.append(v)
    get_path.append(path_name)

for i, v in enumerate(date_item):
    index = get_item.index(date_item[i])
    date_path.append(get_path[index])

path_1 = '/workspace/crawling/data/csv/result/date/' + date_value + '/result.csv'
path_all_top = '/workspace/crawling/data/csv/result/date/' + date_value + '/all_top.csv'
path_all_bottom = '/workspace/crawling/data/csv/result/date/' + date_value + '/all_bottom.csv'
path_today_top = '/workspace/crawling/data/csv/result/date/' + date_value + '/today_top.csv'
path_today_bottom = '/workspace/crawling/data/csv/result/date/' + date_value + '/today_bottom.csv'
path_today_volume = '/workspace/crawling/data/csv/result/date/' + date_value + '/today_volume.csv'
path_recommend_item = '/workspace/crawling/data/csv/result/date/' + date_value + '/recommend_item.csv'
path_recommend_top = '/workspace/crawling/data/csv/result/date/' + date_value + '/recommend_top.csv'
path_recommend_bottom = '/workspace/crawling/data/csv/result/date/' + date_value + '/recommend_bottom.csv'

if(os.path.isdir(date_dir) == False):
    os.makedirs(os.path.join(date_dir))
    for i in range(0, len(date_item)):
        make = read_csv(date_path[i])
        make = make[make["datetime"] == date_value]
        make['name'] = date_item[i]
        make_file(path_1)
    print(date_value + "가 생성 되었습니다")

reset(date_value, 'result')
for i in range(0, len(date_item)):
    make = read_csv(date_path[i])
    make = make[make["datetime"] == date_value]
    make['name'] = date_item[i]
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
result = result_today.sort_values(by='vol_lank', axis = 0, ascending = False)
recommend_item = result.head(10)

result = result_today.sort_values(by='vol_before', axis = 0, ascending = False)
recommend_top = result.head(10)
result = result_today.sort_values(by='vol_before', axis = 0)
recommend_bottom = result.head(10)

reset(date_value, 'all_top')
reset(date_value, 'all_bottom')
reset(date_value, 'today_top')
reset(date_value, 'today_bottom')
reset(date_value, 'today_volume')
reset(date_value, 'recommend_item')
reset(date_value, 'recommend_top')
reset(date_value, 'recommend_bottom')

all_top.to_csv(path_all_top, mode = 'w')
all_bottom.to_csv(path_all_bottom, mode = 'w')
today_top.to_csv(path_today_top, mode = 'w')
today_bottom.to_csv(path_today_bottom, mode = 'w')
today_volume.to_csv(path_today_volume, mode = 'w')
recommend_item.to_csv(path_recommend_item, mode ='w')
recommend_top.to_csv(path_recommend_top, mode ='w')
recommend_bottom.to_csv(path_recommend_bottom, mode ='w')
    
print(date_value + "가 정리 되었습니다")