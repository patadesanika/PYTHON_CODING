with open("another.txt") as f:
    content=f.read()

content=content.replace("donkey","$@##$")
 
with open("another.txt","w")as f:
    f.write(content)