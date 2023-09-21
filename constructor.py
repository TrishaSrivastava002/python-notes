class car:
    def __init__(self,model,power):
        self.model=model
        self.power=power
        print("constructor is automatically invoked")

    def info(self):
        print(f"The latest model is {self.model} with the horse power of {self.power}")

ferrari=car("Bugatti",990)
ferrari.info()    
