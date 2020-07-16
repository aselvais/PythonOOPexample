from libs.animals.Dog import Dog
from libs.animals.Duck import Duck

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
