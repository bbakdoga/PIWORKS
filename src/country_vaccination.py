import csv
from collections import defaultdict


r = csv.reader(open('country_vaccination_stats.csv')) 
data = list(r)
dic = defaultdict(list)
dic2 = defaultdict(list)

totalvac = 0
for elements in  range(len(data)):
        if len(data[elements][2]) < 1:
           data[elements][2] = 0
        #print(data[elements][0], " ",data[elements][2])
        if elements != 0:
            dic[data[elements][0]].append(float(data[elements][2]))
        if(data[elements][1] == '1/6/2021'):
            #print(data[elements][0], " ",data[elements][1], " ",data[elements][2])
            totalvac = totalvac + int(data[elements][2])
            #print()




writer = csv.writer(open('country_vaccination_stats.csv', 'w'))
writer.writerows(data)

for k,v in dic.items():
    dic2[k].append((sorted(v)[len(v) // 2]))
    #prnt ("{} median is {}".format(k,sorted(v)[len(v) // 2]))

dic2 = dict( sorted(dic2.items(),key=lambda item: item[1], reverse=True))
count = 0
for k,v in dic2.items():
    print ("{} median is {}".format(k,v))
    count += 1

    if count == 3:
        break


print('total vaccinations on 1/6/2021: ', totalvac)

