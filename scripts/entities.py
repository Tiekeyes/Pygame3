import pygame 

class PhysicsEntity:

    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]

        self.action = '' 
        self.anim_offset = (-3, -3)
        self.flip = False 
        self.set_action('idle')


    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action].copy()


    def update(self, tilemap, movement=(0, 0)):

        #collision status
        self.collisions = {'up': False, 'down': False, 'right': False,'left': False}

        #calculate transformation
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        
        #apply transformation
        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()

        #in x-dir
        #for each hitbox around the entity
        for rect in tilemap.physics_rects_around(self.pos):
            #if it collides
            if entity_rect.colliderect(rect):
                #moving right
                if frame_movement[0] > 0:
                    #snap the right of the entity to the left of the tile
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                #moving left
                if frame_movement[0] < 0:
                    #snap the left of the entity to the right of the tile
                    entity_rect.left = rect.right 
                    self.collisions['left'] = True 
                self.pos[0] = entity_rect.x

        #in y-dir
        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                #moving down
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True 
                #moving up
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True 
                self.pos[1] = entity_rect.y

        #update the velocity based on acceleration, but keep the terminal velocity as 5
        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        #if the entity collides vertically, reset the vertical velocity
        if(self.collisions['down'] or self.collisions['up']):
            self.velocity[1] = 0

        if(movement[0] >  0):
            self.flip = False
        if(movement[0] < 0):
            self.flip = True

        #update animation
        self.animation.update()
        

    def render(self, surf, offset=(0, 0)):
        surf.blit(pygame.transform.flip(self.animation.img(), self.flip, False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))


    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    

class Player(PhysicsEntity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'player', pos, size)
        self.air_time = 0


    def update(self, tilemap, movement=(0, 0)):
        super().update(tilemap, movement=movement)

        self.air_time += 1

        #player is on the ground
        if(self.collisions['down']):
            self.air_time = 0
        
        #player is in the air for a while
        if(self.air_time >= 5):
            self.set_action('jump')
        #player is moving
        elif(movement[0] != 0):
            self.set_action('run')
        #player is not moving
        else:
            self.set_action('idle')