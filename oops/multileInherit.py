class Parent:
    def phone(self):
        print("nokia")


class Child(Parent):
    def phone(self):
        print("htc")   #working

class Subchild(Child):
    def m3(self):
        print("hi hello")

sb=Subchild()
sb.phone()