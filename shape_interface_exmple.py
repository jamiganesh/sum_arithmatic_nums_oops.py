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
    
class Square(Shape):
    def __init__(self,side):
        self.side = side 

    def area(self):
        return self.side * self.side 
    
    def perimeter(self):
        return self.side * 4
               


s1 = Square(6)
print(s1.area())
print(s1.perimeter())


r1 = Rectangle(4,2) 
print(r1.area())    
print(r1.perimeter())  






