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
from selenium import webdriver

def input_item(etc):
    item = str(etc)
    path = '/home/ec2-user/environment/warframets/data/json/{etc}.json'.format(etc = item)
    with open(path, "r") as json_file:
        json_data = json.load(json_file)

    name_data = []
    #type_data = []

    for i in json_data[item]:
        name_data.append(str(i["name"]))
        #type_data.append(str(i["type"]))
    
    return name_data

#result = input_item('weapons')
#print(result)