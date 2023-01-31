from functools import reduce
arr = [1,2,3,4,5,6,7,8,9,10]
def chkeven(no):
    return no%2==0

def increase(number):
    return number+2

def Add(a,b):
    return a+b


evennumber_filter=list(filter(chkeven,arr))
print("prvious data before apply filter",arr)

print("After filtering the data",evennumber_filter)

print("************ MAP ************************")

incresemap=list(map(increase,evennumber_filter))
print("before the map",evennumber_filter)

print("after adding map function and increse the value by 2 is:-",incresemap)


print("*********Reduce*************")
reducefun=reduce(Add,incresemap)
print("After applying reduce",reducefun)