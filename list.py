a =[1,2,3,4,5,6] # like an array starts with 0
print("a\n",a)
print(a[0])
print(a[4])
a[0] = 98
print(a[0])

b= [2,"tri", 8.97543,'a',76,90] # can create list with different data types
print("b\n",b)
print(b[1:4])
print(b[-5:-3])
print("b[::2] is",b[::2])
print(b[1:5:2])
c = [4,2,6,1,5,8]
print("c\n")
c.sort()
c.reverse()
c.append(56)  # adds at the end of list
c.append(66)
c.insert(2,1098) # inserts at 2
c.pop(2) # removes from index 2
c.remove(56) # removes mentioned element
print(c)
d=sorted(c)
print(d)

e=[x*x for x in d]
print(e)
l=[1,3,2,76,32,100,99]
p=[5]*6
print(p)
p.append(["Grey","50"])
l.sort()
print(l)