#when you want to defined a global vaiable inside a function(Note! that varaible inside function konwon as local varaibel)
a=16
def function1():
    global aa
    aa=19
    print(aa)
function1()
print(a)
