class Maths:
    def add(self):
        print("1st")

    def add(self,num1):
        print("2nd")

    def add(self,num1,num2):
        print("3rd")

math=Maths()
math.add(10,20)
math.add(10)
math.add()   #recent one working