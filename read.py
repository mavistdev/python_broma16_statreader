import csv

f = open('music.csv', 'r', encoding='utf-8')
reader = csv.DictReader(f, delimiter=',', quotechar='"')

days = int(input('Дней в статистике: '))

sorted = sorted(reader, key=lambda x: int(x['streams']), reverse=False)
strms = 0
for row in sorted:
    date = row['\ufeffdate']
    service = row['outlet']
    release = row['release_name']
    track = row['raw_title']
    streams = int(row['streams'])
    strms += streams

    print(f'{date} -- {service} - {release} - {track} - {streams} = = = {strms}')

print(f'Всего прослушиваний - {strms}')
print(f'Средн. ариф - {strms / days}')
