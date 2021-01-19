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

for i in range(0, len(json_data)):
    test = json_data[str(i)]
    if(test[0]["type"] == 'Axi'):
        print("찾음!")