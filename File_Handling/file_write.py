import os
def write_file(filename):
    if(os.path.exists(filename)):
        print("enter the data that you want to write in file")
        Data=input()

        fd=open(filename,"a")
        fd.write(Data)
    else:
        print("File is not available")
        return
def main():
    name=input("enter a name of file to write data into it\n")
    #create(name)
    write_file(name)
if __name__=="__main__":
    main()