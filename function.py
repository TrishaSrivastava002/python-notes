def func(*num):
    # use ** to pass a dictionary, * is used to make input iterable
    print(type(num))  
    sum=0
    for i in num:
      sum=sum+i

    return sum
k=func(1,2,3,4)
print(k)
      