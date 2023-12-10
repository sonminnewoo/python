import csv
import re

def opencsv(filename):
  output = []
  f =  open(filename, 'r')
  reader = csv.reader(f)
  for i in reader:
       output.append(i)
  return output

total = opencsv('popSeoul2.csv')
for i in total[:5]:
    print(i)

for i in total[:5]:
    for j in i:
      try:
         i[i.index(j)] = float(re.sub(',','',j))
      except:
         pass
print(total[:5])      
           