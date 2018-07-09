import string

base62={}

for i in range(0,10):
    base62[i] = str(i)
i = 10
for char in string.ascii_lowercase:
    base62[i] = char
    i = i + 1
for char in string.ascii_uppercase:
    base62[i] = char
    i = i + 1

num = 1530913637
digits = []

while num > 0:
    digits.append(num%62)
    num = num / 62

shorten_string = ""

for item in digits:
    if item in base62:
        shorten_string = shorten_string + base62[item]


shorten_string = shorten_string[::-1]  

