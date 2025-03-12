#37
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def CalculateArea(self):
        pass
    @abstractmethod
    def CalculatePerimeter(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius
       

    def CalculateArea(self):
        return 3.14 * self.radius ** 2
        

    def CalculatePerimeter(self):
        return 2 * 3.14 * self.radius


class Triangle(Shape):
    def __init__(self,a,b,c,height):
        self.a = a
        self.b = b 
        self.c = c 
        self.height = height
        
    def CalculateArea(self):
        return 0.5*self.b*self.height        
    
    def CalculatePerimeter(self):
        return self.a+self.b+self.c
        

circle = Circle(5)
triangle = Triangle(2,3,4,5)

print("circle area : ",circle.CalculateArea())
print("circle perimeter : ",circle.CalculatePerimeter())

print("triangle area : ",triangle.CalculateArea())
print("triangle perimeter : ",triangle.CalculatePerimeter())