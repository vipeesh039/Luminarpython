import re
list=[]
rule="[K][L]\d{2}[A-Z]{2}\d{4}"

f=open("vehicleNumber","r")

for lines in f:
    number=lines.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher!=None:
        list.append(number)
print(list)

