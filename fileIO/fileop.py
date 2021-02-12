f=open("demo","r")
list=[]

for lines in f:
    list.append(lines.rstrip("\n"))
print(list)