import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

        #set display
        pygame.display.set_caption("Platformer pygame")
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.img = pygame.image.load("data\images\clouds\cloud_1.png")
        self.img.set_colorkey((0, 0, 0))
        self.img_pos = [160, 260]
        self.movement = [False, False]

        #create collision area
        self.collision_area = pygame.Rect(50, 50, 300, 50)


    def run(self):
        #main game loop
        while True:

            self.screen.fill((14, 219, 248))

            #define the cloud's hitbox
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            
            #draw collision area on the screen with color based on if the hitbox collides with it
            if(img_r.colliderect(self.collision_area)):
                pygame.draw.rect(self.screen,(0, 100, 255), self.collision_area)
            else:
                 pygame.draw.rect(self.screen,(0, 50, 255), self.collision_area)

            #then, draw the cloud (layering is done by order in Pypygame)
            self.img_pos[1] += self.movement[1] - self.movement[0]
            self.screen.blit(self.img, self.img_pos)
            
            for event in pygame.event.get():

                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                #keyboard inputs

                #when pressed
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_UP):
                        self.movement[0] = True
                    if(event.key == pygame.K_DOWN):
                        self.movement[1] = True
                #when released
                if(event.type == pygame.KEYUP):
                    if(event.key == pygame.K_UP):
                        self.movement[0] = False
                    if(event.key == pygame.K_DOWN):
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60) #runs at 60 fps, dynamic sleep function

Game().run()
