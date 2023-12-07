import csv
field_name=['no','company','model']
car=[{"no":1,"company":"bmw","model":"M5"},
     {"no":2,"company":"bmw","model":"M5"},
     {"no":3,"company":"bmw","model":"M5"}]
c=open('b.csv','w')
d=csv.DictWriter(c, fieldnames=field_name)
d.writeheader()
d.writerows(car)
c.close()
r=open('b.csv',newline='')
d=csv.reader(r)
for i in d:
    print(' '.join(i))