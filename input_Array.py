from array import *

arr=array('i',[])
len=int(input("enter the length of array"))
for i in range(len):
    x=int(input("enter the next element"))
    arr.append(x)
print(arr)