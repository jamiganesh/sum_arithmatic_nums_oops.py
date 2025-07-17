class Rectangle:
    def __init__(self,length=1, width=1):
        self.l = length 
        self.w = width 

    def area(self):
        a = self.l * self.w 
        return a 

    def showArea(self):
        print(self.area())
    

r1 = Rectangle(20, 10) 
r1.showArea()
