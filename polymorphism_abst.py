from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        a=5
        print("area of Circle:" ,round(3.14 *a),2)

class Triangle(Shape):
    def area(self):
        base=3
        height=7
        print("the are of triangle:",0.5 *base*height)

class Rectangle(Shape):
    def area(self):
        length=9
        width=6
        print("the are of rectangele:",length*width)

circle=Circle()
triangle=Triangle()
rectangle=Rectangle()
shapes=[circle,rectangle,triangle]
for shape in shapes:
    shape.area()



