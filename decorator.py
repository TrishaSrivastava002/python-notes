def solve(func):
    def modified_func(*args,**kwargs): #used to pass input
        print("Good Morning")
        func(*args,**kwargs) #input passed in modified_func can be used as parameters
        print("Good night")
    return modified_func    

@solve
def func():
    print("Good Afternoon")


@solve
def add(a, b):
  print(a+b)

print("Func function returns :")
func()
print("\n")
print("Add function returns :",add(123,567)) 
   

