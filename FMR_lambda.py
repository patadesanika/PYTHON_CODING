from functools import reduce
Arr=[10,20,30,40,50,60,78,90]
evenchk=list(filter(lambda no:no%2==0,Arr))
print("after apply even",evenchk)
 
mapck=list(map(lambda no:no+2,Arr))
print("after invrement by 2",mapck)

reducechk=reduce(lambda a,b:a+b,Arr)
print(reducechk)