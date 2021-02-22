class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name

st=Student(100,"ajay","mca",400)
st1=Student(101,"babu","bca",420)
st2=Student(102,"rocky","mca",450)
st3=Student(103,"vijay","bca",480)

students=[]

students.append(st)
students.append(st1)
students.append(st2)
students.append(st3)

#mcastud=list(filter(lambda stud:stud.course=="mca",students))
#for stud in mcastud:
#    print(stud)      #normal method of filter

mca_stud=list(map(lambda stud:stud.name,list(filter(lambda stud:stud.course=="mca",students))))
print(mca_stud)   #single line method using map






max_mark=max(list(map(lambda stud:stud.total,students)))
print(max_mark)    #max using map

min_mark=min(list(map(lambda stud:stud.total,students)))
print(min_mark)    #min using map