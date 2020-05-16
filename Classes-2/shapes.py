from abc import ABC, abstractmethod
import turtle 
import math
import time
t = turtle.Turtle()
t.speed(1.5)
t.shape("turtle")

class Shapes(ABC):

    def __init__(self):
        self.geometrical = True

    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def type(self):
        pass


class Calculate(ABC):                 # Interface Class

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

        
class Square(Shapes, Calculate):

    def __init__(self,s=100):
        Shapes.__init__(self)
        self.s = s

    def type(self):
        print("It is a 2-D shape")

    def getside(self):
        return self.s
    
    def setside(self, s):
        self.s = s

    def area(self):
        return self.s ** 2

    def perimeter(self):
        return 4 * self.s

    def draw(self):
        t.forward(self.s)
        t.left(90)
        t.forward(self.s)
        t.left(90)
        t.forward(self.s)
        t.left(90)
        t.forward(self.s)
        time.sleep(2)


class Rectangle(Shapes, Calculate):
    
    def __init__(self, l=200, b=100):
        Shapes.__init__(self)
        self.l = l
        self.b = b

    def type(self):
        print("It is a 2-D shape")

    def getter(self):
        return self.l, self.b

    def setter(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)

    def draw(self):
        t.forward(self.l)
        t.left(90)
        t.forward(self.b)
        t.left(90)
        t.forward(self.l)
        t.left(90)
        t.forward(self.b)
        time.sleep(2)
        
    
class Triangle(Shapes, Calculate):
    
    def __init__(self, a = 100, b = 100, c = 100):
        Shapes.__init__(self)
        self.a = a
        self.b = b
        self.c = c

    def type(self):
        print("It is a 2-D shape")

    def getsides(self):
        return self.a, self.b,self.c


    def setsides(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.s) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return (self.a + self.b + self.c)


    def draw(self):
        if self.c < self.a+self.b and self.a < self.b+self.c and self.b < self.a+self.c :
            turtle.Screen()
            t.forward(self.a)
            t.left(180-((math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2)/(2 * self.a * self.b))) * (180 / math.pi)))
            t.forward(self.b)
            t.left(180-((math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2)/(2 * self.b * self.c))) * (180 / math.pi)))
            t.forward(self.c)
            time.sleep(2)
        else :
            print("not a valid triangle")


class Pentagon(Shapes, Calculate):

    def __init__(self, s = 100):
        Shapes.__init__(self)
        self.s = s

    def type(self):
        print("It is a 2-D shape")

    def setside(self, s):
        self.s = s
    
    def getside(self):
        return self.s

    def area(self):
        return ((s**2 / 4) * (math.sqrt(5 * (5 + (2*math.sqrt(5))))))

    def perimeter(self):
        return 5 * self.s

    def draw(self):
        t.forward(self.s)
        t.left(72)
        t.forward(self.s)
        t.left(72)
        t.forward(self.s)
        t.left(72)
        t.forward(self.s)
        t.left(72)
        t.forward(self.s)
        time.sleep(2)


class Circle(Shapes, Calculate):
    
    def __init__(self, r = 100):
        Shapes.__init__(self)
        self.r = r

    def type(self):
        print("It is a 2-D shape")

    def setradius(self,r):
        self.r = r

    def getradius(self):
        return self.r

    def area(self):
        return math.pi * self.r * self.r

    def perimeter(self):
        return 2 * math.pi * self.r

    def draw(self):
        t.circle(self.r)
        


class Hexagon(Shapes, Calculate):

    def __init__(self, s = 100):
        Shapes.__init__(self)
        self.s = s

    def type(self):
        print("It is a 2-D shape")

    def setside(self, s):
        self.s = s

    def getside(self):
        return self.s

    def area(self):
        return (1.5 * math.sqrt(3) * (a**2))

    def perimeter(self):
        return 6 * self.s

    def draw(self):
        t.forward(self.s)
        t.left(60)
        t.forward(self.s)
        t.left(60)
        t.forward(self.s)
        t.left(60)
        t.forward(self.s)
        t.left(60)
        t.forward(self.s)
        t.left(60)
        t.forward(self.s)
        time.sleep(2)

class Parallelogram(Shapes, Calculate):

    def __init__(self, a = 100, b = 200):
        Shapes.__init__(self)
        self.a = a
        self.b = b

    def type(self):
        print("It is a 2-D shape")

    def setter(self, a, b):
        self.a = a
        self.b = b

    def getter(self):
        return self.a, self.b

    def area(self):
        return (b * (a * math.sin(45 * (math.pi / 180))))

    def perimeter(self):
        return 2 * (a + b)

    def draw(self):
        t.forward(self.b)
        t.left(45)
        t.forward(self.a)
        t.left(135)
        t.forward(self.b)
        t.left(45)
        t.forward(self.a)
        time.sleep(2)


