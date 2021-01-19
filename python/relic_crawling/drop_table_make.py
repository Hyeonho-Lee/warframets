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

site = 'https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html'
res = requests.get(site)

html = res.text
soup = bs(html, 'html.parser')
test = soup.find_all("table")

data = str(test[1])
data = data.replace('<table>', '')
data = data.replace('</table>', '')
data = data.replace('<tr>', '')
data = data.replace('</tr>', '/')
data = data.replace('<td>', '')
data = data.replace('</td>', '@')
data = data.replace('<th>', '')
data = data.replace('</th>', '')
data = data.replace('<th colspan="2">', '')
data = data.replace('<td class="blank-row" colspan="2">', '')
data = data.replace('<tr class="blank-row">', '')

with open('./drop_table.txt', 'w') as file:
    file.write(str(data))