from sys import *
from add_command import add
def main():
     if(len(argv)!=3):
         print("invalid input!")
         exit()

     f=add(int(argv[1]),int(argv[2]))
     print(f)
if __name__=="__main__":
    main()