marks=[1,34,56,23,78,90]
for index,mark in enumerate(marks):
    print(index,mark)

# starts indexing from 1
for mark,index in enumerate(marks,start=1):
    print(index,mark)    