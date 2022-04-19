import re

import requests
import xlwt

html = requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js')
text_list = re.findall(r"var station_names ='([^']+)'", html.text)
text = "".join(text_list)
text = text.replace('@', '\n')
text = text[1:]
file = open('stations.txt', 'w')
file.write(text)
file.close()

stations_txt = open('stations.txt', 'r')
xls = xlwt.Workbook(encoding='utf-8')
sht = xls.add_sheet('stations')
for lines in range(0, len(open("stations.txt").readlines())):
    line = stations_txt.readline()
    contents = line.split('|')
    contents[5] = contents[5].replace('\n', '')
    for elements in range(0, 6):
        sht.write(lines, elements, contents[elements])
xls.save('stations.xls')
