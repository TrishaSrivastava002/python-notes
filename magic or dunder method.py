class Employee:

  def __init__(self, name):
    self.name = name

  def display(self):
    print(f'Name is {self.name}')

  def __len__(self):
    i = 0
    for e in self.name:
      i += 1
    return i

  def __str__(self):
    return f"My name is {self.name}"

  #__repr__ is also same is __str__ but i dont know the difference.

  def __call__(self):
    return 'This object stores the name of an employee.'


e = Employee('Dev')
e.display()
print(f'Length of {e.name} is {len(e)}')
print(e)
print(e())

#We can also enclose the class in a different file and use these methods to access the information stored in it.

#May be we can refer these magic methods as operator overloading in c++ in some cases.
