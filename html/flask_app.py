import os
import sys
import json
import math
import datetime
import pandas as pd
import numpy as np
import random
import ssl
from io import StringIO
from flask import Flask, url_for, render_template, request, redirect, session, Response

#https://www.chartjs.org/
#https://datatables.net/
#https://rpc-flask-app.run.goorm.io/ 홈페이지 사이트
#https://rpc-test-app.run.goorm.io/ 테스트 사이트
#https://icons8.com/icons 아이콘 사이트
#https://pixlr.com/e/ 포토샵 사이트
#https://zamezzz.tistory.com/309
#https://offbyone.tistory.com/260
#https://keraskorea.github.io/posts/2018-10-25-Keras%EB%A5%BC%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EC%A3%BC%EC%8B%9D%20%EA%B0%80%EA%B2%A9%20%EC%98%88%EC%B8%A1/
#https://github.com/llSourcell/How-to-Predict-Stock-Prices-Easily-Demo/blob/master/lstm.py

#=======================================================================#

def read_csv_file(path):
    get_path = path
    if os.path.isfile(get_path):
        result = pd.read_csv(get_path, index_col = 0)
        result = result.reset_index()
        return result
    else:
        print('파일이 없습니다.')

def read_csv(name, types):
    names = name + '_set'
    name_csv = names + '.csv'
    path = ''
    if types == 'result':
        name_csv = name + '.csv'
        path = '/workspace/crawling/data/csv/{types}/{name_csv}'.format(types = types, name_csv = name_csv)
    elif types == 'weapon_etc':
        name_csv = name + '.csv'
        path = '/workspace/crawling/data/csv/weapon/{names}/{name_csv}'.format(names = name, name_csv = name_csv)
    elif types == 'aura_mods':
        name_csv = name + '.csv'
        path = '/workspace/crawling/data/csv/mod/{names}/{name_csv}'.format(names = name, name_csv = name_csv)
    elif types == 'warframe_mods':
        name_csv = name + '.csv'
        path = '/workspace/crawling/data/csv/mod/{names}/{name_csv}'.format(names = name, name_csv = name_csv)
    elif types == 'items_etc':
        name_csv = name + '.csv'
        path = '/workspace/crawling/data/csv/etc/{names}/{name_csv}'.format(names = name, name_csv = name_csv)
    elif types == 'weapon_mods':
        name_csv = name + '.csv'
        path = '/workspace/crawling/data/csv/mod/{names}/{name_csv}'.format(names = name, name_csv = name_csv)
    else:
        path = '/workspace/crawling/data/csv/{types}/{name}/{name_csv}'.format(types = types, name = names, name_csv = name_csv)
    get_path = path
    if os.path.isfile(get_path):
        result = pd.read_csv(get_path, index_col = 0)
        result = result.reset_index()
        if types != 'result':
            result = result[::-1]
        return result
    else:
        result = pd.DataFrame()
        return result

def input_item(etc):
    item = str(etc)
    path = '/workspace/crawling/data/json/{etc}.json'.format(etc = item)
    with open(path, "r") as json_file:
        json_data = json.load(json_file)

    name_data = []

    for i in json_data[item]:
        name_data.append(str(i["name"]))

    return name_data

def input_item_kr(etc):
    item = str(etc)
    path = '/workspace/crawling/data/json/{etc}.json'.format(etc = item)
    with open(path, "r") as json_file:
        json_data = json.load(json_file)

    name_data = []

    for i in json_data[item]:
        name_data.append(str(i["kr_name"]))

    return name_data

def input_item_en(etc):
    item = str(etc)
    path = '/workspace/crawling/data/json/{etc}.json'.format(etc = item)
    with open(path, "r") as json_file:
        json_data = json.load(json_file)

    name_data = []

    for i in json_data[item]:
        name_data.append(str(i["en_name"]))

    return name_data

def input_item_type(etc):
    item = str(etc)
    path = '/workspace/crawling/data/json/{etc}.json'.format(etc = item)
    with open(path, "r") as json_file:
        json_data = json.load(json_file)

    name_data = []

    for i in json_data[item]:
        name_data.append(str(i["type"]))

    return name_data

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
    input_items_0_kr = input_item_kr('warframes')
    input_items_0_en = input_item_en('warframes')
    input_types_0 = input_item_type('warframes')

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

    for i, v in enumerate(input_items_0_kr):
        item = str(v)
        all_item_kr.append(item)

    for i, v in enumerate(input_items_0_en):
        item = str(v)
        all_item_en.append(item)

    for i, v in enumerate(input_types_0):
        item = str(v)
        all_type.append(item)

    input_items_1 = input_item('weapons')
    input_items_1_kr = input_item_kr('weapons')
    input_items_1_en = input_item_en('weapons')
    input_types_1 = input_item_type('weapons')

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

    for i, v in enumerate(input_items_1_kr):
        item = str(v)
        all_item_kr.append(item)

    for i, v in enumerate(input_items_1_en):
        item = str(v)
        all_item_en.append(item)

    for i, v in enumerate(input_types_1):
        item = str(v)
        all_type.append(item)

    input_items_2 = input_item('weapons_etc')
    input_items_2_kr = input_item_kr('weapons_etc')
    input_items_2_en = input_item_en('weapons_etc')
    input_types_2 = input_item_type('weapons_etc')

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

    for i, v in enumerate(input_items_2_kr):
        item = str(v)
        all_item_kr.append(item)

    for i, v in enumerate(input_items_2_en):
        item = str(v)
        all_item_en.append(item)

    for i, v in enumerate(input_types_2):
        item = str(v)
        all_type.append(item)

    input_items_3 = input_item('aura_mods')
    input_items_3_kr = input_item_kr('aura_mods')
    input_items_3_en = input_item_en('aura_mods')
    input_types_3 = input_item_type('aura_mods')

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

    for i, v in enumerate(input_items_3_kr):
        item = str(v)
        all_item_kr.append(item)

    for i, v in enumerate(input_items_3_en):
        item = str(v)
        all_item_en.append(item)

    for i, v in enumerate(input_types_3):
        item = str(v)
        all_type.append(item)

    input_items_4 = input_item('warframe_mods')
    input_items_4_kr = input_item_kr('warframe_mods')
    input_items_4_en = input_item_en('warframe_mods')
    input_types_4 = input_item_type('warframe_mods')

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

    for i, v in enumerate(input_items_4_kr):
        item = str(v)
        all_item_kr.append(item)

    for i, v in enumerate(input_items_4_en):
        item = str(v)
        all_item_en.append(item)

    for i, v in enumerate(input_types_4):
        item = str(v)
        all_type.append(item)

    input_items_5 = input_item('items_etc')
    input_items_5_kr = input_item_kr('items_etc')
    input_items_5_en = input_item_en('items_etc')
    input_types_5 = input_item_type('items_etc')

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

    for i, v in enumerate(input_items_5_kr):
        item = str(v)
        all_item_kr.append(item)

    for i, v in enumerate(input_items_5_en):
        item = str(v)
        all_item_en.append(item)

    for i, v in enumerate(input_types_5):
        item = str(v)
        all_type.append(item)

    input_items_6 = input_item('weapon_mods')
    input_items_6_kr = input_item_kr('weapon_mods')
    input_items_6_en = input_item_en('weapon_mods')
    input_types_6 = input_item_type('weapon_mods')

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

    for i, v in enumerate(input_items_6_kr):
        item = str(v)
        all_item_kr.append(item)

    for i, v in enumerate(input_items_6_en):
        item = str(v)
        all_item_en.append(item)

    for i, v in enumerate(input_types_6):
        item = str(v)
        all_type.append(item)

    for i, v in enumerate(all_item_kr):
        if all_type[i] == "primary":
            all_type_kr.append("주무기")
        elif all_type[i] == "secondary":
            all_type_kr.append("보조무기")
        elif all_type[i] == "melee":
            all_type_kr.append("근접무기")
        elif all_type[i] == "archwing":
            all_type_kr.append("아크윙")
        elif all_type[i] == "warframe":
            all_type_kr.append("워프레임")
        elif all_type[i] == "aura_mod":
            all_type_kr.append("워프레임 모드")
        elif all_type[i] == "warframe_mod":
            all_type_kr.append("워프레임 모드")
        elif all_type[i] == "arcane":
            all_type_kr.append("아케인")
        elif all_type[i] == "magus":
            all_type_kr.append("아케인")
        elif all_type[i] == "virtuos":
            all_type_kr.append("아케인")
        elif all_type[i] == "pax":
            all_type_kr.append("아케인")
        elif all_type[i] == "exodia":
            all_type_kr.append("아케인")
        elif all_type[i] == "primary_mod":
            all_type_kr.append("주무기 모드")
        elif all_type[i] == "rifle_mod":
            all_type_kr.append("주무기 모드")
        elif all_type[i] == "shotgun_mod":
            all_type_kr.append("주무기 모드")
        elif all_type[i] == "sniper_mod":
            all_type_kr.append("주무기 모드")
        elif all_type[i] == "bow_mod":
            all_type_kr.append("주무기 모드")
        elif all_type[i] == "pistol_mod":
            all_type_kr.append("보조무기 모드")
        elif all_type[i] == "melee_mod":
            all_type_kr.append("근접무기 모드")
        elif all_type[i] == "stance_mod":
            all_type_kr.append("근접무기 모드")
        elif all_type[i] == "ephemera":
            all_type_kr.append("업데이트")
        elif all_type[i] == "necramech_mod":
            all_type_kr.append("업데이트")
        else:
            all_type_kr.append("기타")

    for i, v in enumerate(all_item_en):
        if all_type[i] == "primary":
            all_type_en.append("Primary")
        elif all_type[i] == "secondary":
            all_type_en.append("Secondary")
        elif all_type[i] == "melee":
            all_type_en.append("Melee")
        elif all_type[i] == "archwing":
            all_type_en.append("Archwing")
        elif all_type[i] == "warframe":
            all_type_en.append("Warframe")
        elif all_type[i] == "aura_mod":
            all_type_en.append("Aura Mod")
        elif all_type[i] == "warframe_mod":
            all_type_en.append("Warframe Mod")
        elif all_type[i] == "arcane":
            all_type_en.append("Arcane")
        elif all_type[i] == "magus":
            all_type_en.append("Arcane")
        elif all_type[i] == "virtuos":
            all_type_en.append("Arcane")
        elif all_type[i] == "pax":
            all_type_en.append("Arcane")
        elif all_type[i] == "exodia":
            all_type_en.append("Arcane")
        elif all_type[i] == "primary_mod":
            all_type_en.append("Primary Mod")
        elif all_type[i] == "rifle_mod":
            all_type_en.append("Primary Mod")
        elif all_type[i] == "shotgun_mod":
            all_type_en.append("Primary Mod")
        elif all_type[i] == "sniper_mod":
            all_type_en.append("Primary Mod")
        elif all_type[i] == "bow_mod":
            all_type_en.append("Primary Mod")
        elif all_type[i] == "pistol_mod":
            all_type_en.append("Secondary Mod")
        elif all_type[i] == "melee_mod":
            all_type_en.append("Melee Mod")
        elif all_type[i] == "stance_mod":
            all_type_en.append("Melee Mod")
        elif all_type[i] == "ephemera":
            all_type_en.append("Update")
        elif all_type[i] == "necramech_mod":
            all_type_en.append("Update")
        else:
            all_type_en.append("Etc")

    return all_item, all_item_kr, all_item_en, all_path, all_path_0, all_path_1, all_type, all_type_kr, all_type_en

