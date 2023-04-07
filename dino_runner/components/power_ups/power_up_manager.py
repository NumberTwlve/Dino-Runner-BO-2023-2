import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components import texts_utils
      
class PowerUpManager:
    def __init__(self):
        self.power_ups = []

    def update(self, game_speed, points, player):
        move_type = random.randint(0, 1)
        if len(self.power_ups) == 0 and points % 200 == 0 and move_type == 0: 
            self.power_ups.append(Hammer()) 
        elif len(self.power_ups) == 0 and points % 200 == 0 and move_type == 1:
            self.power_ups.append(Shield())          
                                 
        for power_up in self.power_ups:
            if power_up.used or power_up.rect.x < -power_up.rect.width:
                self.power_ups.pop()
            if power_up.used:
                player.set_power_up(power_up)
            power_up.update(game_speed, player)                                 

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)