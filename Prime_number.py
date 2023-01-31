#num=7
#for i in range(2,num):
#    if num % i==0:
#        print("NOT! prime number")
#       break
#else:
#    print(" prime")

number=int(input("Enter a any number"))
for i in range(2,number):
    if number%i==0:
        print("not prime number")
        break
else:
    print("prime number")