import pygame 

class PhysicsEntity:

    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]

    def update(self, movement=(0, 0)):
        pass
    
        