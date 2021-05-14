import weapon
from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = 20
        self.health = 100
        self.weapon = [Weapon("Decepticon Hunter", 40),
                       Weapon("Blaster Gun", 25),
                       Weapon("Laser Beam", 15)]

    def attack_dinosaur(self, dino):
        dino.health -= self.weapon[0].attack_damage
        self.power_level -= 4
