import pygame
import sys
from scripts.entities import PhysicsEntity
from scripts.utils import load_image

class Game:
    def __init__(self):
        pygame.init()

        #set display
        pygame.display.set_caption("Platformer in Pygame")
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        #instantiate player
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        #load all assets
        self.assets = {
            'player': load_image("entities/player.png")
        }


    def run(self):
        #main game loop
        while True:

            self.screen.fill((14, 219, 248))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)
            
            for event in pygame.event.get():

                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                #keyboard inputs

                #when pressed
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_LEFT):
                        self.movement[0] = True
                    if(event.key == pygame.K_RIGHT):
                        self.movement[1] = True
                #when released
                if(event.type == pygame.KEYUP):
                    if(event.key == pygame.K_LEFT):
                        self.movement[0] = False
                    if(event.key == pygame.K_RIGHT):
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60) #runs at 60 fps, dynamic sleep function

Game().run()
