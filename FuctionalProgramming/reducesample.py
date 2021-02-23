from functools import reduce
lst=[2,4,5,6,7]

sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum)

ma=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(ma)
