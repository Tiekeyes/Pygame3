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

    def run(self):
        #main game loop
        while True:
            
            self.screen.blit(self.img, (100, 200))
            
            for event in game.event.get():
                if(event.type == game.QUIT):
                    game.quit()
                    sys.exit()

            game.display.update()
            self.clock.tick(60) #runs at 60 fps, dynamic sleep function

Game().run()
