import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.obstacle import Obstacle

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        

    def update(self, game_speed, player):
        move_type = random.randint(0, 1)
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus())if move_type == 0 else self.obstacles.append(Bird())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.pop()
           
        
         #   if Obstacle.rect.colliderect(player.dino_rect):
          #      if player.hammer:
           #         self.obstacles.pop(obstacle)
         
            obstacle.update(game_speed, player)
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            

