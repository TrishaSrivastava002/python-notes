x = 10 # global variable
print("global x is",x)
def my_function():
  global x
  x = 4
  y = 5 # local variable 
  print("y is",y)

my_function()

print("x is",x)

# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function