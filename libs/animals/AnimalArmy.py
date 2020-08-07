"""
Class for creating an army of animal
"""
from libs.animals.Dog import Dog
from libs.animals.Duck import Duck


class AnimalArmy:
    """Generates an army of animals

    Args:
        animal_type (str, optional): duck or dog. Defaults to 'duck'.
        army_size (int, optional): Number of animal in the army. Defaults to 10.
    """

    animals = []

    def __init__(self, animal_type='Duck', army_size=10):
        """Generates an army of animals

        Args:
            animal_type (str, optional): duck or dog. Defaults to 'Duck'.
            army_size (int, optional): Number of animal in the army. Defaults to 10.
        """
        for i in range(army_size):
            if animal_type == 'Duck':
                _a = Duck()
            if animal_type == 'Dog':
                _a = Dog()
            _a.set_name(animal_type + str(i))
            self.animals.append(_a)
        print('Army of ' + str(army_size) + ' ' + animal_type + 's created!')

    def attack(self, enemy):
        """Attacking the enemy animal with the army, each animal at a time

        Args:
            enemy (Animal): Enemy animal
        """
        print('Army attack on ' + enemy._name)
        for i in self.animals:
            i.attack(enemy)
