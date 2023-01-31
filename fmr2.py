from functools import reduce
def chkeven(no):
    return no%2==0

def double(no):
    return no*2

def summaation(a,b):
    return a+b
def main():
    isize=int(input("Enter the count of data that you want"))
    data_Size=[]#creates empty list
    for i in range(0,isize):
        value=int(input())
        data_Size.append(value)
    print("your data is",data_Size)
    print("----------------------------------")
    filterX=list(filter(chkeven,data_Size))
    print("data after filter is",filterX)
    print("----------------------------------")
    mapX=list(map(double,data_Size))
    print("data after double is:-",mapX)
    print("----------------------------------")
    reduceX=reduce(summaation,data_Size)
    print("After summation is:-",reduceX)


if __name__=="__main__":
    main()
   