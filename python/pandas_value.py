import os
import pandas as pd
import numpy as np

def read_csv(path):
    get_path = path
    if os.path.isfile(get_path):
        result = pd.read_csv(get_path, index_col = 0)
        result = result.reset_index()
        #result = result[::-1]
        return result
    else:
        print('파일이 없습니다.')

def pandas_value(name, types):
    #warframe_name = name
    #name = warframe_name.replace(' ', '_')
    name_csv = name + '.csv'
    path = '/workspace/crawling/data/csv/{types}/{name}/{name_csv}'.format(types = types, name = name, name_csv = name_csv)

    result = read_csv(path)

    result['day_before'] = np.nan
    result['yn_before'] = np.nan
    result['lank'] = np.nan
    result['day_percent'] = np.nan
    result['vol_before'] = np.nan
    result['vol_lank'] = np.nan
    #result['min_price'] = np.nan
    #result['max_price'] = np.nan
    #result['open_price'] = np.nan
    #result['closed_price'] = np.nan

    result.loc[0, ['day_before']] = 0.0
    result.loc[0, ['yn_before']] = '-'
    result.loc[0, ['lank']] = 0
    result.loc[0, ['day_percent']] = 0.0
    result.loc[0, ['vol_before']] = 0
    result.loc[0, ['vol_lank']] = 0
    #result.loc[0, ['min_price']] = 0.0
    #result.loc[0, ['max_price']] = 0.0
    #result.loc[0, ['open_price']] = 0.0
    #result.loc[0, ['closed_price']] = 0.0

    for i in range(1, len(result)):
        value = result['avg_price'][i] - result['avg_price'][i-1]
        vol_value = result['volume'][i] - result['volume'][i-1]
        result.loc[i, ['day_before']] = round(value, 1)
        result.loc[i, ['vol_before']] = vol_value
        result.loc[i, ['vol_lank']] = result['vol_lank'][i-1] + result['volume'][i]

        values = round(value, 1)
        before = result['avg_price'][i-1]
        percents = float(values) / float(before) * 100
        result.loc[i, ['day_percent']] = round(percents, 1)

        yn_value = str(value)[0:1]
        if(yn_value == '-'):
            yn_result = '▼'
            result.loc[i, ['yn_before']] = yn_result
            result.loc[i, ['lank']] = result['lank'][i-1] - 1
        else:
            if(value == 0.0):
                yn_result = '-'
                result.loc[i, ['yn_before']] = yn_result
                result.loc[i, ['lank']] = result['lank'][i-1]
            else:
                yn_result = '▲'
                result.loc[i, ['yn_before']] = yn_result
                result.loc[i, ['lank']] = result['lank'][i-1] + 1

    for col in result.columns:
        if col == 'index':
            del result[col]

    return result

#item = 'loki_prime_set'
#get_path = '/workspace/crawling/data/csv/warframe/' + item + '/' + item + '.csv'
#value = pandas_value('loki_prime_set', 'warframe')
#value.to_csv(get_path, mode = 'w')