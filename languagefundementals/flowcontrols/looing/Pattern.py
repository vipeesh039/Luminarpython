
num=int(input("enter the number"))
sum=0
for i in range (1,(num+1)):
    data=str(num)*i
    sum=sum+int(data)
print(sum)