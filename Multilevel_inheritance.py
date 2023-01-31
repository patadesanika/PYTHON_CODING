class A:
    def feature1(self):
        print("ih feature 1")
class B(A):
    def feature2(self):
        print("ih fearure 2")
class C(B):
    def feature3(self):
        print("in feature 3")
objj=C()
objj.feature1()
objj.feature2()
objj.feature3()