def demo1():
    print("inside demo 1")
#function accept one parameter and returns nothing
def Demo2(no):
    print("inside demo 2",no)
#function accept one parameter and return one parameter
def Demo3(no):
    print("inside demo 2",no)
    return no+2
#function accept two parameter and return one parameter
def Demo4(no1,no2):
    print("inside demo4")
    add=no1+no2
    return add
#function accept two parameter and return two parameter
def Demo5(no1,no2):
    print("inside demo5")
    add=no1+no2
    sub=no1-no2
    return add,sub
def main():
    demo1()

    Demo2('hello')

    ans=Demo3(10)
    print("return value of demo3 is",ans)

    ans=Demo4(10,11)
    print("return value is",ans)

    ans1=Demo5(11,12)
    print("output is",ans1)
    #print("second return value",ans2)

if __name__=="__main__":
    main()