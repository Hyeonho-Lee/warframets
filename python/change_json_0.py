import os
import json
import pandas as pd
import numpy as np
from datetime import date, timedelta

item = str("weapon_mods")
path = '/home/ec2-user/environment/warframets/data/json/{etc}.json'.format(etc = item)
with open(path, "r") as json_file:
    json_data = json.load(json_file, strict = False)

name_data = []
result_data = []
type_data = []

for i in json_data[item]:
    name_data.append(str(i["en_name"]))
    result_data.append(str(i["name"]))
    type_data.append(str(i["type"]))

test, result_name = name_data, result_data

result = []

for i, v in enumerate(test):
    before = v.lower()
    after = before.replace(' ', '_')
    result.append(after)

for i, v in enumerate(json_data[item]):
    v["name"] = result[i]