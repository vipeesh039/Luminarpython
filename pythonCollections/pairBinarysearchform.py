lst=[1,2,3,4]
inp=int(input("enter element"))
low=0
upp=len(lst)-1

for i in range(0,len(lst)):
    sum=lst[low]+lst[upp]
    if(sum==inp):
        print("pairs",lst[low],lst[upp])
        low+=1
    elif(sum<inp):
        low+=1
    else:
        upp-=1