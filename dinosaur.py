

class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.energy = 20
        self.attack_power = int(attack_power)
        self.health = 100


    def attack_robot(self, robot):
        robot.health -= self.attack_power
        self.energy -= 4
