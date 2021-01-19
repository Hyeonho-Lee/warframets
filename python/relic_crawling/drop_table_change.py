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

for i in range(0, int(len(first_data) / 4)):
    text = first_data[i * 4]
    text = text.replace('@/', '/')
    text = text.replace('@', '/')
    text = text.split('/')

    types = text[0].split(' ')

    make_json[str(i)] = []
    make_json[str(i)].append({
        "type": types[0],
        "relic": types[1],
        "name_1": text[1],
        "reward_1": text[2],
        "name_2": text[3],
        "reward_2": text[4],
        "name_3": text[5],
        "reward_3": text[6],
        "name_4": text[7],
        "reward_4": text[8],
        "name_5": text[9],
        "reward_5": text[10],
        "name_6": text[11],
        "reward_6": text[12]
    })


with open('/workspace/crawling/data/json/relic_drop_table.json', 'w', encoding='utf-8') as file:
    json_data = json.dumps(make_json, indent = 4)
    file.write(json_data)