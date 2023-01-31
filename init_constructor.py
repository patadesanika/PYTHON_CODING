class init_cons:
    def __init__(self,name,salry) -> None:
        self.name=name
        self.salry=salry
        print("Bro its automatically call when you erite init constructor ! ok!")
    def printdata(self):
        print(f"the name is:- {self.name}")
        print(f"the salry is:- {self.salry}")

ok=init_cons("sanika",1000000000)
ok.printdata()