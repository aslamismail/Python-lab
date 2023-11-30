import csv
c=open("csv1.csv")
d=csv.DictReader(c)
print("Name and Course")
for i in d:
    print(i['Name'],i['Course'])