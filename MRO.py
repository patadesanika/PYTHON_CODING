class A:
    def __init__(self) -> None:
        print("In A init constrcutor")
class B:
    def __init__(self) -> None:
       print("In B init constructor")
class C(A,B):
    def __init__(self) -> None:
        super().__init__()#Here it just only call a parent A class constructor it Does not 
        print("In C constructor")#call B class either we include SUPER keyword so MRO is came into picture

cc=C()
