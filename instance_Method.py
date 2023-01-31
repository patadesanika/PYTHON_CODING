class student:
    def __init__(self,m1,m2,m3) -> None:
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
       
s1=student(22,22,33)
print(s1.avg())