import pygame
from dino_runner.utils.constants import SCREEN_WIDTH, DINO_DEAD

class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect):
            if not player.hammer:
                    if not player.shield:
                        player.image = DINO_DEAD
                        pygame.time.delay(400)
                        player.dino_dead = True 
        if self.rect.colliderect(player.dino_rect):
            if player.hammer:
                    self.rect.x += 1000
    def draw(self, screen):
        screen.blit(self.image, self.rect)  