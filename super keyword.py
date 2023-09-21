class teacher:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")  

class student(teacher):
    def __init__(self,name,age,reg):
        super().__init__(name,age)
        self.reg=reg


t=teacher("Peter",67)
s=student("Anna",24,207)
s.intro()   

print(s.name)       
print(s.age)  
print(s.reg)                               