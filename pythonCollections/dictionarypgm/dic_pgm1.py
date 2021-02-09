student={"rol":1000,"name":"akhil","course":"bca"}

print(student["name"]) #value accessing

if "total" in student:
    print("exist")
else:
    #print("not exist") #checking "total" exist or not
    student["total"]=150 #adding new key-value
print(student)

student["total"]+=50 #updating value
print(student["total"])