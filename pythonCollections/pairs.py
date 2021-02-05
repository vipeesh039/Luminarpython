lst=[1,2,3,4]
num=int(input("enter the number"))
flag=0
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==num:
            print(lst[i],",",lst[j])
            flag=1
            break
if flag==1:
    print("not found")
