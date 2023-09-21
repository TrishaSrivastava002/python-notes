# Python Program to depict multiple inheritance
# when method is overridden in both classes

class Class1:
	def m(self):
		print("In Class1")
	
class Class2(Class1):
	def m(self):
		print("In Class2")

class Class3(Class1):
	def m(self):
		print("In Class3")
		
class Class4(Class2, Class3):
	pass
	
obj = Class4()
obj.m()
#class 2 is printed because class 2 is passed first as an argument 
# if class3 was passed first then class3 would be printed