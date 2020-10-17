import os
import json
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_csv_file(path):
    get_path = path
    if os.path.isfile(get_path):
        result = pd.read_csv(get_path, index_col = 0)
        result = result.reset_index()
        return result
    else:
        print('파일이 없습니다.')


def get_mdd(value):
    mdd_index = -1
    mdd_value = 1

    for i in range(1, len(value)):
        bw_max = max(value[:i])
        curr = value[i]
        mdd = curr / bw_max

        if mdd < mdd_value:
            mdd_value = mdd
            mdd_index = i

    return (mdd_index, mdd_value)

def find_mmd(path):
    test = read_csv_file(path)

    result = test['avg_price']
    list_r = result.tolist()
    value = get_mdd(list_r)
    mnd = test['datetime'][value[0]]
    mnd_date = datetime.strptime(mnd, '%Y-%m-%d')

    today_date = datetime.today()
    result_date = int((today_date - mnd_date).days)
    return result_date

path = '/workspace/crawling/data/csv/warframe/ash_prime_set/ash_prime_set.csv'
result = find_mmd(path)

#result.to_excel('test.xlsx')
#plt.plot(list_r)
#plt.axvline(value[0], c='r')
#plt.savefig('result_result.png')