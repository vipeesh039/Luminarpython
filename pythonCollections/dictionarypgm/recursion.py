text="ABAC"
dict={}
for ch in text:
    if ch not in dict:
        dict[ch]=1
    else:
        print(ch,"is the first recursive character")
        break