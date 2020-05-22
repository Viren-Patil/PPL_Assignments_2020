class Animals:

    def __init__(self):
        self.__eyes = 2       # Private varible __eyes
        self._living = True   # Protected variable _living
        self.legs = 4         # Public varibale legs

    def seteyes(self, eyes):
        self.__eyes = eyes

    def geteyes(self):
        return self.__eyes

    def getliving(self):
        return self._living

    def setliving(self, living):
        self._living = living

    def getlegs(self):
        return self.legs
    
    def setlegs(self, legs):
        self.legs = legs
        



class Lion(Animals):

    def eats(self):
        print("Lion eats meat!")

    def color(self):
        print("Color of Lion is Grayish Yellow!")

    def sound(self):
        print("A lion roars!")

    def typeOfAnimal(self):
        print("Lion is a carnivorous animal")


class Tiger(Animals):

    def eats(self):
        print("A tiger eats meat!")

    def color(self):
        print("Color of Tiger is orange with black stripes!")

    def sound(self):
        print("A tiger roars!")

    def typeOfAnimal(self):
        print("Tiger is a carnivorous animal")

class Giraffe(Animals):

    def eats(self):
        print("Giraffe eats leaves off the trees!")

    def color(self):
        print("Giraffe has patterns of dark brown, orange, or chestnut spots broken up by white or cream-coloured stripes!")

    def sound(self):
        print("A giraffe makes a flute like sound!")

    def typeOfAnimal(self):
        print("Giraffe is a herbivorous animal")

class Zebra(Animals):

    def eats(self):
        print("Zebra eat grass!")

    def color(self):
        print("A Zebra has black and white stripes on its body.")

    def sound(self):
        print("Zebras either bark, bray or snort!")

    def typeOfAnimal(self):
        print("Zebra is a herbivorous animal")

class Monkey(Animals):

    def eats(self):
        print("Monkey eats vegetables and fruits")

    def color(self):
        print("Color of monkey is brown")

    def sound(self):
        print("A monkey makes a screeching sound!")

    def typeOfAnimal(self):
        print("LMonkey is a herbivorous animal")

class Dog(Animals):

    def eats(self):
        print("A dog eats meat, veggies, dog-food etc.!")

    def color(self):
        print("A dog could be of any color, it depends on the breed.")

    def sound(self):
        print("A dog barks!")

    def typeOfAnimal(self):
        print("Dog is an omnivorous animal")

class Rat(Animals):

    def eats(self):
        print("LRat eats flesh, leftover food, garbage etc.!")

    def color(self):
        print("Rats can be white, black or gray in color!")

    def sound(self):
        print("A rat squeaks!")

    def typeOfAnimal(self):
        print("Rat is an omnivorous animal")

class Kangaroo(Animals):

    def eats(self):
        print("A Kangaroo eats vegetables, plants, leaves!")

    def color(self):
        print("A Kangaroo is blue-grey or brown in color!")

    def sound(self):
        print("A Kangaroo growls or barks!")

    def typeOfAnimal(self):
        print("Kangaroo is a herbivorous animal")

class PolarBear(Animals):

    def eats(self):
        print("Polar Bear eats meat!")

    def color(self):
        print("Color of Polar Bear is off white or bright white.")

    def sound(self):
        print("A polar bear makes sounds like hissing, growling or champing of teeth!")

    def typeOfAnimal(self):
        print("Polar Bear is a carnivorous animal")

class Deer(Animals):

    def eats(self):
        print("A deer eats plants, leaves!")

    def color(self):
        print("Color of Lion is Reddish brown or Grayish brown!")

    def sound(self):
        print("A Deer makes a grunting sound or a bleating sound!")

    def typeOfAnimal(self):
        print("Deer is a herbivorous animal")


mon = Monkey()
# print(mon.__eyes)    This gives an error as we cannot access private variables directly.
print(mon._Animals__eyes)  # This is one way to access the private variables.
print(mon._living)
print(mon.legs)
mon.eats()
mon.color()
mon.sound()
mon.typeOfAnimal()



