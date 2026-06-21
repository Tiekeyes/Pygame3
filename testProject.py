import pygame as game

game.init()

screen = game.display.set_mode((640, 640))
clock = game.time.Clock()

running = True
while running:
    for event in game.event.get():
        if(event.type == game.QUIT):
            running = False

    game.display.update()
    clock.tick(60) #runs at 60 fps, dynamic sleep function

game.quit()

