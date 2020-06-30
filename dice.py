import random

class Die:
    """
    A Multi-sided die

    Instance variables:
        sides -> the number of sides on die
    """
    def __init__(self, sides):
        self.sides = sides if sides else 6

    def describe(self):
        return 'This die has {sides} sides'.format(sides = self.sides)

    def roll(self):
        return random.randint(1, self.sides)


class Dice(Die):
    def __init__(self, dice_number, *sides):
        super().__init__(sides)

        self.dice_number = dice_number


    def describe(self):
        return 'This bucket has {dice} dice. Each dice has {sides} sides'.format(dice = self.dice_number, sides = self.sides)

    def roll_dice(self):
        total = 0
        i = self.dice_number
        while i != 0:
            value = random.randint(1, self.sides)
            print(value)
            total += value
            i -= 1

        return "TOTAL IS {total}".format(total = total)

d1 = Die(6)

bucket = Dice(3)
print(bucket.roll_dice())
