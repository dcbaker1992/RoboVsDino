from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.fleet = [Robot("Optimus Prime", 5000, 100, Weapon("Decepticon Hunter", 40)),
                    Robot("Ultron", 3000, 100, Weapon("Blaster Gun", 25)),
                    Robot("Sentinels", 1500, 100, Weapon("Laser Beam", 15))]