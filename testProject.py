import pygame as game
import sys
game.init()



screen = game.display.set_mode((640, 640))
clock = game.time.Clock()

#set display name
game.display.set_caption("Platformer Game")

running = True
while running:
    for event in game.event.get():
        if(event.type == game.QUIT):
            game.quit()
            sys.exit()
            running = False

    game.display.update()
    clock.tick(60) #runs at 60 fps, dynamic sleep function

game.quit()

