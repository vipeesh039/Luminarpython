class Parent:
    def phone(self):
        print("nokia")


class Child(Parent):
    def phone(self):
        print("htc")

p=Child()
print(p)