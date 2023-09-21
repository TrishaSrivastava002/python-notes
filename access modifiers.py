class emp:
    def __init__(self):
        self.__val=32 #private member
        self._age=44 #protected member

e=emp()
# print(e.__val)  cannot be acessed
print(e._emp__val) #can be indirectly accessed through name mangling    
print(e._age) #protected member can be accessed by child and parent class     

    