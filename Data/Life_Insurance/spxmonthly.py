import csv

with open("spx-monthly.csv","rb") as f:
    reader = csv.reader(f)
    mylist  = list(reader)

mylist[0] = ['Apr. 30, 2018', '0.27']

clean_list=[]
for item in mylist:
    x= item[0].split(',')
    x.append(item[1])
    x[0]=x[0][0:3]
    x[1] = int(x[1].strip())
    x[2] = float(x[2])
    clean_list.append(x)
clean_list.reverse()

month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
range_list = [[] for y in range(12)] 

for index, month in enumerate(month_list):
    start = False
    growth = 0.0
    count = 0
    for item in clean_list:
        if item[0] == month and start is False:
            start = True
        if start is True:
            if count % 12 == 0:
                growth = 0
                str1 = item[0] + " " + str(item[1])
            growth = growth + item[2]
            if count % 12 == 11:
                str1 = str1 + "-" + item[0] + " " + str(item[1])
                range_list[index].append([str1, round(growth,2)])
            count = count + 1

month_dict = {}

for index, item in enumerate(range_list):
    #print (month_list[index], len(item))
    cap_val =11
    spread_val = 6
    cap_total = 0
    spread_total = 0
    spx_total = 0
    for sub_item in item:
        spx_total =  spx_total + sub_item[1]
        if sub_item[1] <= 1:
            cap_total = cap_total + 1
        elif sub_item[1] > 1 and sub_item[1] <= cap_val:
            cap_total = cap_total + sub_item[1]
        elif sub_item[1] > cap_val:
            cap_total = cap_total + cap_val

        if sub_item[1] - spread_val <= 1:
            spread_total = spread_total + 1
        else:
            spread_total = spread_total + (sub_item[1] - spread_val)
    month_dict[month_list[index]]= [round(spx_total/len(item),2), round(cap_total/len(item),2),round(spread_total/len(item),2)]

print("Sorting by SPX")
for key, value in sorted(month_dict.items(), key=lambda x: x[1][0], reverse=True):
    print (key, value)
print("Sorting by Penn 11 cap")
for key, value in sorted(month_dict.items(), key=lambda x: x[1][1], reverse=True):
    print (key, value)
print("Sorting by Pen spread")
for key, value in sorted(month_dict.items(), key=lambda x: x[1][2], reverse=True):
    print (key, value)

