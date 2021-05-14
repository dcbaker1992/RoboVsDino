from attack_type import Attack_type

class Dinosaur:
    def __init__(self, type):
        self.type = type
        self.energy = -10
        self.health = 100
        self.attack_type = [Attack_type("Claw Slash", 15),
                            Attack_type("Chomp", 30),
                            Attack_type("Maul", 25)]




