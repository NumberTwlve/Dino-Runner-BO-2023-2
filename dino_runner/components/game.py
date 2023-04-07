import pygame
import os
from dino_runner.components import texts_utils
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, RUNNING, GAME_OVER, SCREEN
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

#MUSIC_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
#pygame.init()
#pygame.mixer.init()

#audio_file = os.path.join(MUSIC_DIR, "Other/music.mp3")

#pygame.mixer.music.load(audio_file)
#pygame.mixer.music.play()

#while pygame.mixer.music.get_busy():
   # continue
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_screen = 0
        self.y_pos_screen = 0
        self.x_pos_cloud = 0
        self.y_pos_cloud = 100
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.death_count = 0
        self.pause = False
        
    def run(self):
        # Game loop: events - update - draw
        self.running = True
        

        while self.running:
            if self.pause == False:
                self.events()
                self.update()
                self.draw()
            else:
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    self.pause = False
                
                    
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 
                self.playing = False
                pygame.quit()      
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()


    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            if user_input[pygame.K_p] and self.pause == False:
                text, text_rect = texts_utils.get_message('Press any Key to Restar', 30)
                self.screen.blit(text, text_rect)
                self.pause = True

            self.player.update(user_input)
            self.obstacle_manager.update(self.game_speed, self.player)
            self.power_up_manager.update(self.game_speed, self.points, self.player)
            self.points += 1
            if self.points % 200 == 0:
                self.game_speed += 10
            if self.player.dino_dead:
                self.playing = False
                self.death_count += 1
         
        

    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_background()
            self.draw_screen()
            self.draw_cloud()
            self.draw_score()
            self.player.draw(self.screen)
            self.obstacle_manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)
        
        else:
            self.draw_menu()
           

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = SCREEN.get_width()
        self.screen.blit(SCREEN, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(SCREEN, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(SCREEN, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_screen(self):
        self.screen.blit(SCREEN, (self.x_pos_screen, self.y_pos_screen))
           
    
    def draw_cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 3000
        self.x_pos_cloud -= self.game_speed

    def draw_score(self):
        score, score_rect = texts_utils.get_message('points: ' + str(self.points), 20, 900, 40)
        self.screen.blit(score, score_rect) 

    def draw_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)   
        self.print_menu_element()



                

    def print_menu_element(self):
        if self.death_count == 0:
            text, text_rect = texts_utils.get_message('Press any Key to Star', 30)
            self.screen.blit(text, text_rect)
            self.screen.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        else:
            text, text_rect = texts_utils.get_message('Press any Key to Restar', 30) 
            score, score_rect = texts_utils.get_message('Your score: ' + str(self.points), 30, heigth=SCREEN_HEIGHT//2 + 50 )  
            self.screen.blit(text, text_rect)     
            self.screen.blit(score, score_rect)
            self.screen.blit(GAME_OVER, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 130))
    

    def reset(self):
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
 #   def pause(self):

 #       pause_game = True

#        while pause_game:
 #           for event in pygame.event.get():
  #              if event.type == pygame.QUIT:
   #                 pygame.quit()
    #                quit()

     #           if event.type == pygame.KEYDOWN:
      #              if event.key == pygame.K_c:
       #                 text, text_rect = texts_utils.get_message('Press any Key to Restar', 30)
        #                self.screen.blit(text, text_rect) 

         #               pause_game = False

          #          elif event.key == pygame.K_q:
           #             pygame.quit()
            #            quit()



               
