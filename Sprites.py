
import sys, pygame

white = [255,255,255]
black = [0,0,0]

spritesheet = pygame.image.load(r"Images\Spritesheet.png")

def get_image(sheet, frame, width,height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width),0, width, height))
    image = pygame.transform.scale(image ,(width*scale,height*scale))
    image.set_colorkey(white)
    return image


class Bus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = get_image(spritesheet, 0, 30, 30, 4)
        #self.height = 3 * 50
        #self.width = 2.5 * 50 
        self.x = 320
        self.y = 320
        #self.image = pygame.transform.scale(self.image, (self.width, self.height))
        #self.rect = self.image.get_rect(topleft=(self.x-(self.width/2), self.y-(self.height/2)))
        self.rect = self.image.get_rect(center=(self.x, self.y))




class Obstacle(pygame.sprite.Sprite):
    def __init(self, type, location):
        super().__init__()
        self.type = type
        self.x = location[0]
        self.y = location[1]
        if self.type == 'Person':
            self.width = 0.4
            self.height = 1.8
        #    self.image = pygame.image.load(r"Images\Person.jpg").convert()    #may need to change args
        elif self.type == 'Car':
            self.width = 2
            self.height = 1.5
        #    self.image = pygame.image.load(r"Images\Car.jpg").convert()     #may need to change args
        self.image = pygame.image.load(r"Images\%s.jpg" % type).convert()
        self.rect = self.image.get_rect(topleft=(self.x-(self.width/2), self.y-(self.height/2)))
