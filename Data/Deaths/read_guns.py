"""
-- this is an identifier column, which contains the row number. It's common in CSV files to include a unique identifier for each row, but we can ignore it in this analysis.
year -- the year in which the fatality occurred.
month -- the month in which the fatality occurred.
intent -- the intent of the perpetrator of the crime. This can be Suicide, Accidental, NA, Homicide, or Undetermined.
police -- whether a police officer was involved with the shooting. Either 0 (false) or 1 (true).
sex -- the gender of the victim. Either M or F.
age -- the age of the victim.
race -- the race of the victim. Either Asian/Pacific Islander, Native American/Native Alaskan, Black, Hispanic, or White.
hispanic -- a code indicating the Hispanic origin of the victim.
place -- where the shooting occurred. Has several categories, which you're encouraged to explore on your own.
education -- educational status of the victim. Can be one of the following:
    In this project, we'll explore the dataset, and try to find patterns in the demographics of the victims. Our first step is to read the data in and take a look at it.

"""
import csv
import datetime
import re

with open("guns.csv", "r") as f:
    reader = csv.reader(f)
    data =  list(reader)

with open("census.csv", "r") as c:
    reader =  csv.reader(c)
    census = list(reader)

number_of_deaths_in_year = {}

headers = data[0]
data = data[1:]

print(headers)

for row in data[:5]:
    print (row)
    
print (census)
for row in data:
    if row[1] in number_of_deaths_in_year:
        number_of_deaths_in_year[row[1]] += 1
    else:
        number_of_deaths_in_year[row[1]] = 1
    
print (number_of_deaths_in_year)

dates = [datetime.datetime(year=int(row[1]), month = int(row[2]), day = 1) for row in data]

for row in dates[:5]:
    print (row)

unique_dates = {}

for row in dates:
    if row in unique_dates:
        unique_dates[row] += 1
    else:
        unique_dates[row] = 1

print (unique_dates)

#5,7
sex_counts = {}
race_counts = {}

for row in data:
    if row[5] in sex_counts:
        sex_counts[row[5]] += 1
    else:
        sex_counts[row[5]] = 1
        
regex = "[Hh]omicide"
for row in data:
    if row[7] in race_counts and re.search(regex, row[3]) is not None:
        race_counts[row[7]] += 1
    elif row[7] not in race_counts and re.search(regex, row[3]) is not None:
        race_counts[row[7]] = 1
print(sex_counts)
print(race_counts)

mapping = {}
mapping['Asian/Pacific Islander'] = int(census[1][13]) + int(census[1][14])
mapping['Hispanic'] = int(census[1][10])
mapping['Black'] = int(census[1][11])
mapping['White'] = int(census[1][9])
mapping['Native American/Native Alaskan'] = int(census[1][12])

print(mapping)

race_per_hundredk = {}

for key in race_counts:
    if key in mapping:
        race_per_hundredk[key] =  float(race_counts[key])/float(mapping[key])*100000
        
print (race_per_hundredk)
