num=int(input("enter number"))

while(num!=0):#123!=0   12!=0   0!=0
    digit=num%10#digit=123%10=3     12%10=2    1%10=1
    print(digit)#321
    num//=10#num=num//10=123//10=12  12//10=1  1//10=0