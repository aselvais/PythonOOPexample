"""
Class for Dogs inheriting from Animals
"""
from libs.animals.Animals import Animals


class Dog(Animals):
    _health = 50
    _damage = 20

    def __init__(self):
        super().__init__()
        print('Init a new Dog')

    def talk(self):
        print('*** WOOOFFF!!!!!!! ***')
