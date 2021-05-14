from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = -10
        self.health = 100
        self.weapon = [Weapon("Decepticon Hunter", 40),
                       Weapon("Blaster Gun", 25),
                       Weapon("Laser Beam", 15)]


