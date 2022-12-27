import pygame, sys

class Ship(pygame.sprite.Sprite):
    def __init__(self,groups): 
        # 1. init parent class
        super().__init__(groups)

        # 2. We need a surface -> image
        self.image = pygame.image.load('/Users/griggs/Desktop/Dev/Games/AsteroidShooters/graphics/ship.png').convert_alpha() 

        #3. We need a rect
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # timer
        self.can_shoot = True
        self.shoot_time = None
    
    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 400:
                self.can_shoot = True
    
    def input_position(self): 
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def shoot(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

            # create new laser object in specified location
            Laser(self.rect.midtop,laser_group)

    def update(self):
        self.laser_timer()
        self.shoot()
        self.input_position()
        

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('/Users/griggs/Desktop/Dev/Games/AsteroidShooters/graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
       
        # float-based position
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 600

    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x),round(self.pos.y))
        
class Meteor(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('/Users/griggs/Desktop/Dev/Games/AsteroidShooters/graphics/meteor.png')

        # random float-based position 
        self.pos = pygame.math.Vector2([math.rand,])

# basic setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid Shooters')
clock = pygame.time.Clock()

# background
background_surface = pygame.image.load('/Users/griggs/Desktop/Dev/Games/AsteroidShooters/graphics/background.png')

# sprite groups
spaceship_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()

# sprite creation
ship = Ship(spaceship_group)

# timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer,400)
# game loop:
while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == meteor_timer
            Meteor(pos, group)

    # delta time
    dt = clock.tick() / 1000

    # background
    display_surface.blit(background_surface,(0,0))

    # update
    spaceship_group.update()
    laser_group.update()

    # graphics
    spaceship_group.draw(display_surface)
    laser_group.draw(display_surface)

    # draw the frame
    pygame.display.update()
