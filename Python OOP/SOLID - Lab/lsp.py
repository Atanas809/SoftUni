"""
LCP stands for - Liskov Substitution Principle
"""
from abc import abstractmethod, ABC


class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass


class RubberDuck(Duck):
    def quack(self):
        return "Squeek"


class RobotDuck(Duck):
    HEIGHT = 2

    def __init__(self):
        self.height = 0

    def quack(self):
        return 'Robotic quacking'

    def walk(self):
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
            return "landing..."
        self.height += 1
        return "Flying"

    def land(self):
        self.height = 0


rd = RubberDuck()
dd = RobotDuck()

print(rd.quack())
print(dd.quack())
print(dd.walk())
print(dd.fly())
print(dd.fly())
print(dd.fly())
print(dd.fly())
