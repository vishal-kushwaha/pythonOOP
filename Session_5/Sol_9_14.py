from random import randint


class Die(object):
    def __init__(self, sides=6):
        self.sides = sides

    def __str__(self):
        return str(self.sides)

    def roll_die(self):
        return randint(1, self.sides)

Die_6 = Die()
Die_10 = Die(10)
Die_20 = Die(20)


def roll_10_times(dice):
    print '\nRolling Die with {} sides:'.format(dice)
    for i in range(10):
        print dice.roll_die(),

roll_10_times(Die_6)
roll_10_times(Die_10)
roll_10_times(Die_20)
