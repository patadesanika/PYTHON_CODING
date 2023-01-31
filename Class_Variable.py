class Carr:
#VARIABLE WHICH IS DECALRED INSIDE CLASS BUT OUTSIDE _init_ METHOD KNOWN AS CLASS VARIABLE
    wheel=4
    def __init__(self) -> None:
        self.com="BMW"
c1=Carr()
c2=Carr()
c1.wheel=9#will overide wheel=4
print(c1.wheel,c1.com)
print(c2.wheel,c2.com)