# else will only execute when the for,while loop will the completely iterated without breaking in 
# between the loop
i=0
while i<7:
    print(i)
    i+=1
else:
  print("Error\n")   

j=0
while j<7:
    print(j)
    if j==3:
       break
    j+=1
else:
  print("Error")  