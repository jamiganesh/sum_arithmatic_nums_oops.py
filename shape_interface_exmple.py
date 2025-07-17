from abc import ABC, abstractmethod
import math 

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass 

    @abstractmethod 
    def perimeter(self):
        pass 

class Rectangle(Shape):
    def __init__(self, lengh, width):
        self.l = lengh
        self.w = width 

    def area(self):
        return self.l * self.w 
    
    def perimeter(self):
        return 2*(self.l + self.w)
    

r1 = Rectangle(4,2) 
print(r1.area())    






