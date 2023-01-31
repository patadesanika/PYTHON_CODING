class A:
    def show(self):
        print("in show")
class B(A):
    def show(self):
        print("IN B SHOW")#these method will override class A's method 
obj=B()
obj.show()