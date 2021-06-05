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

def change_to_kr(csv_name, etc, text):
    item_name = []
    item_en_name = []
    item_kr_name = []

    with open('/home/ec2-user/environment/warframets/data/json/warframes.json', 'r') as file:
        json_data = json.load(file)
    result_data = json_data['warframes']
    with open('/home/ec2-user/environment/warframets/data/json/weapons.json', 'r') as file_1:
        json_data_1 = json.load(file_1)
    result_data_1 = json_data_1['weapons']

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

    path = '/home/ec2-user/environment/warframets/data/csv/result/{name}.csv'.format(name = csv_name)
    resource = read_csv(path)

    result_all = []
    result_value = ''
    types = etc
    
    if types == 'in':
        for i in range(0, len(resource)):
            result = resource['name'][i]
            result_1 = result.replace('_set', '')
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

print(change_to_kr('all_top', 'out', '노바 프라임s'))