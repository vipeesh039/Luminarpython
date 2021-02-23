class Employee:
    def __init__(self,id,name,desig,exp,sal):
        self.id=id
        self.name=name
        self.desig=desig
        self.exp=exp
        self.sal=sal
    def __str__(self):
        return self.name
lst=[]
f=open("employees","r")
for lines in f:
    id,name,desig,exp,sal=lines.rstrip("\n").split(",")
    #print(id,name,desig,exp,sal)
    lst.append(Employee(id,name,desig,exp,sal))

developers=list(filter(lambda emp:emp.desig=="developer",lst))
for emp in developers:
    print(emp.name)







