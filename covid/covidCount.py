f=open("covid19 india","r")
dict={}

for lines in f:
    data=lines.rstrip("\n").split("\t")
    state=data[3]
    confirmed_case=data[-1]
    if state not in dict:
        dict[state]=int(confirmed_case)
    else:
        dict[state]=int(confirmed_case)
for k,v in dict.items():
    print(k," ",v)
print("highest:\n",max(dict,key=dict.get))
print("lowest:\n",min(dict,key=dict.get))