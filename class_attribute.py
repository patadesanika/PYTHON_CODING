class Emp:
    company="Google"
ob=Emp()
print(ob.company)
Emp.company="Microsoft" #CLASS ATTRIBUTE CAUSE WE WRITE CLASS NAME AND THEN VARIABLE NAME
print("class attribute:- ",ob.company)