from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def calculateArea():
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def calculateArea(self):
        return (3.14*self.radius**2)
    
class Rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def calculateArea(self):
        return self.length*self.breadth
    
circle = circle(5)
Rectangle = Rectangle(6,4)

print(f" Area of circle : {circle.calculateArea()}")

print(f" Area of rectangle : {Rectangle.calculateArea()}")