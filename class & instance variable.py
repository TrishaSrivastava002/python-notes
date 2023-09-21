class emp:
    company="Google" #class variable
    num=0 #class variable
    def __init__(self,name):
        self.name=name
        self.age=21
        emp.num+=1
    def info(self):                     #class variable   ***********#instance variable ****************
        print(f"this is our employee number {emp.num}, {self.name} aged {self.age} at {self.company}")  

e=emp("Anna")
e.age=452
e.info() 

f=emp("Bell")
f.age=42
f.company="Microsoft" #instance variable
f.info() 