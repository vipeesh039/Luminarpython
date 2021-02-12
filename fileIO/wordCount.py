f=open("demo1","r")
names=set()
dict={}
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for word in words:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
print(dict)
print(max(dict,key=dict.get))
