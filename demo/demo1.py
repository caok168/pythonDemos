
import math
import calendar

def is_sqr(x):
    return math.sqrt(x) % 1 == 0

templist = filter(is_sqr, range(1,101))
newlist = list(templist)

print(newlist)

list = ['abcd',786,2.23,'runoob',70.2]
tinylist = [123,'runoob']

print(list)
print(tinylist)

tuple = ('abcd',786,2.23,'runoob',70.2)
print(tuple)
print(tuple[2:])

sum = lambda arg1, arg2: arg1 + arg2
print("相加后的值为：",sum(10,20))

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        return "my name is "+self.name

stu = Student('ck',30)
print(stu.name,stu.age)
print(stu.getName())

monthRange = calendar.monthrange(2019,5)
print(monthRange)
