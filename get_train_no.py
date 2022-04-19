import os
import re

import requests
import xlrd

train_info = open('train_info.txt', 'w')
xls = xlrd.open_workbook_xls('stations.xls')
sht = xls.sheets()[0]
sht_rows = sht.nrows
session = requests.session()
date = input('YYYY-MM-DD')
for line in range(0, sht_rows):
    station_code = str(sht.row(line)[2].value)
    html = session.get(
        f'https://kyfw.12306.cn/otn/czxx/query?train_start_date={date}&train_station_code={station_code}')
    text = re.sub(r'\{\"validateMessagesShowId([\s\S]+?)\:\[', '', html.text)
    text = re.sub(r'\]\,\"sameStations([\s\S]+?)\{\}\}', '', text)
    text = re.sub(r'\}([\s\S]+?)\{', '}\n{', text)
    train_info.write(text + '\n')
train_info.close()
