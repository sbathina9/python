import math


def binary_search(mylist, start, end, number):
    length = len(mylist[start:end]) 
    middle = start + int(math.floor(length/2))
    
    if start >= end:
        print ("Not Found")
        return 

    if number < mylist[middle]:
        binary_search(mylist, start, middle, number)
    elif number > mylist[middle]:
        binary_search(mylist, middle+1,end, number)
    elif number == mylist[middle]:
        print ("Found")
        return

#mylist = ["Andy", "Becky", "Cat", "James", "Ryan", "Susan", "Zhang"]
#binary_search(mylist, 0, len(mylist), "Ryan")

mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14]

print (mylist)

for i in range(10):
    binary_search(mylist, 0, len(mylist), i)
binary_search(mylist, 0, len(mylist), -1)
binary_search(mylist, 0, len(mylist), 10)

