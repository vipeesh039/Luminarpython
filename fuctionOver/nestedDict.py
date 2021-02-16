student={
    1000:{"id":1000,"name":"akhil","course":"btech"},
    1001:{"id":1001,"name":"ram","course":"btech"},
    1002:{"id":1002,"name":"raju","course":"mca"},
    1003:{"id":1003,"name":"manu","course":"btech"}

}

#print(student[1000]["course"])
id=int(input("enter student id"))

if id in student:
    property = input("enter student property")
    if property in student[id]:
        print(student[id]["name"],student[id][property])
    else:
        print("invalid")
else:
    print("not found")