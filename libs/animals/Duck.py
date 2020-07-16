"""
Class for Ducks inheriting from Animals
"""
from libs.animals.Animals import Animals


class Duck(Animals):
    _health = 10
    _damage = 3

    def __init__(self):
        super().__init__()
        print('Init a new Duck')

    def talk(self):
        print('*** KWACK!!! ***')
