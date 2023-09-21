class car:
    def __init__(self,name,company):
        self.name=name
        self.company=company

    @classmethod #instance as argument
    def change1(self,name,company):
        self.name=name
        self.company=company

    @classmethod #class as argument
    def change2(cls,name,company):
        cls.name=name
        cls.company=company    

c1=car("swift","TATA")
print(c1.name)
print(c1.company)

print("\n")

c1.change1("Mercedes","Benz")
print(car.name)
print(car.company)

print("\n")

c1.change2("Mercedes","Benz")
print(car.name)
print(car.company)
