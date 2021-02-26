lst=[1,2,3,4]
op=[num**2 for num in lst]
print(op)



#even no from list

evens=[num for num in lst if num%2==0]
print(evens)

#common element
lst1=[1,2,3]
lst2=[3,4,5]
res=[num1 for num1 in lst1 for num2 in lst2 if num1==num2 ]
print(res)

