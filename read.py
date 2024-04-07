import csv
from isrcs import ISRCS
import datetime as DT
import pandas as pd

exerelease = False
ISRC = False
BYNAME = False

print("Заполните информацию о самом первом дне отчетов. \nПредставьте, что у вас есть отчеты с 20.02.2021 по 11.04.2023.\nСейчас введите информацию об отчете 20.02.2021")

start_date = DT.datetime(int(input("Введите год: ")), int(input("Введите месяц: ")), int(input("Введите день: ")))  # начальная дата

print("Заполните информацию о последнем дне отчетов. \nПредставьте, что у вас есть отчеты с 20.02.2021 по 11.04.2023.\nСейчас введите информацию об отчете 11.04.2023")
end_date = DT.datetime(int(input("Введите год: ")), int(input("Введите месяц: ")), int(input("Введите день: ")))  # конечная дата

res = pd.date_range(
    min(start_date, end_date),
    max(start_date, end_date)
).strftime('%Y-%m-%d_%Y-%m-%d_').tolist() #ЗАМЕНИТЕ ТЕКСТ ПОСЛЕ ДАТЫ!
days = int(input('Дней в статистике: '))
strms = 0
for i in res:

    f = open(f'{i}.csv', 'r', encoding='utf-8')
    reader = csv.DictReader(f, delimiter=',', quotechar='"')

    # sorted = sorted(reader, key=lambda x: int(x['streams']), reverse=False)
    if BYNAME: rname = input('Название релиза: ')
    for row in reader:
        if ISRC:
            if row['isrc'] in ISRCS:
                date = row['\ufeffdate']
                service = row['outlet']
                release = row['release_name']
                track = row['raw_title']
                iiiii = row['isrc']
                streams = int(row['streams'])
                strms += streams

                print(f'{date} -- {service} - {release} - {track} - {streams} = = = {strms}')

        elif BYNAME:
            if row['release_name'] in rname:
                date = row['\ufeffdate']
                service = row['outlet']
                release = row['release_name']
                track = row['raw_title']
                iiiii = row['isrc']
                streams = int(row['streams'])
                strms += streams

                # print(f'{iiiii} = = = {strms}')
        else:
            # print(row)
            date = row['\ufeffdate']
            service = row['outlet']
            release = row['release_name']
            track = row['raw_title']
            streams = int(row['streams'])
            strms += streams

        # print(f'{date} -- {service} - {release} - {track} - {streams} = = = {strms}')

if exerelease:
    file = open("musicstats.txt", "a")
    file.write(f'\nВсего прослушиваний - {strms}')
    file.write(f'\nДней - {days}')
    file.write(f'\nСредн. ариф - {strms / days}')
    file.write('\n------------------')
    file.close()

print(f'Всего прослушиваний - {strms}')
print(f'Средн. ариф - {strms / days}')
