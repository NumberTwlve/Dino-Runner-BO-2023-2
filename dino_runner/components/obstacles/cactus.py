import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class Cactus(Obstacle):
    

    def __init__(self):
        self.Y_POS_CACTUS = 0
        self.list_type = random.randint(0, 1)
        self.type = random.randint(0, 2)
        self.list = [SMALL_CACTUS[self.type], LARGE_CACTUS[self.type]]
        
        image = self.list[self.list_type]

        if self.list_type == 1:
            self.Y_POS_CACTUS = 300
        else:
            self.Y_POS_CACTUS = 320    

        super().__init__(image)
        self.rect.y = self.Y_POS_CACTUS