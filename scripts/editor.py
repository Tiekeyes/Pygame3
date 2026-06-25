import pygame
import sys
from utils import load_images
from tilemap import Tilemap

RENDER_SCALE = 2.0 

class Editor:
    def __init__(self):
        pygame.init()

        self.FPS = 60

        #set display
        pygame.display.set_caption("Level Editor")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock() 

        #load all assets
        self.assets = {
            'decor': load_images("tiles/decor"),
            'grass': load_images("tiles/grass"),
            'large_decor': load_images("tiles/large_decor"),
            'stone': load_images("tiles/stone")
        }

        self.movement = [False, False, False, False]
        
        #create tilemap
        self.tilemap = Tilemap(self, tile_size = 16)

        #instantiate camera position
        self.scroll = [0, 0]

        self.tile_list = list(self.assets)
        self.tile_group = 0
        self.tile_variant = 0
        self.clicking = False
        self.right_clicking = False
        self.shift = False

    def run(self):
        #main game loop
        while True:

            self.display.fill((0, 0, 0))

            #render the tilemap
            self.scroll[0] += (self.movement[1] - self.movement[0]) * RENDER_SCALE
            self.scroll[1] += (self.movement[3] - self.movement[2]) * RENDER_SCALE
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            self.tilemap.render(self.display, offset=render_scroll)

            #display the current tile selected
            current_tile_img = self.assets[self.tile_list[self.tile_group]][self.tile_variant].copy() 
            current_tile_img.set_alpha(100)

            #returns the pixel coordiantes of the mouse in respect to the WINDOW
            mouse_pos = pygame.mouse.get_pos()
            mouse_pos = (mouse_pos[0] / RENDER_SCALE, mouse_pos[1] / RENDER_SCALE)
            tile_pos = ((int(mouse_pos[0] + self.scroll[0]) // self.tilemap.tile_size), 
                        (int(mouse_pos[1] + self.scroll[1]) // self.tilemap.tile_size))

            self.display.blit(current_tile_img, (tile_pos[0] * self.tilemap.tile_size - self.scroll[0], tile_pos[1] * self.tilemap.tile_size - self.scroll[1]))
            
            #place tiles
            if(self.clicking):
                self.tilemap.tilemap[str(tile_pos[0]) + ";" + str(tile_pos[1])] = {"type": self.tile_list[self.tile_group], "variant": self.tile_variant, "pos": tile_pos}
            #delete tiles
            if(self.right_clicking):
                tile_loc = str(tile_pos[0]) + ";" + str(tile_pos[1])
                if tile_loc in self.tilemap.tilemap:
                    del self.tilemap.tilemap[tile_loc]


            for event in pygame.event.get():

                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                #keyboard inputs
                #when clicked
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    if(event.button == 1):
                        self.clicking = True
                    if(event.button == 3):
                        self.right_clicking = True

                    if(self.shift):
                        if(event.button == 4):
                            self.tile_variant = (self.tile_variant - 1) % len(self.assets[self.tile_list[self.tile_group]])
                        if(event.button == 5):
                            self.tile_variant = (self.tile_variant + 1) % len(self.assets[self.tile_list[self.tile_group]])
                    else:
                        if(event.button == 4):
                            self.tile_group = (self.tile_group - 1) % len(self.tile_list)
                            self.tile_variant = 0
                        if(event.button == 5):
                            self.tile_group = (self.tile_group + 1) % len(self.tile_list)
                            self.tile_variant = 0
                
                #when click is released
                if(event.type == pygame.MOUSEBUTTONUP):
                    if(event.button == 1):
                        self.clicking = False
                    if(event.button == 3):
                        self.right_clicking = False

                #when a key is pressed
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_LEFT):
                        self.movement[0] = True
                    if(event.key == pygame.K_RIGHT):
                        self.movement[1] = True
                    if(event.key == pygame.K_UP):
                        self.movement[2] = True
                    if(event.key == pygame.K_DOWN):
                        self.movement[3] = True
                    if(event.key == pygame.K_LSHIFT):
                        self.shift = True

                #when released
                if(event.type == pygame.KEYUP):
                    if(event.key == pygame.K_LEFT):
                        self.movement[0] = False
                    if(event.key == pygame.K_RIGHT):
                        self.movement[1] = False
                    if(event.key == pygame.K_UP):
                        self.movement[2] = False
                    if(event.key == pygame.K_DOWN):
                        self.movement[3] = False
                    if(event.key == pygame.K_LSHIFT):
                        self.shift = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(self.FPS) #runs at 60 fps, dynamic sleep function

Editor().run()

