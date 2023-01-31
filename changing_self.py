class emp:
    def __init__(sani,salry) -> None:#so you can chnage the self parameter as anything you can writr yiur name,padosi name anything 
        sani.salry=salry
    def method(self,name):
        self.name=name
onj=emp(100000)
onj.method("sanika")
print(onj.name)
print(onj.salry)