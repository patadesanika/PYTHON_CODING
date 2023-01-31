class A:
    def a(self):
        print("hello strat from here toooo")
class B:
    @property
    def b():
        print("exam pressure!")
class c(A,B):
    @staticmethod
    def c():
        print("static method")
obj=c()
obj.c()
obj.a()