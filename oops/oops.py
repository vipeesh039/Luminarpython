class Person:
    def set_values(self,age,name):
        self.age=age
        self.name=name
    def print_values(self):
        print(self.age)
        print(self.name)

#create objects

obj=Person()
obj.set_values(25,"ajay")
obj.print_values()

obj1=Person()
obj.set_values(26,"vijay")
obj.print_values()