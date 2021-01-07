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
        elif all_type[i] == "companion_mod":
            all_type_kr.append("동반자 모드")
        elif all_type[i] == "archwing_mod":
            all_type_kr.append("아크윙 모드")
        elif all_type[i] == "necramech_mod":
            all_type_kr.append("네크라메크 모드")
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

#=======================================================================#

@app.route('/')
def new_index():

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

    def get_items(name):
        for i, v in enumerate(get_item):
            if str(v) == name:
                search_path = get_path[i]
                result = read_csv_file(search_path)
                return result

    top_data = get_items(a_top_name[0])
    bottom_data = get_items(a_bottom_name[0])
    t_data_1 = get_items(t_top_name[0])

    t_xlabels = []
    t_dataset = []
    t_xlabels = top_data['datetime'].tolist()
    t_dataset = top_data['avg_price'].tolist()

    b_xlabels = []
    b_dataset = []
    b_xlabels = bottom_data['datetime'].tolist()
    b_dataset = bottom_data['avg_price'].tolist()

    up_xlabels = []
    up_dataset = []
    for i in t_top_kr_name:
        up_xlabels.append(i)
    for i in t_top_percent:
        up_dataset.append(i)

    down_xlabels = []
    down_dataset = []
    for i in t_bottom_kr_name:
        down_xlabels.append(i)
    for i in t_bottom_percent:
        down_dataset.append(i)

    return render_template('/new_templates/new_index.html', **locals())

#=======================================================================#

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

                return render_template('/new_templates/new_result.html', **locals())
            else:
                return redirect('/error/')

#=======================================================================#

if __name__ == '__main__':
    #ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    #ssl_context.load_cert_chain(certfile='', keyfile='', password='')
    app.static_folder = 'static'
    app.run(host = '0.0.0.0', port = 5000, debug = True)