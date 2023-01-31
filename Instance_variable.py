class Car:
    def __init__(self) -> None:
        # VARIABLE WHICH IS DECALRED INSIDE A INIT METHOD IS KNOWN AS INSTANCE VARIABLE
        self.mil=10
        self.com="BMW"
c1=Car()
c2=Car()
c1.mil=8
print(c1.mil,c1.com)
print(c2.mil,c2.com)
        
        
