import pygame
from dino_runner.utils.constants import SCREEN_WIDTH, DINO_DEAD, JUMPING, RUNNING, DUCKING

class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect):
            player.image = DINO_DEAD
            pygame.time.delay(400)
            player.dino_dead = True    
    def draw(self, screen):
        screen.blit(self.image, self.rect)  