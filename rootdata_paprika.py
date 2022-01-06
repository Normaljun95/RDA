from pymongo import MongoClient
import pandas as pd
import json


client = MongoClient('mongodb://203.255.77.162:27017',
                      username='pa',
                      password='1',
                      authSource='paprika',
                      authMechanism='SCRAM-SHA-256')

db = client['paprika']
col = db['rootData']

xlsData1 = pd.read_excel("//203.255.92.201/netdb/001_프로젝트 자료/015_농진청 과제/데이터/7@2019_데이터현황/3.파프리카/근권부데이터/근권부데이터/down_period_20190301_0331.xls")
xlsData2 = pd.read_excel("//203.255.92.201/netdb/001_프로젝트 자료/015_농진청 과제/데이터/7@2019_데이터현황/3.파프리카/근권부데이터/근권부데이터/down_period_20190401_0430.xls")
xlsData = pd.concat([xlsData1, xlsData2], ignore_index=True)
payload = json.loads(xlsData.to_json(orient='records'))

# print(len(payload))


for num in range(len(payload)):
    
    keys_list = list(payload[num].keys())
    keys_list[4] = 'humi'
    keys_list[8] = 'ec'
    keys_list[9] = 'ph'

    values_list = list(payload[num].values())
    values_list[0] = str(values_list[0])
    values_list[2] = float(values_list[2])
    values_list[3] = float(values_list[3])
    values_list[4] = float(values_list[4])
    values_list[5] = float(values_list[5])
    values_list[6] = float(values_list[6])
    values_list[7] = float(values_list[7])
    values_list[8] = float(values_list[8])
    values_list[9] = float(values_list[9])
    values_list[10] = float(values_list[10])

    result = dict(zip(keys_list, values_list))
    col.insert(result)