class A:
    def feature1(self):
        print("in feature 1")
class B:
    def feature2(self):
        print("in fearure 2")
class C(A,B):
    def feature3(slef):
        print("in feature 3")
obj3=C()
obj3.feature1()
obj3.feature2()
obj3.feature3()