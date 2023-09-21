import os
# make dictionary

#if a directory named data already exist it will not try to make a directory 
# with the same name
if(not os.path.exists("data")):
   os.mkdir("data")

for i in range(5):
    os.mkdir(f"data/file{i+1}")
    # os.rename(f"data/file{i+1}",f"data/name{i+1}")

folder=os.listdir("data")
print(type(folder))

for f in folder:
    print(f"data/{f}")