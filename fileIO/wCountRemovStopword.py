f=open("demo1","r")
names=set()
dict={}
stopword=["the","were","is","a","an","have","has","had","and","by","that","to","on"]
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for word in words:
        if word in stopword:
            pass
        else:
            if word not in dict:
                dict[word]=1
print(dict)

