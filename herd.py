import random

from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        # self.herd = [Dinosaur("Indoraptor"),
        #              Dinosaur("Indominus Rex"),
        #              Dinosaur("Spinosaurus")]
        self.team_dino = []

    def create_dino_herd(self):
        while len(self.team_dino) < 3:
            self.team_dino.append(Dinosaur(input("Name your Dinosaur Fighter"), random.randint(1, 10)))
