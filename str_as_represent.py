class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name 

    # Here, we did not mention a custom method name; instead
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")    
    

p1 = Person("Ganesh", "Jami") 
print(p1)    