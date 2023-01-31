def create(filename):
    f=open(filename,"w")
def main():
    name=input("enter a name of file to create")
    create(name)
if __name__=="__main__":
    main()