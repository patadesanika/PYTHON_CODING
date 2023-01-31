from re import A


def sum(a,*b):
    c=a
    for i in b:
        c=c+i
    print("the output is:- ",c)
sum(12,67,89,90)