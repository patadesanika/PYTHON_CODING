class slef_use:
    def getdata(self):#self method
        print("here is self")
    @staticmethod
    def without_self():
        print("static")
    
ob=slef_use()
ob.getdata()
ob.without_self()