class Cube(Shapes, Calculate):

    def __init__(self, s = 200):
        Shapes.__init__(self)
        self.s = s

    def type(self):
        print("It is a 3-D shape")

    def setside(self, s):
        self.s = s
    
    def getside(self):
        return self.s

    def area(self):
        return 6 * (self.s**2)

    def perimeter(self):
        print("Cannot be calculated")

    def volume(self):
        return self.s**3

    def draw(self):
        t.forward(self.s)
        t.left(90)
        t.forward(self.s)
        t.left(90)
        t.forward(self.s)
        t.left(90)
        t.forward(self.s)
        t.left(90)
        t.forward(self.s)
        t.left(50)
        t.forward(self.s / 2)
        t.left(130)
        t.forward(self.s)
        t.left(50)
        t.forward(self.s / 2)
        t.left(130)
        t.left(90)
        t.forward(self.s)
        t.right(90)
        t.forward(self.s)
        t.left(50)
        t.forward(self.s / 2)
        t.left(130)
        t.forward(self.s)
        t.left(50)
        t.forward(self.s / 2)
        t.left(180)
        t.forward(self.s / 2)
        t.right(50)
        t.right(90)
        t.forward(self.s)
        t.left(90)
        t.forward(self.s)
        t.left(90)
        t.forward(self.s)
        time.sleep(2)

class Cuboid(Shapes, Calculate):

    def __init__(self, l = 200, b = 100, h = 50):
        Shapes.__init__(self)
        self.l = l
        self.b = b
        self.h = h

    def type(self):
        print("It is a 3-D shape")

    def setter(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h
    
    def getside(self):
        return self.l, self.b, self.h

    def area(self):
        return 2 * ((self.l * self.b) + (self.b * self.h) + (self.l * self.h))

    def perimeter(self):
        print("Cannot be calculated")

    def volume(self):
        return self.l * self.b * self.h

    def draw(self):
        t.forward(self.l)
        t.left(90)
        t.forward(self.b)
        t.left(90)
        t.forward(self.l)
        t.left(90)
        t.forward(self.b)
        t.left(90)
        t.forward(self.l)
        t.left(50)
        t.forward(self.h)
        t.left(130)
        t.forward(self.l)
        t.left(50)
        t.forward(self.h)
        t.left(130)
        t.left(90)
        t.forward(self.b)
        t.right(90)
        t.forward(self.l)
        t.left(50)
        t.forward(self.h)
        t.left(130)
        t.forward(self.l)
        t.left(50)
        t.forward(self.h)
        t.left(180)
        t.forward(self.h)
        t.right(50)
        t.right(90)
        t.forward(self.b)
        t.left(90)
        t.forward(self.l)
        t.left(90)
        t.forward(self.b)
        time.sleep(2)


class Cone(Shapes, Calculate):

    def __init__(self):
        Shapes.__init__(self)
        self.angle = 45
        self.side = 200

    def type(self):
        print("It is a 3-D shape")

    def area(self):
        print("Not Calculated")

    def perimeter(self):
        print("Not calculated")

    def draw(self):
        t.left(90.0 - (self.angle) / 2.0)
        t.forward(self.side)
        t.left(180)
        t.forward(self.side)
        t.right(135)
        t.forward(self.side)
        t.right(self.angle / 2.0)
        t.right(90)
        t.penup()
        t.forward(self.side * math.sin((self.angle / 2) * (math.pi / 180)))
        t.pendown()
        t.left(90)
        t.shape("circle")
        t.shapesize(7.6, 2.5, 1)
        t.fillcolor("white")
        time.sleep(2)


# sq = Square()
# rec = Rectangle()
# tri = Triangle()
# pen = Pentagon()
# cir = Circle()
# hexa = Hexagon()
# cube = Cube()
# cuboid = Cuboid()
# cone = Cone()
# prl = Parallelogram()
# sq.draw()
# t.reset()
# t.speed(1.5)
# rec.draw()
# t.reset()
# t.speed(1.5)
# tri.draw()
# t.reset()
# t.speed(1.5)
# pen.draw()
# t.reset()
# t.speed(1.5)
# cir.draw()
# t.reset()
# t.speed(1.5)
# hexa.draw()
# t.reset()
# t.speed(1.5)
# cube.draw()
# t.reset()
# t.speed(1.5)
# cuboid.draw()
# t.reset()
# t.speed(1.5)
# cone.draw()
# t.reset()
# t.speed(1.5)
# t.shape("turtle")
# prl.draw()

