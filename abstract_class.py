from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area (self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area (self):
        return self.width * self.height
    

if __name__ == "__main__":
    rect = Rectangle(4,5)
    print("Area of Rectangle:", rect.area())
        