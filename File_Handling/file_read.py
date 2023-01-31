import os
def read_file(filename):
    if(os.path.exists(filename)):
        fd=open(filename,"r")
        data=fd.read()
        print("data from your file is:-")
        print(data)
        fd.close()
    else:
        print("File is not available")
        return
def main():
    name=input("enter a name of file to read data\n")
    #create(name)
    read_file(name)
if __name__=="__main__":
    main()