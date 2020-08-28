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

pd.options.display.float_format = '{:.0f}'.format

def write_plot(item):
    get_item = str(item)
    get_path = './item/' + get_item + '/' + get_item + '.csv'
    get_path_0 = './item/' + get_item + '/' + get_item + '.png'
    
    result = pd.read_csv(get_path)
    result_data = pd.DataFrame({'date' : result['datetime'].apply(lambda x: pd.to_datetime(str(x), format = '%Y-%m-%d')), 'platinum' : result['avg_price']})
    
    result_data.set_index(result_data['date'], inplace = True)
    
    for col in result_data.columns:
        if col == 'date':
            del result_data[col]
    
    save = result_data.plot(kind = 'line', title = get_item, figsize = (13.5, 9), legend = True, fontsize = 12, marker = 'o')
    
    plt.show()
    plt.savefig(get_path_0)
    
write_plot('loki_prime_set')