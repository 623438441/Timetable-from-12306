# Timetable from 12306
一种通过12306数据生成某一日期列车车次列表、时刻表（条目）数据的方法
具体逻辑：获取某日所有客运车站名及电报码->根据电报码获取该车站某日全部车次->对车次进行筛选去重->根据车次的TrainCode获取时刻数据生成Timetable->根据时刻数据中的车次（含复车次）回填Trainlist

运行顺序：get_station_name.py -> get_train_no.py -> arrange_train_no.py -> get_timetable.py -> arrange_timetable.py -> link.py
