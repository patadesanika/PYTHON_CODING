import os
def delete_file(filename):
    if(os.path.exists(filename)):
        os.remove(filename)
    else:
        print("File is not available")
        return
def main():
    name=input("enter a name of file to deletet\n")
    #create(name)
    delete_file(name)
if __name__=="__main__":
    main()