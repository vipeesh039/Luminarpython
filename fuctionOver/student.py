student={
    1000:{"id":1000,"name":"akhil","course":"btech"},
    1001:{"id":1001,"name":"ram","course":"btech"},
    1002:{"id":1002,"name":"raju","course":"mca"},
    1003:{"id":1003,"name":"manu","course":"btech"}

}

def get_student(**kwargs):
    #print(kwargs)
    id=kwargs["id"]
    prop=kwargs["property"]
    if id in student:
        print(student[id]["name"])
        if prop in student[id]:
            print(student[id][prop])
        else:
            print("not found")
    else:
        print("student does not exist")
get_student(id=1002,property="course")