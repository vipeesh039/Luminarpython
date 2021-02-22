class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total

st=Student(100,"ajay","mca",400)
st1=Student(101,"babu","bca",420)
st2=Student(102,"rocky","mca",450)
st3=Student(103,"vijay","bca",480)

students=[]

students.append(st)
students.append(st1)
students.append(st2)
students.append(st3)

upp=list(map(lambda stud:stud.name.upper(),students))
print(upp)
bonusmark=list(map(lambda st:st.total+50,students))
print(bonusmark)
