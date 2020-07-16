"""
Main file instanciating the objects from the classes and
making them interacting with each others
"""
from libs.animals.Dog import Dog
from libs.animals.Duck import Duck
from libs.animals.AnimalArmy import AnimalArmy

print("\n\n")

scoobydoo = Dog()
scoobydoo.set_name('Scooby Doo')
scoobydoo.say_my_name()
scoobydoo.talk()
scoobydoo.show_health()

print("\n\n")

fido = Dog()
fido.set_name('Fido')
fido.say_my_name()
fido.talk()
fido.show_health()

print("\n")

ducky = Duck()
ducky.set_name('Ducky')
ducky.say_my_name()
ducky.talk()
ducky.show_health()

print("\n")

for i in range(17):
    ducky.attack(fido)
    fido.show_living_status()

print("\n")

scoobydoo.attack(ducky)

print("\n")

duckArmy = AnimalArmy('duck', 10)

print("\n")

duckArmy.attack(scoobydoo)

print("\n")

scoobydoo.show_living_status()
scoobydoo.talk()
scoobydoo.talk()
scoobydoo.talk()