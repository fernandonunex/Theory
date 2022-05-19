import random
from time import sleep

class Die():
    """ A simple attempt to model a Die"""

    def __init__(self, sides=6) -> None:
        self.sides = sides

    
    def roll_die(self):
        print('Rolling the die')
        print('.')
        sleep(0.5)
        print('.')
        sleep(0.5)
        print('.')
        sleep(0.5)
        print('.')
        sleep(0.5)
        print(random.randint(1,self.sides))


if __name__ == '__main__':
    dice_6_sides = Die(6)

    dice_6_sides.roll_die()