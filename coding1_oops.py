#A class with using class method
class Person:
    def __init__(self,name= "Unknown", age= None):
        self.name = name 
        self.age = age 

    @classmethod 
    def get_name(cls,name):
        return cls(name=name) 

    @classmethod 
    def get_age(cls,age):
        return cls(age=age) 

    def showData(self):
        print(f"my name is {self.name}, i am {self.age} years old.")       


p1 = Person.get_name("ganesh")
p2 = Person("Ganesh",26) 
p2.showData()



