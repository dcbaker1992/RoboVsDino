from herd import Herd
from fleet import Fleet


class Battlefield:
    def __init__(self):
        self.dinosaur_herd = Herd()
        self.robot_fleet = Fleet()
        self.robot_defeated = []
        self.dinosaurs_defeated = []


print('Welcome to Dinosaurs Vs Robots!')
