text="hello hai how hello"
words=text.split(" ")
dict={}
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
maxword=max(dict.get)
print(maxword)
#error