class Circle:
    def __init__(self, radius):
        self.__radius = radius 

    @property 
    # getter
    def value(self):
        return self.__radius  

    @value.setter 
    # setter
    def value(self, new_radius):
        if new_radius < 0:
            raise ValueError("Radius value must be positive")
        self.__radius = new_radius
        

r = Circle(10) 
r.value = 5
print(r.value)

