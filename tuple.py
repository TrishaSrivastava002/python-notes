t = (1,2,3,4,5,6,7)
print(t[2])
print(t[2:5])
print(t[0:3])
#t.remove(2)
print(sum(t))
print(t.index(1)) #returns index of the element entered
# t[1]= 876 cannot update tupil like this
# k = (5) cannot initialize a single element tupil like this should have a ,
k=(5,)
print(k.count(5))
# k.remove(5)
print(k)
l=list(t)
print(l)
# can initialize tuple without any brackets  
my_tuple="Tish",21,"hey","you","Srivas"
# no.of elemnets should be same as variable initialization on the left side
name,*age,last=my_tuple
print(name)
print(age)
print(last)

tup=(1,2,3,4,5,6)
i1,*i2,i3=tup
print("i1= ",i1)
print("i2= ",i2) # i2 makes a list of all the items between i1 and i2 and stores it
print("i3= ",i3)



