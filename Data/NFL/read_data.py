import csv

with open("nfl-suspensions-data.csv", "rb") as f:
    reader = csv.reader(f)
    mylist = list(reader)


for row in mylist[:5]:
    print (row)
