class Parent:
    def m1(self):
        print("hi")


class Child(Parent):
    def m2(self):
        print("hello")

class Subchild(Child):
    def m3(self):
        print("hi hello")

sb=Subchild()
sb.m3()
sb.m2()
sb.m1()

ch=Child()
#ch.m3()
ch.m2()
ch.m1()

p=Parent()
#p.m3()
#p.m2()
p.m1()