def change_to_kr(csv_name, etc, text):
    item_name = []
    item_en_name = []
    item_kr_name = []

    with open('/workspace/crawling/data/json/warframes.json', 'r') as file:
        json_data = json.load(file)
    result_data = json_data['warframes']
    with open('/workspace/crawling/data/json/weapons.json', 'r') as file_1:
        json_data_1 = json.load(file_1)
    result_data_1 = json_data_1['weapons']
    with open('/workspace/crawling/data/json/weapons_etc.json', 'r') as file_2:
        json_data_2 = json.load(file_2)
    result_data_2 = json_data_2['weapons_etc']
    with open('/workspace/crawling/data/json/aura_mods.json', 'r') as file_3:
        json_data_3 = json.load(file_3)
    result_data_3 = json_data_3['aura_mods']
    with open('/workspace/crawling/data/json/warframe_mods.json', 'r') as file_4:
        json_data_4 = json.load(file_4)
    result_data_4 = json_data_4['warframe_mods']
    with open('/workspace/crawling/data/json/items_etc.json', 'r') as file_5:
        json_data_5 = json.load(file_5)
    result_data_5 = json_data_5['items_etc']
    with open('/workspace/crawling/data/json/weapon_mods.json', 'r') as file_6:
        json_data_6 = json.load(file_6)
    result_data_6 = json_data_6['weapon_mods']

    for i in range(0, len(result_data)):
        result = result_data[i]['name']
        en_result = result_data[i]['en_name']
        kr_result = result_data[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    for i in range(0, len(result_data_1)):
        result = result_data_1[i]['name']
        en_result = result_data_1[i]['en_name']
        kr_result = result_data_1[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    for i in range(0, len(result_data_2)):
        result = result_data_2[i]['name']
        en_result = result_data_2[i]['en_name']
        kr_result = result_data_2[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    for i in range(0, len(result_data_3)):
        result = result_data_3[i]['name']
        en_result = result_data_3[i]['en_name']
        kr_result = result_data_3[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    for i in range(0, len(result_data_4)):
        result = result_data_4[i]['name']
        en_result = result_data_4[i]['en_name']
        kr_result = result_data_4[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    for i in range(0, len(result_data_5)):
        result = result_data_5[i]['name']
        en_result = result_data_5[i]['en_name']
        kr_result = result_data_5[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    for i in range(0, len(result_data_6)):
        result = result_data_6[i]['name']
        en_result = result_data_6[i]['en_name']
        kr_result = result_data_6[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    path = '/workspace/crawling/data/csv/result/{name}.csv'.format(name = csv_name)
    resource = read_csv_file(path)

    result_all = []
    result_value = ''
    types = etc

    if types == 'in':
        for i in range(0, len(resource)):
            result = resource['name'][i]
            results = str(result)
            result_1 = results.replace('_set', '')
            if result_1 in item_name:
                count = item_name.index(result_1)
                re_text = item_kr_name[count]
                result_all.append(re_text)
        return result_all
    elif types == 'out':
        input_text = text
        if input_text in item_kr_name:
            count = item_kr_name.index(input_text)
            re_text = item_name[count]
            result_value = re_text + '_set'
        else:
            result_value = input_text
        return result_value

def change_to_en(csv_name, etc, text):
    item_name = []
    item_en_name = []
    item_kr_name = []

    with open('/workspace/crawling/data/json/warframes.json', 'r') as file:
        json_data = json.load(file)
    result_data = json_data['warframes']
    with open('/workspace/crawling/data/json/weapons.json', 'r') as file_1:
        json_data_1 = json.load(file_1)
    result_data_1 = json_data_1['weapons']
    with open('/workspace/crawling/data/json/weapons_etc.json', 'r') as file_2:
        json_data_2 = json.load(file_2)
    result_data_2 = json_data_2['weapons_etc']
    with open('/workspace/crawling/data/json/aura_mods.json', 'r') as file_3:
        json_data_3 = json.load(file_3)
    result_data_3 = json_data_3['aura_mods']
    with open('/workspace/crawling/data/json/warframe_mods.json', 'r') as file_4:
        json_data_4 = json.load(file_4)
    result_data_4 = json_data_4['warframe_mods']
    with open('/workspace/crawling/data/json/items_etc.json', 'r') as file_5:
        json_data_5 = json.load(file_5)
    result_data_5 = json_data_5['items_etc']
    with open('/workspace/crawling/data/json/weapon_mods.json', 'r') as file_6:
        json_data_6 = json.load(file_6)
    result_data_6 = json_data_6['weapon_mods']

    for i in range(0, len(result_data)):
        result = result_data[i]['name']
        en_result = result_data[i]['en_name']
        kr_result = result_data[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    for i in range(0, len(result_data_1)):
        result = result_data_1[i]['name']
        en_result = result_data_1[i]['en_name']
        kr_result = result_data_1[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    for i in range(0, len(result_data_2)):
        result = result_data_2[i]['name']
        en_result = result_data_2[i]['en_name']
        kr_result = result_data_2[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    for i in range(0, len(result_data_3)):
        result = result_data_3[i]['name']
        en_result = result_data_3[i]['en_name']
        kr_result = result_data_3[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    for i in range(0, len(result_data_4)):
        result = result_data_4[i]['name']
        en_result = result_data_4[i]['en_name']
        kr_result = result_data_4[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    for i in range(0, len(result_data_5)):
        result = result_data_5[i]['name']
        en_result = result_data_5[i]['en_name']
        kr_result = result_data_5[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    for i in range(0, len(result_data_6)):
        result = result_data_6[i]['name']
        en_result = result_data_6[i]['en_name']
        kr_result = result_data_6[i]['kr_name']
        item_name.append(str(result))
        item_en_name.append(str(en_result))
        item_kr_name.append(str(kr_result))

    path = '/workspace/crawling/data/csv/result/{name}.csv'.format(name = csv_name)
    resource = read_csv_file(path)

    result_all = []
    result_value = ''
    types = etc

    if types == 'in':
        for i in range(0, len(resource)):
            result = resource['name'][i]
            results = str(result)
            result_1 = results.replace('_set', '')
            if result_1 in item_name:
                count = item_name.index(result_1)
                re_text = item_en_name[count]
                result_all.append(re_text)
        return result_all
    elif types == 'out':
        input_text = text
        if input_text in item_en_name:
            count = item_en_name.index(input_text)
            re_text = item_name[count]
            result_value = re_text + '_set'
        else:
            result_value = input_text
        return result_value

def get_today_date():
    result = read_csv('result', 'result')
    date = result['datetime']
    datetime = str(date[0])
    return datetime

def get_visit():
    today = datetime.datetime.now()
    year = str(today.year)
    month = str(today.month)
    day = str(today.day)

    if len(month) == 1:
        month = '0' + month

    visit_count = session.get('visit_count') != 1

    with open('/workspace/crawling/data/json/visitant.json', "r") as json_visit:
        visit_data = json.load(json_visit)

    if visit_count:
        session['visit_count'] = 1

        query_1 = dict()
        year_month = dict()
        year_month["year_month"] = year + month
        year_month["day"] = day
        result = session.get('visit_count')
        year_month["count"] = visit_data["date"]["count"] + 1
        query_1["date"] = year_month

        with open('/workspace/crawling/data/json/visitant.json', 'w', encoding='utf-8') as update_visit:
            json.dump(query_1, update_visit, indent = 4)

    with open('/workspace/crawling/data/json/visitant.json', "r") as json_visits:
        visits_data = json.load(json_visits)
    result = visits_data["date"]["count"]
    return result

#=======================================================================#

app = Flask(__name__)
random = os.urandom(24)
app.secret_key = random

@app.route('/')
def index():

    visit_count = get_visit()

    today_datetime = get_today_date()
    all_top = read_csv('all_top', 'result')
    all_bottom = read_csv('all_bottom', 'result')
    today_top = read_csv('today_top', 'result')
    today_bottom = read_csv('today_bottom', 'result')
    today_volume = read_csv('today_volume', 'result')
    today_all = read_csv('result', 'result')

    all_item, all_item_kr, all_item_en, all_path, all_path_0, all_path_1, all_type, all_type_kr, all_type_en = get_all_item()
    def find_path(name, types):
        if types == 'path':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path = all_path[i]
                    return path
        elif types == 'path_0':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_0 = all_path_0[i]
                    return path_0
        elif types == 'path_1':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_1 = all_path_1[i]
                    return path_1

    a_top_name = []
    a_top_kr_name = []
    a_top_price = []
    a_top_before = []
    a_top_percent = []
    a_top_path = []
    a_top_path_0 = []
    a_top_path_1 = []
    a_top_name = all_top['name'].tolist()
    a_top_kr_name = change_to_kr('all_top', 'in', '')
    a_top_price = all_top['avg_price'].tolist()
    a_top_before = all_top['day_before'].tolist()
    a_top_percent = all_top['day_percent'].tolist()
    for i in a_top_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        a_top_path.append(str(result))
        a_top_path_0.append(str(result_0))
        a_top_path_1.append(str(result_1))

    a_bottom_name = []
    a_bottom_kr_name = []
    a_bottom_price = []
    a_bottom_before = []
    a_bottom_percent = []
    a_bottom_path = []
    a_bottom_path_0 = []
    a_bottom_path_1 = []
    a_bottom_name = all_bottom['name'].tolist()
    a_bottom_kr_name = change_to_kr('all_bottom', 'in', '')
    a_bottom_price = all_bottom['avg_price'].tolist()
    a_bottom_before = all_bottom['day_before'].tolist()
    a_bottom_percent = all_bottom['day_percent'].tolist()
    for i in a_bottom_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        a_bottom_path.append(str(result))
        a_bottom_path_0.append(str(result_0))
        a_bottom_path_1.append(str(result_1))

    t_top_name = []
    t_top_kr_name = []
    t_top_price = []
    t_top_before = []
    t_top_percent = []
    t_top_path = []
    t_top_path_0 = []
    t_top_path_1 = []
    t_top_name = today_top['name'].tolist()
    t_top_kr_name = change_to_kr('today_top', 'in', '')
    t_top_price = today_top['avg_price'].tolist()
    t_top_before = today_top['day_before'].tolist()
    t_top_percent = today_top['day_percent'].tolist()
    for i in t_top_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_top_path.append(str(result))
        t_top_path_0.append(str(result_0))
        t_top_path_1.append(str(result_1))

    t_bottom_name = []
    t_bottom_kr_name = []
    t_bottom_price = []
    t_bottom_before = []
    t_bottom_percent = []
    t_bottom_path = []
    t_bottom_path_0 = []
    t_bottom_path_1 = []
    t_bottom_name = today_bottom['name'].tolist()
    t_bottom_kr_name = change_to_kr('today_bottom', 'in', '')
    t_bottom_price = today_bottom['avg_price'].tolist()
    t_bottom_before = today_bottom['day_before'].tolist()
    t_bottom_percent = today_bottom['day_percent'].tolist()
    for i in t_bottom_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_bottom_path.append(str(result))
        t_bottom_path_0.append(str(result_0))
        t_bottom_path_1.append(str(result_1))

    t_all_name = []
    t_all_kr_name = []
    t_all_price = []
    t_all_before = []
    t_all_befores = []
    t_all_volume = []
    t_all_date = []
    t_all_percent = []
    t_all_lank = []
    t_all_path = []
    t_all_path_0 = []
    t_all_path_1 = []
    t_all_name = today_all['name'].tolist()
    t_all_name_count = len(t_all_name)
    t_all_kr_name = change_to_kr('result', 'in', '')
    t_all_price = today_all['avg_price'].tolist()
    t_all_before = today_all['day_before'].tolist()
    t_all_befores = today_all['yn_before'].tolist()
    t_all_volume = today_all['volume'].tolist()
    t_all_date = today_all['datetime'].tolist()
    t_all_percent = today_all['day_percent'].tolist()
    t_all_lank = today_all['lank'].tolist()

    for i in t_all_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_all_path.append(str(result))
        t_all_path_0.append(str(result_0))
        t_all_path_1.append(str(result_1))

    return render_template('index.html', **locals())
######################################################################
@app.route('/en/')
def index_value_en():

    visit_count = get_visit()

    today_datetime = get_today_date()
    all_top = read_csv('all_top', 'result')
    all_bottom = read_csv('all_bottom', 'result')
    today_top = read_csv('today_top', 'result')
    today_bottom = read_csv('today_bottom', 'result')
    today_volume = read_csv('today_volume', 'result')
    today_all = read_csv('result', 'result')

    all_item, all_item_kr, all_item_en, all_path, all_path_0, all_path_1, all_type, all_type_kr, all_type_en = get_all_item()
    def find_path(name, types):
        if types == 'path':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path = all_path[i]
                    return path
        elif types == 'path_0':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_0 = all_path_0[i]
                    return path_0
        elif types == 'path_1':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_1 = all_path_1[i]
                    return path_1

    a_top_name = []
    a_top_en_name = []
    a_top_price = []
    a_top_before = []
    a_top_percent = []
    a_top_path = []
    a_top_path_0 = []
    a_top_path_1 = []
    a_top_name = all_top['name'].tolist()
    a_top_en_name = change_to_en('all_top', 'in', '')
    a_top_price = all_top['avg_price'].tolist()
    a_top_before = all_top['day_before'].tolist()
    a_top_percent = all_top['day_percent'].tolist()
    for i in a_top_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        a_top_path.append(str(result))
        a_top_path_0.append(str(result_0))
        a_top_path_1.append(str(result_1))

    a_bottom_name = []
    a_bottom_en_name = []
    a_bottom_price = []
    a_bottom_before = []
    a_bottom_percent = []
    a_bottom_path = []
    a_bottom_path_0 = []
    a_bottom_path_1 = []
    a_bottom_name = all_bottom['name'].tolist()
    a_bottom_en_name = change_to_en('all_bottom', 'in', '')
    a_bottom_price = all_bottom['avg_price'].tolist()
    a_bottom_before = all_bottom['day_before'].tolist()
    a_bottom_percent = all_bottom['day_percent'].tolist()
    for i in a_bottom_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        a_bottom_path.append(str(result))
        a_bottom_path_0.append(str(result_0))
        a_bottom_path_1.append(str(result_1))

    t_top_name = []
    t_top_en_name = []
    t_top_price = []
    t_top_before = []
    t_top_percent = []
    t_top_path = []
    t_top_path_0 = []
    t_top_path_1 = []
    t_top_name = today_top['name'].tolist()
    t_top_en_name = change_to_en('today_top', 'in', '')
    t_top_price = today_top['avg_price'].tolist()
    t_top_before = today_top['day_before'].tolist()
    t_top_percent = today_top['day_percent'].tolist()
    for i in t_top_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_top_path.append(str(result))
        t_top_path_0.append(str(result_0))
        t_top_path_1.append(str(result_1))

    t_bottom_name = []
    t_bottom_en_name = []
    t_bottom_price = []
    t_bottom_before = []
    t_bottom_percent = []
    t_bottom_path = []
    t_bottom_path_0 = []
    t_bottom_path_1 = []
    t_bottom_name = today_bottom['name'].tolist()
    t_bottom_en_name = change_to_en('today_bottom', 'in', '')
    t_bottom_price = today_bottom['avg_price'].tolist()
    t_bottom_before = today_bottom['day_before'].tolist()
    t_bottom_percent = today_bottom['day_percent'].tolist()
    for i in t_bottom_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_bottom_path.append(str(result))
        t_bottom_path_0.append(str(result_0))
        t_bottom_path_1.append(str(result_1))

    t_all_name = []
    t_all_en_name = []
    t_all_price = []
    t_all_before = []
    t_all_befores = []
    t_all_volume = []
    t_all_date = []
    t_all_percent = []
    t_all_lank = []
    t_all_path = []
    t_all_path_0 = []
    t_all_path_1 = []
    t_all_name = today_all['name'].tolist()
    t_all_name_count = len(t_all_name)
    t_all_en_name = change_to_en('result', 'in', '')
    t_all_price = today_all['avg_price'].tolist()
    t_all_before = today_all['day_before'].tolist()
    t_all_befores = today_all['yn_before'].tolist()
    t_all_volume = today_all['volume'].tolist()
    t_all_date = today_all['datetime'].tolist()
    t_all_percent = today_all['day_percent'].tolist()
    t_all_lank = today_all['lank'].tolist()

    for i in t_all_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_all_path.append(str(result))
        t_all_path_0.append(str(result_0))
        t_all_path_1.append(str(result_1))

    return render_template('index_en.html', **locals())
######################################################################
@app.route('/tests/')
def tests():
    return render_template('demo_0.html')
######################################################################
@app.route('/result/<get_name>/')
def result(get_name):
    visit_count = get_visit()
    all_item, all_item_kr, all_item_en, all_path, all_path_0, all_path_1, all_type, all_type_kr, all_type_en = get_all_item()

    def find_path(name, types):
        if types == 'path':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path = all_path[i]
                    return path
        elif types == 'path_0':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_0 = all_path_0[i]
                    return path_0
        elif types == 'path_1':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_1 = all_path_1[i]
                    return path_1

    if get_name not in all_item_kr:
        return redirect('/error/')
    else:

        input_warframe = input_item('warframes')
        input_weapon = input_item('weapons')
        input_weapon_etc = input_item('weapons_etc')
        input_aura_mods = input_item('aura_mods')
        input_warframe_mods = input_item('warframe_mods')
        input_items_etc = input_item('items_etc')
        input_weapon_mods = input_item('weapon_mods')

        result_name = '%s' % get_name
        for i, v in enumerate(all_item_kr):
            if str(v) == result_name:
                result_name = all_item[i]
        name = result_name.replace('_set', '')

        name_set = name.replace(' ', '_')
        name_sets = name_set + '_set'

        for i, v in enumerate(all_item):
            if str(v) == result_name:
                kr_name = all_item_kr[i]

        for i in input_weapon_etc:
            if str(name) in i:
                name_sets = name

        for i in input_aura_mods:
            if str(name) in i:
                name_sets = name

        for i in input_warframe_mods:
            if str(name) in i:
                name_sets = name

        for i in input_items_etc:
            if str(name) in i:
                name_sets = name

        for i in input_weapon_mods:
            if str(name) in i:
                name_sets = name

        search_path = find_path(name_sets, 'path')
        search_path_0 = find_path(name_sets, 'path_0')
        search_path_1 = find_path(name_sets, 'path_1')

        get_find = False
        is_warframe = False
        is_weapon = False
        is_weapon_etc = False
        is_aura_mods = False
        is_warframe_mods = False
        is_items_etc = False
        is_weapon_mods = False

        if get_find == False:
            for finds in input_warframe:
                if name in finds:
                    result = read_csv(name, 'warframe')
                    get_find = True
                    is_warframe = True
                    break

        if get_find == False:
            for finds in input_weapon:
                if name in finds:
                    result = read_csv(name, 'weapon')
                    get_find = True
                    is_weapon = True
                    break

        if get_find == False:
            for finds in input_weapon_etc:
                if name in finds:
                    result = read_csv(name, 'weapon_etc')
                    get_find = True
                    is_weapon_etc = True
                    break

        if get_find == False:
            for finds in input_aura_mods:
                if name in finds:
                    result = read_csv(name, 'aura_mods')
                    get_find = True
                    is_aura_mods = True
                    break

        if get_find == False:
            for finds in input_warframe_mods:
                if name in finds:
                    result = read_csv(name, 'warframe_mods')
                    get_find = True
                    is_aura_mods = True
                    break

        if get_find == False:
            for finds in input_items_etc:
                if name in finds:
                    result = read_csv(name, 'items_etc')
                    get_find = True
                    is_items_etc = True
                    break

        if get_find == False:
            for finds in input_weapon_mods:
                if name in finds:
                    result = read_csv(name, 'weapon_mods')
                    get_find = True
                    is_items_etc = True
                    break

        if(is_warframe == False and is_weapon == False and is_weapon_etc == False and is_aura_mods == False and is_warframe_mods == False and is_items_etc == False and is_weapon_mods):
            return redirect('/error/')

        if get_find == True:
            if(result.empty != True):

                today_datetime = get_today_date()

                label = 'market'
                xlabels = []
                dataset = []
                xlabels = result['datetime'].tolist()
                xlabels.reverse()
                dataset = result['avg_price'].tolist()
                dataset.reverse()

                all_datetime = result['datetime'].tolist()
                all_price = result['avg_price'].tolist()
                all_volume = result['volume'].tolist()
                all_day_before = result['day_before'].tolist()
                all_yn_before = result['yn_before'].tolist()
                all_day_percent = result['day_percent'].tolist()
                all_count = len(all_datetime)
                all_lank = result['lank'].tolist()

                return render_template('result.html', **locals())
            else:
                return redirect('/error/')
######################################################################
@app.route('/en/result/<get_name>/')
def result_en(get_name):
    visit_count = get_visit()
    all_item, all_item_kr, all_item_en, all_path, all_path_0, all_path_1, all_type, all_type_kr, all_type_en = get_all_item()

    def find_path(name, types):
        if types == 'path':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path = all_path[i]
                    return path
        elif types == 'path_0':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_0 = all_path_0[i]
                    return path_0
        elif types == 'path_1':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_1 = all_path_1[i]
                    return path_1

    if get_name not in all_item_en:
        return redirect('/error/')
    else:

        input_warframe = input_item('warframes')
        input_weapon = input_item('weapons')
        input_weapon_etc = input_item('weapons_etc')
        input_aura_mods = input_item('aura_mods')
        input_warframe_mods = input_item('warframe_mods')
        input_items_etc = input_item('items_etc')
        input_weapon_mods = input_item('weapon_mods')

        result_name = '%s' % get_name
        for i, v in enumerate(all_item_en):
            if str(v) == result_name:
                result_name = all_item[i]
        name = result_name.replace('_set', '')

        name_set = name.replace(' ', '_')
        name_sets = name_set + '_set'

        for i, v in enumerate(all_item):
            if str(v) == result_name:
                en_name = all_item_en[i]

        for i in input_weapon_etc:
            if str(name) in i:
                name_sets = name

        for i in input_aura_mods:
            if str(name) in i:
                name_sets = name

        for i in input_warframe_mods:
            if str(name) in i:
                name_sets = name

        for i in input_items_etc:
            if str(name) in i:
                name_sets = name

        for i in input_weapon_mods:
            if str(name) in i:
                name_sets = name

        search_path = find_path(name_sets, 'path')
        search_path_0 = find_path(name_sets, 'path_0')
        search_path_1 = find_path(name_sets, 'path_1')

        get_find = False
        is_warframe = False
        is_weapon = False
        is_weapon_etc = False
        is_aura_mods = False
        is_warframe_mods = False
        is_items_etc = False
        is_weapon_mods = False

        if get_find == False:
            for finds in input_warframe:
                if name in finds:
                    result = read_csv(name, 'warframe')
                    get_find = True
                    is_warframe = True
                    break

        if get_find == False:
            for finds in input_weapon:
                if name in finds:
                    result = read_csv(name, 'weapon')
                    get_find = True
                    is_weapon = True
                    break

        if get_find == False:
            for finds in input_weapon_etc:
                if name in finds:
                    result = read_csv(name, 'weapon_etc')
                    get_find = True
                    is_weapon_etc = True
                    break

        if get_find == False:
            for finds in input_aura_mods:
                if name in finds:
                    result = read_csv(name, 'aura_mods')
                    get_find = True
                    is_aura_mods = True
                    break

        if get_find == False:
            for finds in input_warframe_mods:
                if name in finds:
                    result = read_csv(name, 'warframe_mods')
                    get_find = True
                    is_aura_mods = True
                    break

        if get_find == False:
            for finds in input_items_etc:
                if name in finds:
                    result = read_csv(name, 'items_etc')
                    get_find = True
                    is_items_etc = True
                    break

        if get_find == False:
            for finds in input_weapon_mods:
                if name in finds:
                    result = read_csv(name, 'weapon_mods')
                    get_find = True
                    is_items_etc = True
                    break

        if(is_warframe == False and is_weapon == False and is_weapon_etc == False and is_aura_mods == False and is_warframe_mods == False and is_items_etc == False and is_weapon_mods):
            return redirect('/error/')

        if get_find == True:
            if(result.empty != True):

                today_datetime = get_today_date()

                label = 'market'
                xlabels = []
                dataset = []
                xlabels = result['datetime'].tolist()
                xlabels.reverse()
                dataset = result['avg_price'].tolist()
                dataset.reverse()

                all_datetime = result['datetime'].tolist()
                all_price = result['avg_price'].tolist()
                all_volume = result['volume'].tolist()
                all_day_before = result['day_before'].tolist()
                all_yn_before = result['yn_before'].tolist()
                all_day_percent = result['day_percent'].tolist()
                all_count = len(all_datetime)
                all_lank = result['lank'].tolist()

                return render_template('result_en.html', **locals())
            else:
                return redirect('/error/')
#####################################################################
@app.route('/result/download/<get_name>/')
def csv_file_download(get_name):

    all_item, all_item_kr, all_item_en, all_path, all_path_0, all_path_1, all_type, all_type_kr, all_type_en = get_all_item()

    def find_path(name, types):
        if types == 'path':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path = all_path[i]
                    return path
        elif types == 'path_0':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_0 = all_path_0[i]
                    return path_0
        elif types == 'path_1':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_1 = all_path_1[i]
                    return path_1

    if get_name not in all_item_kr:
        return redirect('/error/')
    else:

        input_warframe = input_item('warframes')
        input_weapon = input_item('weapons')
        input_weapon_etc = input_item('weapons_etc')
        input_aura_mods = input_item('aura_mods')
        input_warframe_mods = input_item('warframe_mods')
        input_items_etc = input_item('items_etc')
        input_weapon_mods = input_item('weapon_mods')

        result_name = '%s' % get_name
        for i, v in enumerate(all_item_kr):
            if str(v) == result_name:
                result_name = all_item[i]
        name = result_name.replace('_set', '')

        name_set = name.replace(' ', '_')
        name_sets = name_set + '_set'

        for i, v in enumerate(all_item):
            if str(v) == result_name:
                kr_name = all_item_kr[i]

        for i in input_weapon_etc:
            if str(name) in i:
                name_sets = name

        for i in input_aura_mods:
            if str(name) in i:
                name_sets = name

        for i in input_warframe_mods:
            if str(name) in i:
                name_sets = name

        for i in input_items_etc:
            if str(name) in i:
                name_sets = name

        for i in input_weapon_mods:
            if str(name) in i:
                name_sets = name

        search_path = find_path(name_sets, 'path')
        search_path_0 = find_path(name_sets, 'path_0')
        search_path_1 = find_path(name_sets, 'path_1')

        get_find = False
        is_warframe = False
        is_weapon = False
        is_weapon_etc = False
        is_aura_mods = False
        is_warframe_mods = False
        is_items_etc = False
        is_weapon_mods = False

        if get_find == False:
            for finds in input_warframe:
                if name in finds:
                    result = read_csv(name, 'warframe')
                    get_find = True
                    is_warframe = True
                    break

        if get_find == False:
            for finds in input_weapon:
                if name in finds:
                    result = read_csv(name, 'weapon')
                    get_find = True
                    is_weapon = True
                    break

        if get_find == False:
            for finds in input_weapon_etc:
                if name in finds:
                    result = read_csv(name, 'weapon_etc')
                    get_find = True
                    is_weapon_etc = True
                    break

        if get_find == False:
            for finds in input_aura_mods:
                if name in finds:
                    result = read_csv(name, 'aura_mods')
                    get_find = True
                    is_aura_mods = True
                    break

        if get_find == False:
            for finds in input_warframe_mods:
                if name in finds:
                    result = read_csv(name, 'warframe_mods')
                    get_find = True
                    is_aura_mods = True
                    break

        if get_find == False:
            for finds in input_items_etc:
                if name in finds:
                    result = read_csv(name, 'items_etc')
                    get_find = True
                    is_items_etc = True
                    break

        if get_find == False:
            for finds in input_weapon_mods:
                if name in finds:
                    result = read_csv(name, 'weapon_mods')
                    get_find = True
                    is_items_etc = True
                    break

        if(is_warframe == False and is_weapon == False and is_weapon_etc == False and is_aura_mods == False and is_warframe_mods == False and is_items_etc == False and is_weapon_mods):
            return redirect('/error/')

        if get_find == True:
            if(result.empty != True):

                today_datetime = get_today_date()

                result = result.reset_index()
                del result['index']
                del result['lank']
                del result['level_0']
                result = result[['datetime', 'avg_price', 'yn_before', 'day_before', 'day_percent', 'volume']]
                result = result.rename(columns={'datetime': '날짜', 'avg_price': '가격', 'yn_before': '', 'day_before': '전일대비', 'day_percent': '퍼센트', 'volume': '거래량'})

                export_file = StringIO()
                result.to_csv(export_file)
                response = Response(
                    export_file.getvalue(), 
                    mimetype='text/csv', 
                    content_type='application/octet-stream',
                )
                file_name = str(name_sets) + "_" + str(today_datetime) + ".csv"
                str_value = "attachment; filename=" + file_name
                response.headers["Content-Disposition"] = str_value
                return response
            else:
                return redirect('/error/')
#####################################################################
@app.route('/error/')
def error():
    visit_count = get_visit()
    all_item, all_item_kr, all_item_en, all_path, all_path_0, all_path_1, all_type, all_type_kr, all_type_en = get_all_item()
    return render_template('error.html', **locals())

######################################################################

@app.route('/temp/')
def temp():
    visit_count = get_visit()
    all_item, all_item_kr, all_item_en, all_path, all_path_0, all_path_1, all_type, all_type_kr, all_type_en = get_all_item()

    return render_template('temp.html', **locals())

#=======================================================================#
@app.route('/category/')
def category():

    visit_count = get_visit()
    all_item, all_item_kr, all_item_en, all_path, all_path_0, all_path_1, all_type, all_type_kr, all_type_en = get_all_item()

    type_primary_item = []
    type_primary_item_kr = []
    type_primary_path = []
    type_primary_path_0 = []
    type_primary_path_1 = []
    type_primary_type = []
    type_primary_type_kr = []
    type_primary_price = []
    type_primary_percent = []
    type_primary_volume = []
    type_primary_len = 0

    type_secondary_item = []
    type_secondary_item_kr = []
    type_secondary_path = []
    type_secondary_path_0 = []
    type_secondary_path_1 = []
    type_secondary_type = []
    type_secondary_type_kr = []
    type_secondary_price = []
    type_secondary_percent = []
    type_secondary_volume = []
    type_secondary_len = 0

    type_melee_item = []
    type_melee_item_kr = []
    type_melee_path = []
    type_melee_path_0 = []
    type_melee_path_1 = []
    type_melee_type = []
    type_melee_type_kr = []
    type_melee_price = []
    type_melee_percent = []
    type_melee_volume = []
    type_melee_len = 0

    type_warframe_item = []
    type_warframe_item_kr = []
    type_warframe_path = []
    type_warframe_path_0 = []
    type_warframe_path_1 = []
    type_warframe_type = []
    type_warframe_type_kr = []
    type_warframe_price = []
    type_warframe_percent = []
    type_warframe_volume = []
    type_warframe_len = 0

    type_warframe_mod_item = []
    type_warframe_mod_item_kr = []
    type_warframe_mod_path = []
    type_warframe_mod_path_0 = []
    type_warframe_mod_path_1 = []
    type_warframe_mod_type = []
    type_warframe_mod_type_kr = []
    type_warframe_mod_price = []
    type_warframe_mod_percent = []
    type_warframe_mod_volume = []
    type_warframe_mod_len = 0

    type_arcane_item = []
    type_arcane_item_kr = []
    type_arcane_path = []
    type_arcane_path_0 = []
    type_arcane_path_1 = []
    type_arcane_type = []
    type_arcane_type_kr = []
    type_arcane_price = []
    type_arcane_percent = []
    type_arcane_volume = []
    type_arcane_len = 0

    type_etc_item = []
    type_etc_item_kr = []
    type_etc_path = []
    type_etc_path_0 = []
    type_etc_path_1 = []
    type_etc_type = []
    type_etc_type_kr = []
    type_etc_price = []
    type_etc_percent = []
    type_etc_volume = []
    type_etc_len = 0

    type_primary_mod_item = []
    type_primary_mod_item_kr = []
    type_primary_mod_path = []
    type_primary_mod_path_0 = []
    type_primary_mod_path_1 = []
    type_primary_mod_type = []
    type_primary_mod_type_kr = []
    type_primary_mod_price = []
    type_primary_mod_percent = []
    type_primary_mod_volume = []
    type_primary_mod_len = 0

    type_secondary_mod_item = []
    type_secondary_mod_item_kr = []
    type_secondary_mod_path = []
    type_secondary_mod_path_0 = []
    type_secondary_mod_path_1 = []
    type_secondary_mod_type = []
    type_secondary_mod_type_kr = []
    type_secondary_mod_price = []
    type_secondary_mod_percent = []
    type_secondary_mod_volume = []
    type_secondary_mod_len = 0

    type_melee_mod_item = []
    type_melee_mod_item_kr = []
    type_melee_mod_path = []
    type_melee_mod_path_0 = []
    type_melee_mod_path_1 = []
    type_melee_mod_type = []
    type_melee_mod_type_kr = []
    type_melee_mod_price = []
    type_melee_mod_percent = []
    type_melee_mod_volume = []
    type_melee_mod_len = 0

    def en_to_kr(item):
        for i, v in enumerate(item):
            if all_type_kr[i] == "주무기":
                type_primary_item.append(all_item[i])
                type_primary_item_kr.append(all_item_kr[i])
                type_primary_path.append(all_path[i])
                type_primary_path_0.append(all_path_0[i])
                type_primary_path_1.append(all_path_1[i])
                type_primary_type.append(all_type[i])
                type_primary_type_kr.append(all_type_kr[i])
            elif all_type_kr[i] == "보조무기":
                type_secondary_item.append(all_item[i])
                type_secondary_item_kr.append(all_item_kr[i])
                type_secondary_path.append(all_path[i])
                type_secondary_path_0.append(all_path_0[i])
                type_secondary_path_1.append(all_path_1[i])
                type_secondary_type.append(all_type[i])
                type_secondary_type_kr.append(all_type_kr[i])
            elif all_type_kr[i] == "근접무기":
                type_melee_item.append(all_item[i])
                type_melee_item_kr.append(all_item_kr[i])
                type_melee_path.append(all_path[i])
                type_melee_path_0.append(all_path_0[i])
                type_melee_path_1.append(all_path_1[i])
                type_melee_type.append(all_type[i])
                type_melee_type_kr.append(all_type_kr[i])
            elif all_type_kr[i] == "워프레임":
                type_warframe_item.append(all_item[i])
                type_warframe_item_kr.append(all_item_kr[i])
                type_warframe_path.append(all_path[i])
                type_warframe_path_0.append(all_path_0[i])
                type_warframe_path_1.append(all_path_1[i])
                type_warframe_type.append(all_type[i])
                type_warframe_type_kr.append(all_type_kr[i])
            elif all_type_kr[i] == "워프레임 모드":
                type_warframe_mod_item.append(all_item[i])
                type_warframe_mod_item_kr.append(all_item_kr[i])
                type_warframe_mod_path.append(all_path[i])
                type_warframe_mod_path_0.append(all_path_0[i])
                type_warframe_mod_path_1.append(all_path_1[i])
                type_warframe_mod_type.append(all_type[i])
                type_warframe_mod_type_kr.append(all_type_kr[i])
            elif all_type_kr[i] == "아케인":
                type_arcane_item.append(all_item[i])
                type_arcane_item_kr.append(all_item_kr[i])
                type_arcane_path.append(all_path[i])
                type_arcane_path_0.append(all_path_0[i])
                type_arcane_path_1.append(all_path_1[i])
                type_arcane_type.append(all_type[i])
                type_arcane_type_kr.append(all_type_kr[i])
            elif all_type_kr[i] == "주무기 모드":
                type_primary_mod_item.append(all_item[i])
                type_primary_mod_item_kr.append(all_item_kr[i])
                type_primary_mod_path.append(all_path[i])
                type_primary_mod_path_0.append(all_path_0[i])
                type_primary_mod_path_1.append(all_path_1[i])
                type_primary_mod_type.append(all_type[i])
                type_primary_mod_type_kr.append(all_type_kr[i])
            elif all_type_kr[i] == "보조무기 모드":
                type_secondary_mod_item.append(all_item[i])
                type_secondary_mod_item_kr.append(all_item_kr[i])
                type_secondary_mod_path.append(all_path[i])
                type_secondary_mod_path_0.append(all_path_0[i])
                type_secondary_mod_path_1.append(all_path_1[i])
                type_secondary_mod_type.append(all_type[i])
                type_secondary_mod_type_kr.append(all_type_kr[i])
            elif all_type_kr[i] == "근접무기 모드":
                type_melee_mod_item.append(all_item[i])
                type_melee_mod_item_kr.append(all_item_kr[i])
                type_melee_mod_path.append(all_path[i])
                type_melee_mod_path_0.append(all_path_0[i])
                type_melee_mod_path_1.append(all_path_1[i])
                type_melee_mod_type.append(all_type[i])
                type_melee_mod_type_kr.append(all_type_kr[i])
            elif all_type_kr[i] == "업데이트":
                type_etc_item.append(all_item[i])
                type_etc_item_kr.append(all_item_kr[i])
                type_etc_path.append(all_path[i])
                type_etc_path_0.append(all_path_0[i])
                type_etc_path_1.append(all_path_1[i])
                type_etc_type.append(all_type[i])
                type_etc_type_kr.append(all_type_kr[i])
            else:
                continue


    en_to_kr(all_item_kr)

    type_primary_len = len(type_primary_item)
    type_secondary_len = len(type_secondary_item)
    type_melee_len = len(type_melee_item)
    type_warframe_len = len(type_warframe_item)
    type_warframe_mod_len = len(type_warframe_mod_item)
    type_arcane_len = len(type_arcane_item)
    type_etc_len = len(type_etc_item)
    type_primary_mod_len = len(type_primary_mod_item)
    type_secondary_mod_len = len(type_secondary_mod_item)
    type_melee_mod_len = len(type_melee_mod_item)

    price_data = read_csv('result', 'result')
    price_name = price_data["name"].tolist()
    price_avg = price_data["avg_price"].tolist()
    price_percent = price_data["day_percent"].tolist()
    price_volume = price_data["volume"].tolist()

    today_item = []
    today_price = []
    today_percent = []
    today_volume = []

    for i, v in enumerate(all_item):
        if v in price_name:
            today_item.append(str(v))
        else:
            today_item.append(str("none"))

    for i, v in enumerate(today_item):
        if v in price_name:
            index = price_name.index(v)
            today_price.append(price_avg[index])
            today_percent.append(price_percent[index])
            today_volume.append(price_volume[index])
        elif v == "none":
            today_price.append(0)
            today_percent.append(0)
            today_volume.append(0)

    for i, v in enumerate(all_item):
        if v in type_primary_item:
            type_primary_price.append(today_price[i])
            type_primary_percent.append(today_percent[i])
            type_primary_volume.append(today_volume[i])
        if v in type_secondary_item:
            type_secondary_price.append(today_price[i])
            type_secondary_percent.append(today_percent[i])
            type_secondary_volume.append(today_volume[i])
        if v in type_melee_item:
            type_melee_price.append(today_price[i])
            type_melee_percent.append(today_percent[i])
            type_melee_volume.append(today_volume[i])
        if v in type_warframe_item:
            type_warframe_price.append(today_price[i])
            type_warframe_percent.append(today_percent[i])
            type_warframe_volume.append(today_volume[i])
        if v in type_warframe_mod_item:
            type_warframe_mod_price.append(today_price[i])
            type_warframe_mod_percent.append(today_percent[i])
            type_warframe_mod_volume.append(today_volume[i])
        if v in type_arcane_item:
            type_arcane_price.append(today_price[i])
            type_arcane_percent.append(today_percent[i])
            type_arcane_volume.append(today_volume[i])
        if v in type_etc_item:
            type_etc_price.append(today_price[i])
            type_etc_percent.append(today_percent[i])
            type_etc_volume.append(today_volume[i])
        if v in type_primary_mod_item:
            type_primary_mod_price.append(today_price[i])
            type_primary_mod_percent.append(today_percent[i])
            type_primary_mod_volume.append(today_volume[i])
        if v in type_secondary_mod_item:
            type_secondary_mod_price.append(today_price[i])
            type_secondary_mod_percent.append(today_percent[i])
            type_secondary_mod_volume.append(today_volume[i])
        if v in type_melee_mod_item:
            type_melee_mod_price.append(today_price[i])
            type_melee_mod_percent.append(today_percent[i])
            type_melee_mod_volume.append(today_volume[i])

    def sort_array(index, t_f, array_name, array_name_kr, array_price, array_percent, array_volume, array_path_1):
        value = {"name" : pd.Series(array_name), "kr_name" : pd.Series(array_name_kr), "price" : pd.Series(array_price), "percent" : pd.Series(array_percent), "volume" : pd.Series(array_volume), "path_1" : pd.Series(array_path_1)}
        today_data = pd.DataFrame(value)

        if t_f == "True":
            tf = True

        if t_f == "False":
            tf = False

        if index == "가격":
            today_data_1 = today_data.sort_values(by = 'price', ascending = tf)
            name1 = today_data_1['name'].tolist()
            kr_name1 = today_data_1['kr_name'].tolist()
            price1 = today_data_1['price'].tolist()
            path1 = today_data_1['path_1'].tolist()
            return name1, kr_name1, price1, path1
        if index == "퍼센트":
            today_data_2 = today_data.sort_values(by = 'percent', ascending = tf)
            name2 = today_data_2['name'].tolist()
            kr_name2 = today_data_2['kr_name'].tolist()
            percent2 = today_data_2['percent'].tolist()
            path2 = today_data_2['path_1'].tolist()
            return name2, kr_name2, percent2, path2
        if index == "거래량":
            today_data_3 = today_data.sort_values(by = 'volume', ascending = tf)
            name3 = today_data_3['name'].tolist()
            kr_name3 = today_data_3['kr_name'].tolist()
            volume3 = today_data_3['volume'].tolist()
            path3 = today_data_3['path_1'].tolist()
            return name3, kr_name3, volume3, path3

    type_primary_item_pr1, type_primary_item_kr_pr1, type_primary_price_pr1, type_primary_path_1_pr1 = sort_array("가격", "False", type_primary_item, type_primary_item_kr, type_primary_price, type_primary_percent, type_primary_volume, type_primary_path_1)
    type_primary_item_pr2, type_primary_item_kr_pr2, type_primary_price_pr2, type_primary_path_1_pr2 = sort_array("가격", "True", type_primary_item, type_primary_item_kr, type_primary_price, type_primary_percent, type_primary_volume, type_primary_path_1)
    type_primary_item_pe1, type_primary_item_kr_pe1, type_primary_percent_pe1, type_primary_path_1_pe1 = sort_array("퍼센트", "False", type_primary_item, type_primary_item_kr, type_primary_price, type_primary_percent, type_primary_volume, type_primary_path_1)
    type_primary_item_pe2, type_primary_item_kr_pe2, type_primary_percent_pe2, type_primary_path_1_pe2 = sort_array("퍼센트", "True", type_primary_item, type_primary_item_kr, type_primary_price, type_primary_percent, type_primary_volume, type_primary_path_1)
    type_primary_item_vo1, type_primary_item_kr_vo1, type_primary_volume_vo1, type_primary_path_1_vo1 = sort_array("거래량", "False", type_primary_item, type_primary_item_kr, type_primary_price, type_primary_percent, type_primary_volume, type_primary_path_1)
    type_primary_item_vo2, type_primary_item_kr_vo2, type_primary_volume_vo2, type_primary_path_1_vo2 = sort_array("거래량", "True", type_primary_item, type_primary_item_kr, type_primary_price, type_primary_percent, type_primary_volume, type_primary_path_1)
    
    type_secondary_item_pr1, type_secondary_item_kr_pr1, type_secondary_price_pr1, type_secondary_path_1_pr1 = sort_array("가격", "False", type_secondary_item, type_secondary_item_kr, type_secondary_price, type_secondary_percent, type_secondary_volume, type_secondary_path_1)
    type_secondary_item_pr2, type_secondary_item_kr_pr2, type_secondary_price_pr2, type_secondary_path_1_pr2 = sort_array("가격", "True", type_secondary_item, type_secondary_item_kr, type_secondary_price, type_secondary_percent, type_secondary_volume, type_secondary_path_1)
    type_secondary_item_pe1, type_secondary_item_kr_pe1, type_secondary_percent_pe1, type_secondary_path_1_pe1 = sort_array("퍼센트", "False", type_secondary_item, type_secondary_item_kr, type_secondary_price, type_secondary_percent, type_secondary_volume, type_secondary_path_1)
    type_secondary_item_pe2, type_secondary_item_kr_pe2, type_secondary_percent_pe2, type_secondary_path_1_pe2 = sort_array("퍼센트", "True", type_secondary_item, type_secondary_item_kr, type_secondary_price, type_secondary_percent, type_secondary_volume, type_secondary_path_1)
    type_secondary_item_vo1, type_secondary_item_kr_vo1, type_secondary_volume_vo1, type_secondary_path_1_vo1 = sort_array("거래량", "False", type_secondary_item, type_secondary_item_kr, type_secondary_price, type_secondary_percent, type_secondary_volume, type_secondary_path_1)
    type_secondary_item_vo2, type_secondary_item_kr_vo2, type_secondary_volume_vo2, type_secondary_path_1_vo2 = sort_array("거래량", "True", type_secondary_item, type_secondary_item_kr, type_secondary_price, type_secondary_percent, type_secondary_volume, type_secondary_path_1)
    
    type_melee_item_pr1, type_melee_item_kr_pr1, type_melee_price_pr1, type_melee_path_1_pr1 = sort_array("가격", "False", type_melee_item, type_melee_item_kr, type_melee_price, type_melee_percent, type_melee_volume, type_melee_path_1)
    type_melee_item_pr2, type_melee_item_kr_pr2, type_melee_price_pr2, type_melee_path_1_pr2 = sort_array("가격", "True", type_melee_item, type_melee_item_kr, type_melee_price, type_melee_percent, type_melee_volume, type_melee_path_1)
    type_melee_item_pe1, type_melee_item_kr_pe1, type_melee_percent_pe1, type_melee_path_1_pe1 = sort_array("퍼센트", "False", type_melee_item, type_melee_item_kr, type_melee_price, type_melee_percent, type_melee_volume, type_melee_path_1)
    type_melee_item_pe2, type_melee_item_kr_pe2, type_melee_percent_pe2, type_melee_path_1_pe2 = sort_array("퍼센트", "True", type_melee_item, type_melee_item_kr, type_melee_price, type_melee_percent, type_melee_volume, type_melee_path_1)
    type_melee_item_vo1, type_melee_item_kr_vo1, type_melee_volume_vo1, type_melee_path_1_vo1 = sort_array("거래량", "False", type_melee_item, type_melee_item_kr, type_melee_price, type_melee_percent, type_melee_volume, type_melee_path_1)
    type_melee_item_vo2, type_melee_item_kr_vo2, type_melee_volume_vo2, type_melee_path_1_vo2 = sort_array("거래량", "True", type_melee_item, type_melee_item_kr, type_melee_price, type_melee_percent, type_melee_volume, type_melee_path_1)
    
    type_warframe_item_pr1, type_warframe_item_kr_pr1, type_warframe_price_pr1, type_warframe_path_1_pr1 = sort_array("가격", "False", type_warframe_item, type_warframe_item_kr, type_warframe_price, type_warframe_percent, type_warframe_volume, type_warframe_path_1)
    type_warframe_item_pr2, type_warframe_item_kr_pr2, type_warframe_price_pr2, type_warframe_path_1_pr2 = sort_array("가격", "True", type_warframe_item, type_warframe_item_kr, type_warframe_price, type_warframe_percent, type_warframe_volume, type_warframe_path_1)
    type_warframe_item_pe1, type_warframe_item_kr_pe1, type_warframe_percent_pe1, type_warframe_path_1_pe1 = sort_array("퍼센트", "False", type_warframe_item, type_warframe_item_kr, type_warframe_price, type_warframe_percent, type_warframe_volume, type_warframe_path_1)
    type_warframe_item_pe2, type_warframe_item_kr_pe2, type_warframe_percent_pe2, type_warframe_path_1_pe2 = sort_array("퍼센트", "True", type_warframe_item, type_warframe_item_kr, type_warframe_price, type_warframe_percent, type_warframe_volume, type_warframe_path_1)
    type_warframe_item_vo1, type_warframe_item_kr_vo1, type_warframe_volume_vo1, type_warframe_path_1_vo1 = sort_array("거래량", "False", type_warframe_item, type_warframe_item_kr, type_warframe_price, type_warframe_percent, type_warframe_volume, type_warframe_path_1)
    type_warframe_item_vo2, type_warframe_item_kr_vo2, type_warframe_volume_vo2, type_warframe_path_1_vo2 = sort_array("거래량", "True", type_warframe_item, type_warframe_item_kr, type_warframe_price, type_warframe_percent, type_warframe_volume, type_warframe_path_1)
    
    type_warframe_mod_item_pr1, type_warframe_mod_item_kr_pr1, type_warframe_mod_price_pr1, type_warframe_mod_path_1_pr1 = sort_array("가격", "False", type_warframe_mod_item, type_warframe_mod_item_kr, type_warframe_mod_price, type_warframe_mod_percent, type_warframe_mod_volume, type_warframe_mod_path_1)
    type_warframe_mod_item_pr2, type_warframe_mod_item_kr_pr2, type_warframe_mod_price_pr2, type_warframe_mod_path_1_pr2 = sort_array("가격", "True", type_warframe_mod_item, type_warframe_mod_item_kr, type_warframe_mod_price, type_warframe_mod_percent, type_warframe_mod_volume, type_warframe_mod_path_1)
    type_warframe_mod_item_pe1, type_warframe_mod_item_kr_pe1, type_warframe_mod_percent_pe1, type_warframe_mod_path_1_pe1 = sort_array("퍼센트", "False", type_warframe_mod_item, type_warframe_mod_item_kr, type_warframe_mod_price, type_warframe_mod_percent, type_warframe_mod_volume, type_warframe_mod_path_1)
    type_warframe_mod_item_pe2, type_warframe_mod_item_kr_pe2, type_warframe_mod_percent_pe2, type_warframe_mod_path_1_pe2 = sort_array("퍼센트", "True", type_warframe_mod_item, type_warframe_mod_item_kr, type_warframe_mod_price, type_warframe_mod_percent, type_warframe_mod_volume, type_warframe_mod_path_1)
    type_warframe_mod_item_vo1, type_warframe_mod_item_kr_vo1, type_warframe_mod_volume_vo1, type_warframe_mod_path_1_vo1 = sort_array("거래량", "False", type_warframe_mod_item, type_warframe_mod_item_kr, type_warframe_mod_price, type_warframe_mod_percent, type_warframe_mod_volume, type_warframe_mod_path_1)
    type_warframe_mod_item_vo2, type_warframe_mod_item_kr_vo2, type_warframe_mod_volume_vo2, type_warframe_mod_path_1_vo2 = sort_array("거래량", "True", type_warframe_mod_item, type_warframe_mod_item_kr, type_warframe_mod_price, type_warframe_mod_percent, type_warframe_mod_volume, type_warframe_mod_path_1)
    
    type_arcane_item_pr1, type_arcane_item_kr_pr1, type_arcane_price_pr1, type_arcane_path_1_pr1 = sort_array("가격", "False", type_arcane_item, type_arcane_item_kr, type_arcane_price, type_arcane_percent, type_arcane_volume, type_arcane_path_1)
    type_arcane_item_pr2, type_arcane_item_kr_pr2, type_arcane_price_pr2, type_arcane_path_1_pr2 = sort_array("가격", "True", type_arcane_item, type_arcane_item_kr, type_arcane_price, type_arcane_percent, type_arcane_volume, type_arcane_path_1)
    type_arcane_item_pe1, type_arcane_item_kr_pe1, type_arcane_percent_pe1, type_arcane_path_1_pe1 = sort_array("퍼센트", "False", type_arcane_item, type_arcane_item_kr, type_arcane_price, type_arcane_percent, type_arcane_volume, type_arcane_path_1)
    type_arcane_item_pe2, type_arcane_item_kr_pe2, type_arcane_percent_pe2, type_arcane_path_1_pe2 = sort_array("퍼센트", "True", type_arcane_item, type_arcane_item_kr, type_arcane_price, type_arcane_percent, type_arcane_volume, type_arcane_path_1)
    type_arcane_item_vo1, type_arcane_item_kr_vo1, type_arcane_volume_vo1, type_arcane_path_1_vo1 = sort_array("거래량", "False", type_arcane_item, type_arcane_item_kr, type_arcane_price, type_arcane_percent, type_arcane_volume, type_arcane_path_1)
    type_arcane_item_vo2, type_arcane_item_kr_vo2, type_arcane_volume_vo2, type_arcane_path_1_vo2 = sort_array("거래량", "True", type_arcane_item, type_arcane_item_kr, type_arcane_price, type_arcane_percent, type_arcane_volume, type_arcane_path_1)
    
    type_primary_mod_item_pr1, type_primary_mod_item_kr_pr1, type_primary_mod_price_pr1, type_primary_mod_path_1_pr1 = sort_array("가격", "False", type_primary_mod_item, type_primary_mod_item_kr, type_primary_mod_price, type_primary_mod_percent, type_primary_mod_volume, type_primary_mod_path_1)
    type_primary_mod_item_pr2, type_primary_mod_item_kr_pr2, type_primary_mod_price_pr2, type_primary_mod_path_1_pr2 = sort_array("가격", "True", type_primary_mod_item, type_primary_mod_item_kr, type_primary_mod_price, type_primary_mod_percent, type_primary_mod_volume, type_primary_mod_path_1)
    type_primary_mod_item_pe1, type_primary_mod_item_kr_pe1, type_primary_mod_percent_pe1, type_primary_mod_path_1_pe1 = sort_array("퍼센트", "False", type_primary_mod_item, type_primary_mod_item_kr, type_primary_mod_price, type_primary_mod_percent, type_primary_mod_volume, type_primary_mod_path_1)
    type_primary_mod_item_pe2, type_primary_mod_item_kr_pe2, type_primary_mod_percent_pe2, type_primary_mod_path_1_pe2 = sort_array("퍼센트", "True", type_primary_mod_item, type_primary_mod_item_kr, type_primary_mod_price, type_primary_mod_percent, type_primary_mod_volume, type_primary_mod_path_1)
    type_primary_mod_item_vo1, type_primary_mod_item_kr_vo1, type_primary_mod_volume_vo1, type_primary_mod_path_1_vo1 = sort_array("거래량", "False", type_primary_mod_item, type_primary_mod_item_kr, type_primary_mod_price, type_primary_mod_percent, type_primary_mod_volume, type_primary_mod_path_1)
    type_primary_mod_item_vo2, type_primary_mod_item_kr_vo2, type_primary_mod_volume_vo2, type_primary_mod_path_1_vo2 = sort_array("거래량", "True", type_primary_mod_item, type_primary_mod_item_kr, type_primary_mod_price, type_primary_mod_percent, type_primary_mod_volume, type_primary_mod_path_1)
    
    type_secondary_mod_item_pr1, type_secondary_mod_item_kr_pr1, type_secondary_mod_price_pr1, type_secondary_mod_path_1_pr1 = sort_array("가격", "False", type_secondary_mod_item, type_secondary_mod_item_kr, type_secondary_mod_price, type_secondary_mod_percent, type_secondary_mod_volume, type_secondary_mod_path_1)
    type_secondary_mod_item_pr2, type_secondary_mod_item_kr_pr2, type_secondary_mod_price_pr2, type_secondary_mod_path_1_pr2 = sort_array("가격", "True", type_secondary_mod_item, type_secondary_mod_item_kr, type_secondary_mod_price, type_secondary_mod_percent, type_secondary_mod_volume, type_secondary_mod_path_1)
    type_secondary_mod_item_pe1, type_secondary_mod_item_kr_pe1, type_secondary_mod_percent_pe1, type_secondary_mod_path_1_pe1 = sort_array("퍼센트", "False", type_secondary_mod_item, type_secondary_mod_item_kr, type_secondary_mod_price, type_secondary_mod_percent, type_secondary_mod_volume, type_secondary_mod_path_1)
    type_secondary_mod_item_pe2, type_secondary_mod_item_kr_pe2, type_secondary_mod_percent_pe2, type_secondary_mod_path_1_pe2 = sort_array("퍼센트", "True", type_secondary_mod_item, type_secondary_mod_item_kr, type_secondary_mod_price, type_secondary_mod_percent, type_secondary_mod_volume, type_secondary_mod_path_1)
    type_secondary_mod_item_vo1, type_secondary_mod_item_kr_vo1, type_secondary_mod_volume_vo1, type_secondary_mod_path_1_vo1 = sort_array("거래량", "False", type_secondary_mod_item, type_secondary_mod_item_kr, type_secondary_mod_price, type_secondary_mod_percent, type_secondary_mod_volume, type_secondary_mod_path_1)
    type_secondary_mod_item_vo2, type_secondary_mod_item_kr_vo2, type_secondary_mod_volume_vo2, type_secondary_mod_path_1_vo2 = sort_array("거래량", "True", type_secondary_mod_item, type_secondary_mod_item_kr, type_secondary_mod_price, type_secondary_mod_percent, type_secondary_mod_volume, type_secondary_mod_path_1)

    type_melee_mod_item_pr1, type_melee_mod_item_kr_pr1, type_melee_mod_price_pr1, type_melee_mod_path_1_pr1 = sort_array("가격", "False", type_melee_mod_item, type_melee_mod_item_kr, type_melee_mod_price, type_melee_mod_percent, type_melee_mod_volume, type_melee_mod_path_1)
    type_melee_mod_item_pr2, type_melee_mod_item_kr_pr2, type_melee_mod_price_pr2, type_melee_mod_path_1_pr2 = sort_array("가격", "True", type_melee_mod_item, type_melee_mod_item_kr, type_melee_mod_price, type_melee_mod_percent, type_melee_mod_volume, type_melee_mod_path_1)
    type_melee_mod_item_pe1, type_melee_mod_item_kr_pe1, type_melee_mod_percent_pe1, type_melee_mod_path_1_pe1 = sort_array("퍼센트", "False", type_melee_mod_item, type_melee_mod_item_kr, type_melee_mod_price, type_melee_mod_percent, type_melee_mod_volume, type_melee_mod_path_1)
    type_melee_mod_item_pe2, type_melee_mod_item_kr_pe2, type_melee_mod_percent_pe2, type_melee_mod_path_1_pe2 = sort_array("퍼센트", "True", type_melee_mod_item, type_melee_mod_item_kr, type_melee_mod_price, type_melee_mod_percent, type_melee_mod_volume, type_melee_mod_path_1)
    type_melee_mod_item_vo1, type_melee_mod_item_kr_vo1, type_melee_mod_volume_vo1, type_melee_mod_path_1_vo1 = sort_array("거래량", "False", type_melee_mod_item, type_melee_mod_item_kr, type_melee_mod_price, type_melee_mod_percent, type_melee_mod_volume, type_melee_mod_path_1)
    type_melee_mod_item_vo2, type_melee_mod_item_kr_vo2, type_melee_mod_volume_vo2, type_melee_mod_path_1_vo2 = sort_array("거래량", "True", type_melee_mod_item, type_melee_mod_item_kr, type_melee_mod_price, type_melee_mod_percent, type_melee_mod_volume, type_melee_mod_path_1)

    type_etc_item_pr1, type_etc_item_kr_pr1, type_etc_price_pr1, type_etc_path_1_pr1 = sort_array("가격", "False", type_etc_item, type_etc_item_kr, type_etc_price, type_etc_percent, type_etc_volume, type_etc_path_1)
    type_etc_item_pr2, type_etc_item_kr_pr2, type_etc_price_pr2, type_etc_path_1_pr2 = sort_array("가격", "True", type_etc_item, type_etc_item_kr, type_etc_price, type_etc_percent, type_etc_volume, type_etc_path_1)
    type_etc_item_pe1, type_etc_item_kr_pe1, type_etc_percent_pe1, type_etc_path_1_pe1 = sort_array("퍼센트", "False", type_etc_item, type_etc_item_kr, type_etc_price, type_etc_percent, type_etc_volume, type_etc_path_1)
    type_etc_item_pe2, type_etc_item_kr_pe2, type_etc_percent_pe2, type_etc_path_1_pe2 = sort_array("퍼센트", "True", type_etc_item, type_etc_item_kr, type_etc_price, type_etc_percent, type_etc_volume, type_etc_path_1)
    type_etc_item_vo1, type_etc_item_kr_vo1, type_etc_volume_vo1, type_etc_path_1_vo1 = sort_array("거래량", "False", type_etc_item, type_etc_item_kr, type_etc_price, type_etc_percent, type_etc_volume, type_etc_path_1)
    type_etc_item_vo2, type_etc_item_kr_vo2, type_etc_volume_vo2, type_etc_path_1_vo2 = sort_array("거래량", "True", type_etc_item, type_etc_item_kr, type_etc_price, type_etc_percent, type_etc_volume, type_etc_path_1)

    #test = {"name" : pd.Series(all_item), "price" : pd.Series(today_price)}
    #test_data = pd.DataFrame(test)
    #test_data.to_excel('test.xlsx')

    path = '/workspace/crawling/data/json/recommend_0.json'
    with open(path, "r", encoding="UTF-8") as json_file:
        json_data = json.load(json_file, strict = False)
        json_datas = json.dumps(json_data, ensure_ascii=False)

    rec_index_0 = []
    rec_index_number_0 = []
    rec_image_0 = []
    rec_subject_0 = []
    rec_name_0 = []
    rec_type_0 = []
    rec_en_name_0 = []
    rec_kr_name_0 = []
    rec_price_0 = []
    rec_percent_0 = []
    rec_volume_0 = []

    rec_len_data_0 = len(json_data["recommend"])

    for i in json_data["recommend"]:
        rec_index_0.append(i["index"])
        rec_index_number_0.append(i["index_number"])
        rec_image_0.append(i["image"])
        rec_subject_0.append(i["subject"])
        rec_name_0.append(i["name"])
        rec_type_0.append(i["type"])
        rec_en_name_0.append(i["en_name"])
        rec_kr_name_0.append(i["kr_name"])

    for i in range(0, rec_len_data_0):
        index = rec_index_number_0[i]
        rec_price_0.append(today_price[index])
        rec_percent_0.append(today_percent[index])
        rec_volume_0.append(today_volume[index])

    rec_name_0_pr1, rec_kr_name_0_pr1, rec_price_0_pr1, rec_image_0_pr1 = sort_array("가격", "False", rec_name_0, rec_kr_name_0, rec_price_0, rec_percent_0, rec_volume_0, rec_image_0)
    rec_name_0_pr2, rec_kr_name_0_pr2, rec_price_0_pr2, rec_image_0_pr2 = sort_array("가격", "True", rec_name_0, rec_kr_name_0, rec_price_0, rec_percent_0, rec_volume_0, rec_image_0)
    rec_name_0_pe1, rec_kr_name_0_pe1, rec_percent_0_pe1, rec_image_0_pe1 = sort_array("퍼센트", "False", rec_name_0, rec_kr_name_0, rec_price_0, rec_percent_0, rec_volume_0, rec_image_0)
    rec_name_0_pe2, rec_kr_name_0_pe2, rec_percent_0_pe2, rec_image_0_pe2 = sort_array("퍼센트", "True", rec_name_0, rec_kr_name_0, rec_price_0, rec_percent_0, rec_volume_0, rec_image_0)
    rec_name_0_vo1, rec_kr_name_0_vo1, rec_volume_0_vo1, rec_image_0_vo1 = sort_array("거래량", "False", rec_name_0, rec_kr_name_0, rec_price_0, rec_percent_0, rec_volume_0, rec_image_0)
    rec_name_0_vo2, rec_kr_name_0_vo2, rec_volume_0_vo2, rec_image_0_vo2 = sort_array("거래량", "True", rec_name_0, rec_kr_name_0, rec_price_0, rec_percent_0, rec_volume_0, rec_image_0)

    return render_template('category.html', **locals())

###########################################################################

@app.route('/calculator/<get_name>/', methods=['GET', 'POST'])
def calculator(get_name):

    visit_count = get_visit()
    all_item, all_item_kr, all_item_en, all_path, all_path_0, all_path_1, all_type, all_type_kr, all_type_en = get_all_item()

    def find_path(name, types):
        if types == 'path':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path = all_path[i]
                    return path
        elif types == 'path_0':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_0 = all_path_0[i]
                    return path_0
        elif types == 'path_1':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_1 = all_path_1[i]
                    return path_1

    if get_name not in all_item_kr:
        return redirect('/error/')
    else:

        input_warframe = input_item('warframes')
        input_weapon = input_item('weapons')
        input_weapon_etc = input_item('weapons_etc')
        input_aura_mods = input_item('aura_mods')
        input_warframe_mods = input_item('warframe_mods')
        input_items_etc = input_item('items_etc')
        input_weapon_mods = input_item('weapon_mods')

        result_name = '%s' % get_name
        for i, v in enumerate(all_item_kr):
            if str(v) == result_name:
                result_name = all_item[i]
        name = result_name.replace('_set', '')

        name_set = name.replace(' ', '_')
        name_sets = name_set + '_set'

        for i, v in enumerate(all_item):
            if str(v) == result_name:
                kr_name = all_item_kr[i]

        for i in input_weapon_etc:
            if str(name) in i:
                name_sets = name

        for i in input_aura_mods:
            if str(name) in i:
                name_sets = name

        for i in input_warframe_mods:
            if str(name) in i:
                name_sets = name

        for i in input_items_etc:
            if str(name) in i:
                name_sets = name

        for i in input_weapon_mods:
            if str(name) in i:
                name_sets = name

        search_path = find_path(name_sets, 'path')
        search_path_0 = find_path(name_sets, 'path_0')
        search_path_1 = find_path(name_sets, 'path_1')

        get_find = False
        is_warframe = False
        is_weapon = False
        is_weapon_etc = False
        is_aura_mods = False
        is_warframe_mods = False
        is_items_etc = False
        is_weapon_mods = False

        if get_find == False:
            for finds in input_warframe:
                if name in finds:
                    result = read_csv(name, 'warframe')
                    get_find = True
                    is_warframe = True
                    break

        if get_find == False:
            for finds in input_weapon:
                if name in finds:
                    result = read_csv(name, 'weapon')
                    get_find = True
                    is_weapon = True
                    break

        if get_find == False:
            for finds in input_weapon_etc:
                if name in finds:
                    result = read_csv(name, 'weapon_etc')
                    get_find = True
                    is_weapon_etc = True
                    break

        if get_find == False:
            for finds in input_aura_mods:
                if name in finds:
                    result = read_csv(name, 'aura_mods')
                    get_find = True
                    is_aura_mods = True
                    break

        if get_find == False:
            for finds in input_warframe_mods:
                if name in finds:
                    result = read_csv(name, 'warframe_mods')
                    get_find = True
                    is_aura_mods = True
                    break

        if get_find == False:
            for finds in input_items_etc:
                if name in finds:
                    result = read_csv(name, 'items_etc')
                    get_find = True
                    is_items_etc = True
                    break

        if get_find == False:
            for finds in input_weapon_mods:
                if name in finds:
                    result = read_csv(name, 'weapon_mods')
                    get_find = True
                    is_items_etc = True
                    break

        if(is_warframe == False and is_weapon == False and is_weapon_etc == False and is_aura_mods == False and is_warframe_mods == False and is_items_etc == False and is_weapon_mods):
            return redirect('/error/')

        if get_find == True:
            if(result.empty != True):

                today_datetime = get_today_date()
                min_date = str(result['datetime'][0])
                max_date = str(result['datetime'][len(result) - 1])
                input_first_date = '시작일'
                input_second_date = '종료일'
                min_price = 0
                max_price = 0
                input_cash = 0
                input_count = 0
                input_count_0 = 0
                cal_price_0 = 0 #지불한 플레티넘
                cal_price_1 = 0 #지불후 남는 플레티넘
                cal_price_2 = 0 #개당 이윤
                cal_price_3 = 0 #총 이윤
                cal_price_4 = 0 #최종 소지 플레티넘
                cal_percent = 0 #이윤 퍼센트

                all_datetime = result['datetime'].tolist()
                all_price = result['avg_price'].tolist()
                all_volume = result['volume'].tolist()
                all_day_before = result['day_before'].tolist()
                all_yn_before = result['yn_before'].tolist()
                all_day_percent = result['day_percent'].tolist()
                all_count = len(all_datetime)

                label = 'market'
                xlabels = []
                dataset = []
                xlabels = result['datetime'].tolist()
                xlabels.reverse()
                dataset = result['avg_price'].tolist()
                dataset.reverse()

                dataset_1 = []
                for i in range (0, all_count):
                    dataset_1.append(0)

                if request.method == 'POST':
                    post_result = request.form
                    names = []
                    values = []
                    for name, value in post_result.items():
                        names.append(name)
                        values.append(value)
                    tf = values[2].isdigit()
                    #print(values)
                    if tf == False or values[0] == '' or values[1] == '':
                        return redirect('/error/')
                    if int(values[3]) == 0:
                        input_first_date = str(values[0])
                        input_second_date = str(values[1])
                        if datetime.datetime.strptime(values[1], '%Y-%m-%d') >= datetime.datetime.strptime(values[0], '%Y-%m-%d'):
                            input_cash = int(values[2])
                            search_date = result[(result['datetime'] == input_first_date) | (result['datetime'] == input_second_date)]
                            search_index = search_date.index
                            search_index = search_index.tolist()
                            search_all_date = result[(result.index >= search_index[0]) & (result.index <= search_index[1])]
                            min_price = result['avg_price'][search_index[1]]
                            max_price = result['avg_price'][search_index[0]]

                            input_first_price = search_date['avg_price'][search_index[0]]
                            input_second_price = search_date['avg_price'][search_index[1]]
                            input_count = math.trunc(input_cash / min_price) #소지가능 갯수
                            input_count_0 = 0
                            cal_price_0 = 0
                            cal_price_1 = 0
                            cal_price_2 = 0
                            cal_price_3 = 0
                            cal_price_4 = 0
                            cal_percent = 0
                    else:
                        input_first_date = str(values[0])
                        input_second_date = str(values[1])
                        if datetime.datetime.strptime(values[1], '%Y-%m-%d') >= datetime.datetime.strptime(values[0], '%Y-%m-%d'):
                            #min_date = datetime.datetime.strptime(values[1], '%Y-%m-%d') - datetime.timedelta(days=1)
                            #min_date = min_date.strftime('%Y-%m-%d')
                            input_cash = int(values[2])
                            search_date = result[(result['datetime'] == input_first_date) | (result['datetime'] == input_second_date)]
                            search_index = search_date.index
                            search_index = search_index.tolist()
                            search_all_date = result[(result.index >= search_index[0]) & (result.index <= search_index[1])]
                            min_price = result['avg_price'][search_index[1]]
                            max_price = result['avg_price'][search_index[0]]

                            input_first_price = search_date['avg_price'][search_index[0]]
                            input_second_price = search_date['avg_price'][search_index[1]]
                            input_count = math.trunc(input_cash / min_price) #소지가능 갯수
                            input_count_0 = int(values[3]) #소지가능 갯수

                            cal_price_0 = round((input_second_price * input_count_0), 2)
                            cal_price_1 = round(input_cash - cal_price_0, 2)
                            cal_price_2 = round((input_second_price - input_first_price) * -1, 2) #개당 이윤
                            cal_price_3 = round(cal_price_2 * input_count_0, 2)
                            cal_price_4 = cal_price_3 + input_cash
                            cal_percent = round(float(cal_price_3) / float(cal_price_0) * 100, 2)

                            print(result['datetime'][0], input_first_date, input_second_date)
                            #print(all_datetime)
                            if input_first_date in all_datetime:
                                first_index = all_datetime.index(input_first_date)
                                second_index = all_datetime.index(input_second_date)
                                print(second_index)
                                for i in range(0, second_index):
                                    del_date = all_datetime.pop(0)
                                    del_price = all_price.pop(0)
                                    del_volume = all_volume.pop(0)
                                    del_day_before = all_day_before.pop(0)
                                    del_yn_before =  all_yn_before.pop(0)
                                    del_day_percent = all_day_percent.pop(0)
                                j_index = all_count  - first_index
                                for i in range(0, j_index - 1):
                                    all_count = len(all_datetime) - 1
                                    del_date_1 = all_datetime.pop(all_count)
                                    del_price_1 = all_price.pop(all_count)
                                    del_volume_1 = all_volume.pop(all_count)
                                    del_day_before_1 = all_day_before.pop(all_count)
                                    del_yn_before_1 =  all_yn_before.pop(all_count)
                                    del_day_percent_1 = all_day_percent.pop(all_count)

                                all_count = len(all_datetime)
                                all_datetime.reverse()
                                all_price.reverse()

                                get_money = []
                                for i in range(0, all_count):
                                    price_0 = all_price[i]
                                    price_1 = round(price_0 * input_count_0, 2)
                                    price_2 = round(price_1 + cal_price_1, 2)
                                    price_3 = round(price_2 / input_cash, 2)
                                    get_money.append(price_3)
                                xlabels = all_datetime
                                dataset = all_price
                                dataset_1 = get_money

                return render_template('calculator.html', **locals())
            else:
                return redirect('/error/')

@app.errorhandler(404)
def page_not_found(error):
    visit_count = get_visit()
    all_item, all_item_kr, all_item_en, all_path, all_path_0, all_path_1, all_type, all_type_kr, all_type_en = get_all_item()
    return render_template('error.html', **locals()), 404

#=======================================================================#

@app.route('/notice/')
def notice():
    visit_count = get_visit()
    all_item, all_item_kr, all_item_en, all_path, all_path_0, all_path_1, all_type, all_type_kr, all_type_en = get_all_item()

    path = '/workspace/crawling/data/json/info/notice_data.json'
    with open(path, "r", encoding="UTF-8") as json_file:
        json_data_0 = json.load(json_file, strict = False)

    index_0 = []
    image_0 = []
    write_0 = []
    subject_0 = []
    contents_0 = []
    contents_image_0 = []
    youtube_0 = []
    date_0 = []
    len_data_0 = len(json_data_0["info"])

    for i in json_data_0["info"]:
        index_0.append(i["index"])
        image_0.append(i["image"])
        write_0.append(i["write"])
        subject_0.append(i["subject"])
        contents_0.append(i["contents"])
        contents_image_0.append(i["contents_image"])
        youtube_0.append(i["youtube"])
        date_0.append(i["date"])

    index_0.reverse()
    image_0.reverse()
    write_0.reverse()
    subject_0.reverse()
    contents_0.reverse()
    contents_image_0.reverse()
    youtube_0.reverse()
    date_0.reverse()

    path_1 = '/workspace/crawling/data/json/info/info_data_0.json'
    with open(path_1, "r", encoding="UTF-8") as json_file_1:
        json_data_1 = json.load(json_file_1, strict = False)

    index_1 = []
    image_1 = []
    write_1 = []
    subject_1 = []
    contents_1 = []
    contents_image_1 = []
    youtube_1 = []
    date_1 = []
    len_data_1 = len(json_data_1["info"])

    for i in json_data_1["info"]:
        index_1.append(i["index"])
        image_1.append(i["image"])
        write_1.append(i["write"])
        subject_1.append(i["subject"])
        contents_1.append(i["contents"])
        contents_image_1.append(i["contents_image"])
        youtube_1.append(i["youtube"])
        date_1.append(i["date"])

    path = '/workspace/crawling/data/json/info/info_data_2.json'
    with open(path, "r", encoding="UTF-8") as json_file:
        json_data_2 = json.load(json_file, strict = False)

    index_2 = []
    image_2 = []
    write_2 = []
    subject_2 = []
    contents_2 = []
    contents_image_2 = []
    youtube_2 = []
    date_2 = []
    len_data_2 = len(json_data_2["info"])

    for i in json_data_2["info"]:
        index_2.append(i["index"])
        image_2.append(i["image"])
        write_2.append(i["write"])
        subject_2.append(i["subject"])
        contents_2.append(i["contents"])
        contents_image_2.append(i["contents_image"])
        youtube_2.append(i["youtube"])
        date_2.append(i["date"])

    return render_template('notice.html', **locals())

#=======================================================================#

@app.route('/economy/')
def economy():
    visit_count = get_visit()

    today_datetime = get_today_date()
    all_top = read_csv('all_top', 'result')
    all_bottom = read_csv('all_bottom', 'result')
    today_top = read_csv('today_top', 'result')
    today_bottom = read_csv('today_bottom', 'result')
    today_volume = read_csv('today_volume', 'result')
    today_all = read_csv('result', 'result')
    recommend_item = read_csv('recommend_item', 'result')
    recommend_top = read_csv('recommend_top', 'result')
    recommend_bottom = read_csv('recommend_bottom', 'result')

    all_item, all_item_kr, all_item_en, all_path, all_path_0, all_path_1, all_type, all_type_kr, all_type_en = get_all_item()
    def find_path(name, types):
        if types == 'path':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path = all_path[i]
                    return path
        elif types == 'path_0':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_0 = all_path_0[i]
                    return path_0
        elif types == 'path_1':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_1 = all_path_1[i]
                    return path_1

    a_top_name = []
    a_top_kr_name = []
    a_top_price = []
    a_top_before = []
    a_top_percent = []
    a_top_path = []
    a_top_path_0 = []
    a_top_path_1 = []
    a_top_lank = []
    a_top_name = all_top['name'].tolist()
    a_top_kr_name = change_to_kr('all_top', 'in', '')
    a_top_price = all_top['avg_price'].tolist()
    a_top_before = all_top['day_before'].tolist()
    a_top_percent = all_top['day_percent'].tolist()
    a_top_lank = all_top['lank'].tolist()
    for i in a_top_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        a_top_path.append(str(result))
        a_top_path_0.append(str(result_0))
        a_top_path_1.append(str(result_1))

    a_bottom_name = []
    a_bottom_kr_name = []
    a_bottom_price = []
    a_bottom_before = []
    a_bottom_percent = []
    a_bottom_path = []
    a_bottom_path_0 = []
    a_bottom_path_1 = []
    a_bottom_lank = []
    a_bottom_name = all_bottom['name'].tolist()
    a_bottom_kr_name = change_to_kr('all_bottom', 'in', '')
    a_bottom_price = all_bottom['avg_price'].tolist()
    a_bottom_before = all_bottom['day_before'].tolist()
    a_bottom_percent = all_bottom['day_percent'].tolist()
    a_bottom_lank = all_bottom['lank'].tolist()
    for i in a_bottom_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        a_bottom_path.append(str(result))
        a_bottom_path_0.append(str(result_0))
        a_bottom_path_1.append(str(result_1))

    t_top_name = []
    t_top_kr_name = []
    t_top_price = []
    t_top_before = []
    t_top_percent = []
    t_top_path = []
    t_top_path_0 = []
    t_top_path_1 = []
    t_top_name = today_top['name'].tolist()
    t_top_kr_name = change_to_kr('today_top', 'in', '')
    t_top_price = today_top['avg_price'].tolist()
    t_top_before = today_top['day_before'].tolist()
    t_top_percent = today_top['day_percent'].tolist()
    for i in t_top_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_top_path.append(str(result))
        t_top_path_0.append(str(result_0))
        t_top_path_1.append(str(result_1))

    t_bottom_name = []
    t_bottom_kr_name = []
    t_bottom_price = []
    t_bottom_before = []
    t_bottom_percent = []
    t_bottom_path = []
    t_bottom_path_0 = []
    t_bottom_path_1 = []
    t_bottom_name = today_bottom['name'].tolist()
    t_bottom_kr_name = change_to_kr('today_bottom', 'in', '')
    t_bottom_price = today_bottom['avg_price'].tolist()
    t_bottom_before = today_bottom['day_before'].tolist()
    t_bottom_percent = today_bottom['day_percent'].tolist()
    for i in t_bottom_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_bottom_path.append(str(result))
        t_bottom_path_0.append(str(result_0))
        t_bottom_path_1.append(str(result_1))

    t_volume_name = []
    t_volume_kr_name = []
    t_volume_price = []
    t_volume_before = []
    t_volume_percent = []
    t_volume_path = []
    t_volume_path_0 = []
    t_volume_path_1 = []
    t_volume = []
    t_volume_name = today_volume['name'].tolist()
    t_volume_kr_name = change_to_kr('today_volume', 'in', '')
    t_volume_price = today_volume['avg_price'].tolist()
    t_volume_before = today_volume['day_before'].tolist()
    t_volume_percent = today_volume['day_percent'].tolist()
    t_volume = today_volume['volume'].tolist()
    for i in t_volume_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_volume_path.append(str(result))
        t_volume_path_0.append(str(result_0))
        t_volume_path_1.append(str(result_1))

    r_item_name = []
    r_item_kr_name = []
    r_item_price = []
    r_item_before = []
    r_item_percent = []
    r_item_path = []
    r_item_path_0 = []
    r_item_path_1 = []
    r_item_name = recommend_item['name'].tolist()
    r_item_kr_name = change_to_kr('recommend_item', 'in', '')
    r_item_price = recommend_item['avg_price'].tolist()
    r_item_before = recommend_item['day_before'].tolist()
    r_item_percent = recommend_item['day_percent'].tolist()
    for i in r_item_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        r_item_path.append(str(result))
        r_item_path_0.append(str(result_0))
        r_item_path_1.append(str(result_1))

    r_top_name = []
    r_top_kr_name = []
    r_top_price = []
    r_top_before = []
    r_top_percent = []
    r_top_path = []
    r_top_path_0 = []
    r_top_path_1 = []
    r_top_name = recommend_top['name'].tolist()
    r_top_kr_name = change_to_kr('recommend_top', 'in', '')
    r_top_price = recommend_top['avg_price'].tolist()
    r_top_before = recommend_top['day_before'].tolist()
    r_top_percent = recommend_top['day_percent'].tolist()
    for i in r_top_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        r_top_path.append(str(result))
        r_top_path_0.append(str(result_0))
        r_top_path_1.append(str(result_1))

    r_bottom_name = []
    r_bottom_kr_name = []
    r_bottom_price = []
    r_bottom_before = []
    r_bottom_percent = []
    r_bottom_path = []
    r_bottom_path_0 = []
    r_bottom_path_1 = []
    r_bottom_name = recommend_bottom['name'].tolist()
    r_bottom_kr_name = change_to_kr('recommend_bottom', 'in', '')
    r_bottom_price = recommend_bottom['avg_price'].tolist()
    r_bottom_before = recommend_bottom['day_before'].tolist()
    r_bottom_percent = recommend_bottom['day_percent'].tolist()
    for i in r_bottom_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        r_bottom_path.append(str(result))
        r_bottom_path_0.append(str(result_0))
        r_bottom_path_1.append(str(result_1))

    t_all_name = []
    t_all_kr_name = []
    t_all_price = []
    t_all_before = []
    t_all_befores = []
    t_all_volume = []
    t_all_date = []
    t_all_percent = []
    t_all_path = []
    t_all_path_0 = []
    t_all_path_1 = []
    t_all_name = today_all['name'].tolist()
    t_all_name_count = len(t_all_name)
    t_all_kr_name = change_to_kr('result', 'in', '')
    t_all_price = today_all['avg_price'].tolist()
    t_all_before = today_all['day_before'].tolist()
    t_all_befores = today_all['yn_before'].tolist()
    t_all_volume = today_all['volume'].tolist()
    t_all_date = today_all['datetime'].tolist()
    t_all_percent = today_all['day_percent'].tolist()

    for i in t_all_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_all_path.append(str(result))
        t_all_path_0.append(str(result_0))
        t_all_path_1.append(str(result_1))

    return render_template('economy.html', **locals())
#=======================================================================#

@app.route('/en/economy/')
def economy_en():
    visit_count = get_visit()

    today_datetime = get_today_date()
    all_top = read_csv('all_top', 'result')
    all_bottom = read_csv('all_bottom', 'result')
    today_top = read_csv('today_top', 'result')
    today_bottom = read_csv('today_bottom', 'result')
    today_volume = read_csv('today_volume', 'result')
    today_all = read_csv('result', 'result')
    recommend_item = read_csv('recommend_item', 'result')
    recommend_top = read_csv('recommend_top', 'result')
    recommend_bottom = read_csv('recommend_bottom', 'result')

    all_item, all_item_kr, all_item_en, all_path, all_path_0, all_path_1, all_type, all_type_kr, all_type_en = get_all_item()
    def find_path(name, types):
        if types == 'path':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path = all_path[i]
                    return path
        elif types == 'path_0':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_0 = all_path_0[i]
                    return path_0
        elif types == 'path_1':
            for i, v in enumerate(all_item):
                if str(v) == name:
                    path_1 = all_path_1[i]
                    return path_1

    a_top_name = []
    a_top_en_name = []
    a_top_price = []
    a_top_before = []
    a_top_percent = []
    a_top_path = []
    a_top_path_0 = []
    a_top_path_1 = []
    a_top_lank = []
    a_top_name = all_top['name'].tolist()
    a_top_en_name = change_to_en('all_top', 'in', '')
    a_top_price = all_top['avg_price'].tolist()
    a_top_before = all_top['day_before'].tolist()
    a_top_percent = all_top['day_percent'].tolist()
    a_top_lank = all_top['lank'].tolist()
    for i in a_top_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        a_top_path.append(str(result))
        a_top_path_0.append(str(result_0))
        a_top_path_1.append(str(result_1))

    a_bottom_name = []
    a_bottom_en_name = []
    a_bottom_price = []
    a_bottom_before = []
    a_bottom_percent = []
    a_bottom_path = []
    a_bottom_path_0 = []
    a_bottom_path_1 = []
    a_bottom_lank = []
    a_bottom_name = all_bottom['name'].tolist()
    a_bottom_en_name = change_to_en('all_bottom', 'in', '')
    a_bottom_price = all_bottom['avg_price'].tolist()
    a_bottom_before = all_bottom['day_before'].tolist()
    a_bottom_percent = all_bottom['day_percent'].tolist()
    a_bottom_lank = all_bottom['lank'].tolist()
    for i in a_bottom_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        a_bottom_path.append(str(result))
        a_bottom_path_0.append(str(result_0))
        a_bottom_path_1.append(str(result_1))

    t_top_name = []
    t_top_en_name = []
    t_top_price = []
    t_top_before = []
    t_top_percent = []
    t_top_path = []
    t_top_path_0 = []
    t_top_path_1 = []
    t_top_name = today_top['name'].tolist()
    t_top_en_name = change_to_en('today_top', 'in', '')
    t_top_price = today_top['avg_price'].tolist()
    t_top_before = today_top['day_before'].tolist()
    t_top_percent = today_top['day_percent'].tolist()
    for i in t_top_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_top_path.append(str(result))
        t_top_path_0.append(str(result_0))
        t_top_path_1.append(str(result_1))

    t_bottom_name = []
    t_bottom_en_name = []
    t_bottom_price = []
    t_bottom_before = []
    t_bottom_percent = []
    t_bottom_path = []
    t_bottom_path_0 = []
    t_bottom_path_1 = []
    t_bottom_name = today_bottom['name'].tolist()
    t_bottom_en_name = change_to_en('today_bottom', 'in', '')
    t_bottom_price = today_bottom['avg_price'].tolist()
    t_bottom_before = today_bottom['day_before'].tolist()
    t_bottom_percent = today_bottom['day_percent'].tolist()
    for i in t_bottom_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_bottom_path.append(str(result))
        t_bottom_path_0.append(str(result_0))
        t_bottom_path_1.append(str(result_1))

    t_volume_name = []
    t_volume_en_name = []
    t_volume_price = []
    t_volume_before = []
    t_volume_percent = []
    t_volume_path = []
    t_volume_path_0 = []
    t_volume_path_1 = []
    t_volume = []
    t_volume_name = today_volume['name'].tolist()
    t_volume_en_name = change_to_en('today_volume', 'in', '')
    t_volume_price = today_volume['avg_price'].tolist()
    t_volume_before = today_volume['day_before'].tolist()
    t_volume_percent = today_volume['day_percent'].tolist()
    t_volume = today_volume['volume'].tolist()
    for i in t_volume_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_volume_path.append(str(result))
        t_volume_path_0.append(str(result_0))
        t_volume_path_1.append(str(result_1))

    r_item_name = []
    r_item_en_name = []
    r_item_price = []
    r_item_before = []
    r_item_percent = []
    r_item_path = []
    r_item_path_0 = []
    r_item_path_1 = []
    r_item_name = recommend_item['name'].tolist()
    r_item_en_name = change_to_en('recommend_item', 'in', '')
    r_item_price = recommend_item['avg_price'].tolist()
    r_item_before = recommend_item['day_before'].tolist()
    r_item_percent = recommend_item['day_percent'].tolist()
    for i in r_item_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        r_item_path.append(str(result))
        r_item_path_0.append(str(result_0))
        r_item_path_1.append(str(result_1))

    r_top_name = []
    r_top_en_name = []
    r_top_price = []
    r_top_before = []
    r_top_percent = []
    r_top_path = []
    r_top_path_0 = []
    r_top_path_1 = []
    r_top_name = recommend_top['name'].tolist()
    r_top_en_name = change_to_en('recommend_top', 'in', '')
    r_top_price = recommend_top['avg_price'].tolist()
    r_top_before = recommend_top['day_before'].tolist()
    r_top_percent = recommend_top['day_percent'].tolist()
    for i in r_top_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        r_top_path.append(str(result))
        r_top_path_0.append(str(result_0))
        r_top_path_1.append(str(result_1))

    r_bottom_name = []
    r_bottom_en_name = []
    r_bottom_price = []
    r_bottom_before = []
    r_bottom_percent = []
    r_bottom_path = []
    r_bottom_path_0 = []
    r_bottom_path_1 = []
    r_bottom_name = recommend_bottom['name'].tolist()
    r_bottom_en_name = change_to_en('recommend_bottom', 'in', '')
    r_bottom_price = recommend_bottom['avg_price'].tolist()
    r_bottom_before = recommend_bottom['day_before'].tolist()
    r_bottom_percent = recommend_bottom['day_percent'].tolist()
    for i in r_bottom_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        r_bottom_path.append(str(result))
        r_bottom_path_0.append(str(result_0))
        r_bottom_path_1.append(str(result_1))

    t_all_name = []
    t_all_en_name = []
    t_all_price = []
    t_all_before = []
    t_all_befores = []
    t_all_volume = []
    t_all_date = []
    t_all_percent = []
    t_all_path = []
    t_all_path_0 = []
    t_all_path_1 = []
    t_all_name = today_all['name'].tolist()
    t_all_name_count = len(t_all_name)
    t_all_en_name = change_to_en('result', 'in', '')
    t_all_price = today_all['avg_price'].tolist()
    t_all_before = today_all['day_before'].tolist()
    t_all_befores = today_all['yn_before'].tolist()
    t_all_volume = today_all['volume'].tolist()
    t_all_date = today_all['datetime'].tolist()
    t_all_percent = today_all['day_percent'].tolist()

    for i in t_all_name:
        result = find_path(i, 'path')
        result_0 = find_path(i, 'path_0')
        result_1 = find_path(i, 'path_1')
        t_all_path.append(str(result))
        t_all_path_0.append(str(result_0))
        t_all_path_1.append(str(result_1))

    return render_template('economy_en.html', **locals())

#=======================================================================#
if __name__ == '__main__':
    #ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    #ssl_context.load_cert_chain(certfile='', keyfile='', password=random)
    app.static_folder = 'static'
    app.run(host = '0.0.0.0', port = 5000, debug=False)