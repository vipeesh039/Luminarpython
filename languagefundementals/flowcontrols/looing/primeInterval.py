# Python program to display all the prime numbers between 10 and 25
lower = 10
upper = 25
print("Prime numbers between",lower,"and",upper)
for num in range(lower,(upper+1)):
   if num>1:
       for i in range(2,num):
           if (num%i)==0:
               break
       else:
           print(num)