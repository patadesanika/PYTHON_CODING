def addition(no):
    if(no<=0):
        return 1
    else:
        return (no*addition(no-1))
ret=int(input("enter a number"))
fact=addition(ret)
print("result is",fact)