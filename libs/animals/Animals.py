"""
Class for Animals
"""
class Animals:
    """
    Animals
    """
    """ Name of the animal """
    _name = ''
    """ Health of the animal """
    _health = 10
    """ Damage this animal can cause """
    _damage = 10
    """ Is the animal alive or not """
    _alive = True

    def __init__(self):
        """Constructor
        """
        print('Init a new Animal')

    def set_name(self, name=''):
        """
        Gives a name to this animal

        Args:
            name (str, optional): [description]. Defaults to ''.
        """
        self._name = name

    def say_my_name(self):
        """The animal says his name
        """
        print('My name is ' + self._name)

    def talk(self):
        """Animal will say something
        """
        print('I can\'t speak yet ...')

    def show_health(self):
        """Displays animal's health
        """
        print(self._name + '\'s health is ' + str(self._health))

    def attack(self, enemy):
        """Animal attacks other animal and sets damage

        Args:
            enemy (Animal): Enemy animal to attack
        """
        print(self._name + " attacks " + enemy._name)
        enemy._health = enemy._health - self._damage
        if enemy._health <= 0:
            enemy._alive = False
            enemy._health = 0
        enemy.show_health()

    def show_living_status(self):
        """Displays animals dead or alive
        """
        if self._alive is True:
            print(self._name + " is alive!!!!")
        else:
            print(self._name + " is DEAD !!!! ... :-( ")
