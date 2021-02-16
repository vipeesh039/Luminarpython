f=open("movie","r")
dict={}

for lines in f:
    data=lines.rstrip("\n").split("\t")
    year=data[2]
    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1
print(max(dict,key=dict.get))
print(min(dict,key=dict.get))
for k,v in dict.items():
    print(k," ",v)
