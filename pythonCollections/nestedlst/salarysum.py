employees=[
    [100,"akhil","developer",2,"5000"],
    [101,"arjun","developer",2,"3000"],
    [102,"arun","devops",1,"7000"],
    [103,"babu","qt",1,"4000"],
]
total=0
for emp in employees:

    salary=int(emp[4])
    total=total+salary
print(total)


sallist=[]
for emp in employees:
    sallist.append(int(emp[4]))
print(max(sallist))
