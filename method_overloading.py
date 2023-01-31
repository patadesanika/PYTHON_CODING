from re import S


class student:
    def sum(self,a=None,b=None,c=None):
        
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
           s=a+b
        else:
            s=a
        return s
s1=student()
print(s1.sum(10,20))