arr=[1,2,3,4,6,7,8]
element=int(input("enter element"))
arr.sort()
flag=0
low=0
upp=len(arr)-1

while(low<=upp):
    mid=(low+upp)//2
    if(element>arr[mid]):
        low=mid+1
    elif(element<arr[mid]):
        upp=mid-1
    elif(element==arr[mid]):
        flag=1
        break
if flag==0:
    print("element not found")
else:
    print("element found")
