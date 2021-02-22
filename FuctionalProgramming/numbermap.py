lst=[4,5,8,9,3,2]

res=list(map(lambda no:no+1 if no>5 else no-1,lst))
print(res)