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

file_path = '/workspace/crawling/data/json/relic_drop_table.json'
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)

relic = []
types = []
image_path = []
name_1 = []
site_path_1 = []
name_2 = []
site_path_2 = []
name_3 = []
site_path_3 = []
name_4 = []
site_path_4 = []
name_5 = []
site_path_5 = []
name_6 = []
site_path_6 = []
search_name = []
search_price = []

for i in range(0, len(json_data)):
    test = json_data[str(i)]
    relic.append(test[0]["relic"])
    types.append(test[0]["type"])
    image_path.append('/workspace/crawling/html/static/image/item_image/relic/')
    name_1.append(test[0]["name_1"])
    name_2.append(test[0]["name_2"])
    name_3.append(test[0]["name_3"])
    name_4.append(test[0]["name_4"])
    name_5.append(test[0]["name_5"])
    name_6.append(test[0]["name_6"])
    site_path_1.append('https://warframe.market/items/' + str(test[0]["name_1"]).lower().replace(' ', '_'))
    site_path_2.append('https://warframe.market/items/' + str(test[0]["name_2"]).lower().replace(' ', '_'))
    site_path_3.append('https://warframe.market/items/' + str(test[0]["name_3"]).lower().replace(' ', '_'))
    site_path_4.append('https://warframe.market/items/' + str(test[0]["name_4"]).lower().replace(' ', '_'))
    site_path_5.append('https://warframe.market/items/' + str(test[0]["name_5"]).lower().replace(' ', '_'))
    site_path_6.append('https://warframe.market/items/' + str(test[0]["name_6"]).lower().replace(' ', '_'))

def connect_wm(site_path):
    if(site_path == 'https://warframe.market/items/forma_blueprint'):
        return '0'
    res = requests.get(site_path)
    soup = bs(res.text, 'html.parser')
    str_txt = str(soup.find_all('meta')[4])
    return str_txt.split(' ')[2]

def search_value(index):
    ty_name = str(types[index]) + ' ' + str(relic[index])
    name = []
    name.append(name_1[index])
    name.append(name_2[index])
    name.append(name_3[index])
    name.append(name_4[index])
    name.append(name_5[index])
    name.append(name_6[index])
    price = []
    price.append(connect_wm(site_path_1[index]))
    price.append(connect_wm(site_path_2[index]))
    price.append(connect_wm(site_path_3[index]))
    price.append(connect_wm(site_path_4[index]))
    price.append(connect_wm(site_path_5[index]))
    price.append(connect_wm(site_path_6[index]))
    return ty_name, name, price

search_type, search_name, search_price  = search_value(248)
print(search_type, search_name, search_price)