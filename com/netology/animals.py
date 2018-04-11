class Animal:

    color = None
    age = 0
    weight = 0
    position = 0

    def __init__(self):
        self.color = None
        self.age = 0
        self.weight = 0
        self.position = 0

    def reproduce(self):
        pass  # abstract

    def talk(self, sound):
        print(sound)

    def move(self, position):
        self.position = position
        print('Moving to position {}'.format(position))

    def eat(self, amount_of_food):
        self.weight += amount_of_food / 2  # let's imagine that 50% of food is absorbed


class Mammal(Animal):

    def reproduce(self):
        print('Giving birth to a new mammal...')


class Cow(Mammal):

    def talk(self, sound='Muu-u-u!'):
        super(Cow, self).talk(sound)


class Goat(Mammal):

    def talk(self, sound='Bie-e-e!'):
        super(Goat, self).talk(sound)


class Sheep(Mammal):

    def talk(self, sound='Mie-e-e!'):
        super(Sheep, self).talk(sound)


class Pig(Mammal):

    def talk(self, sound='Hru-hru!'):
        super(Pig, self).talk(sound)


class Bird(Animal):

    altitude = 0

    def reproduce(self):
        print('Laying an egg...')

    def ascend(self, altitude):
        self.altitude += altitude
        print('The bird is ascending to altitude {}'.format(altitude))

    def descend(self, altitude):
        if self.altitude == 0:
            print('Ground level, nowhere to descend!')
        elif self.altitude < altitude:
            print('Descend can not be more then ascend, aborting...')
        else:
            self.altitude -= altitude
            print('The bird is descending to altitude {}'.format(altitude))


class Duck(Bird):

    def talk(self, sound='Quack-quack!'):
        super(Duck, self).talk(sound)

    def swim(self):
        print('The duck is swimming...')


class Chicken(Bird):

    def talk(self, sound='Ko-ko-ko!'):
        super(Chicken, self).talk(sound)


class Goose(Bird):

    def talk(self, sound='Ga-ga-ga'):
        super(Goose, self).talk(sound)
