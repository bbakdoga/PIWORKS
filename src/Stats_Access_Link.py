
import csv
from collections import defaultdict

r = csv.reader(open('stats_access.csv')) 
data = list(r)

totalvac = 0
for elements in  range(len(data)):
        temp = data[elements][1]
        if elements > 0:
            #print(data[elements][1])
            temp = data[elements][1].split("//",1)[1] 
            print(temp.split("</",1)[0])
             
        
