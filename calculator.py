class Calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"the square of number is {self.number} is {self.number**2}") 
    def cube(self):
        print(f"the cube of number is {self.number} is {self.number**3}")
    def squareroot(self):
        print(f"the cube of number is {self.number} is {self.number**0.5}")
obj=Calculator(5)
obj.square()
obj.cube()
obj.squareroot()











































