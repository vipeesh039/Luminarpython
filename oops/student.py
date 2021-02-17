class Student:

    cname="sng" #static/class variable
    def create_student(self,rollno,name):
        self.rollno=rollno #instance variable
        self.name=name

    def print_student(self):
        print(self.rollno)
        print(self.name)
        print(self.cname)

obj=Student()
obj.create_student(10,"ram")
obj.print_student()
#print(obj.rollno)  #print outside class