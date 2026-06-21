import pygame as game
import sys

class Game:
    def __init__(self):
        game.init()

        #set display
        game.display.set_caption("Platformer Game")
        self.screen = game.display.set_mode((640, 480))
        self.clock = game.time.Clock()

        self.img = game.image.load("data\images\clouds\cloud_1.png")
        self.img.set_colorkey((0, 0, 0))
        self.img_pos = [160, 260]
        self.movement = [False, False]

        self.collision_area = game.Rect(50, 50, 300, 50)


    def run(self):
        #main game loop
        while True:

            self.screen.fill((14, 219, 248))

            self.img_pos[1] += self.movement[1] - self.movement[0]
            self.screen.blit(self.img, self.img_pos)
            
            img_r = game.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if(img_r.colliderect(self.collision_area)):
                game.draw.rect(self.screen,(0, 100, 255), self.collision_area)
            else:
                 game.draw.rect(self.screen,(0, 50, 255), self.collision_area)

            for event in game.event.get():

                if(event.type == game.QUIT):
                    game.quit()
                    sys.exit()

                #keyboard inputs

                #when pressed
                if(event.type == game.KEYDOWN):
                    if(event.key == game.K_UP):
                        self.movement[0] = True
                    if(event.key == game.K_DOWN):
                        self.movement[1] = True
                #when released
                if(event.type == game.KEYUP):
                    if(event.key == game.K_UP):
                        self.movement[0] = False
                    if(event.key == game.K_DOWN):
                        self.movement[1] = False

            game.display.update()
            self.clock.tick(60) #runs at 60 fps, dynamic sleep function

Game().run()
