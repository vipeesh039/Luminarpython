arr=[10,11,12,13,14,15,16,18]
element=int(input("enter element"))
flag=0
for num in arr:
    if(element==num):
        flag = 1
        break

    else:
        pass
if flag == 1:
    print("present")
else:
    print("not present")