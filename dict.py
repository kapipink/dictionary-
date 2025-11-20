data_list =[]
sports_count={}
file=open('sport.txt', 'r', encoding='cp1251')
head=file.readline().strip().split('\t')
for line in file:
    data=line.strip().split('\t')
    dict={}
    for i, value in enumerate(data):
        if i<len(head):
            dict[head[i]]=value
    data_list.append(dict)
file.close()
for row in data_list:
    sports_str = row.get('Виды спорта', '')
    for sport in (s.strip().lower() for s in sports_str.split(',') if s.strip()):
        sports_count[sport] = sports_count.get(sport, 0) + 1

for sport, count in sorted(sports_count.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(f"{sport}: {count}")               
