class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)

stu1=Student('张三')
stu2=Student('李四')

s=stu1+stu2
s1=stu1.__add__(stu2)
s2=stu1.__len__()

print(s1)
print(s2)