class A:
    company="abc"
    def method1(Self):
        print("start from here!")
class B(A):
    def method2(Self):
        print("method 2 here!")
obj=B()
obj.method1()
print(obj.company)
