#factorial number
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)#4 :n=4-1:= 3 :n=3-1=: 2  :n=2-1:= 1
n=int(input("enter any number that wnat to find a factorial")) 
result=fact(n)
print(result)