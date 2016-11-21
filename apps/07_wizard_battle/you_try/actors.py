import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return 'Creature {} of the level {}'.format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(
          self.name, creature.name
        ))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print("You roll {}...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard triumphed over {}".format(creature.name))
            return True
        else:
            print("The wizard has been DEFEATED!!!")
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        return super().get_defensive_roll()/2


class Dragon(Creature):
    def __init__(self,name, level, scaliness, breathes_fires):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breathes_fires = breathes_fires


    def get_defensive_roll(self):
        base_roll =  super().get_defensive_roll()/2
        # fire_modifier = None
        # if self.breathes_fires:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1
        fire_modifier = 5 if self.breathes_fires else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier

