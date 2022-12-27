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
            if current_time - self.shoot_time > 500:
                self.can_shoot = True
    
    def input_position(self): 
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def shoot(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            print ('shoot')
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def update(self):
        self.laser_timer()
        self.shoot()
        self.input_position()
        



class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        # parent class
        super().__init__(groups)
        # image 
        self.image = pygame.image.load('/Users/griggs/Desktop/Dev/Games/AsteroidShooters/graphics/laser.png').convert_alpha()
        # rect
        self.rect = self.image.get_rect(midbottom = pos)

    def update(self):
        self.rect.y -= 10
        

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

# sprite creation
ship = Ship(spaceship_group)
laser = Laser((100,300),laser_group)

# game loop:
while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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
