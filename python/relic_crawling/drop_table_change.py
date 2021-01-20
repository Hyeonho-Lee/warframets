import os
import re
import time
import datetime
import requests
import json
from collections import OrderedDict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dateutil.parser import parse
from bs4 import BeautifulSoup as bs

find_txt = open('./drop_table.txt', mode='rt', encoding='utf-8')
all_text = str(find_txt.read())

first_data = all_text.split('@/@/')

make_json = OrderedDict()

def change_text(text):
    result = text
    result = result.replace('Systems Blueprint', 'Systems')
    result = result.replace('Chassis Blueprint', 'Chassis')
    result = result.replace('Neuroptics Blueprint', 'Neuroptics')
    return result

for i in range(0, int(len(first_data) / 4)):
    text = first_data[i * 4]
    text = text.replace('@/', '/')
    text = text.replace('@', '/')
    text = text.split('/')

    re_1 = change_text(text[1])
    re_2 = change_text(text[3])
    re_3 = change_text(text[5])
    re_4 = change_text(text[7])
    re_5 = change_text(text[9])
    re_6 = change_text(text[11])

    types = text[0].split(' ')

    make_json[str(i)] = []
    make_json[str(i)].append({
        "type": types[0],
        "relic": types[1],
        "name_1": re_1,
        "kr_name_1": '',
        "reward_1": text[2],
        "name_2": re_2,
        "kr_name_2": '',
        "reward_2": text[4],
        "name_3": re_3,
        "kr_name_3": '',
        "reward_3": text[6],
        "name_4": re_4,
        "kr_name_4": '',
        "reward_4": text[8],
        "name_5": re_5,
        "kr_name_5": '',
        "reward_5": text[10],
        "name_6": re_6,
        "kr_name_6": '',
        "reward_6": text[12]
    })


with open('/workspace/crawling/data/json/relic_drop_table.json', 'w', encoding='utf-8') as file:
    json_data = json.dumps(make_json, indent = 4)
    file.write(json_data)