def  checkEven(No):
    return (No%2==0)

def increment(No):
    return No+2

def filterX(Arr,Function_Name):
    result=[]
    for no in Arr:
        if(Function_Name(no)):
            result.append(no)
    return result

def mapX(Arr,Function_Name):

    Result=[]
    for no in Arr:
        value=Function_Name(no)
        Result.append(value)
    return Result
def main():
    data=[2,3,1,6,4,5]
    print("orignal data is",data)
    Data_filter=list(filterX(data,checkEven ))
    print("after filter is",Data_filter)

    Data_Map=list(mapX(Data_filter,Increment))
    print("data after map",Data_Map)

if __name__=="__main__":
    main()