#36
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Lion(Animal):
    def sound(self):
        print("lion sound ")


class Tiger(Animal):
    def sound(self):
        print("tiger sound")

lion = Lion()
lion.sound()
tiger = Tiger()
tiger.sound()
