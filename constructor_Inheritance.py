class A:
    def __init__(self) -> None:
        print("In A init")
class B(A):
    def __init__(self) -> None:
         super().__init__()
         print("in B init")
            
i=B()
i.__init__()

 