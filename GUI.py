
import sys
import numpy
import pygame
from pygame.locals import *


class Obstacle(pygame.sprite.Sprite):
    def __init(self, type, location):
        super().__init__()
        self.type = type
        self.location = location
        if self.type == 'Person':
            self.width = 0.4
            self.height = 1.8
        #    self.image = pygame.image.load(r"Images\Person.jpg").convert()    #may need to change args
        elif self.type == 'Car':
            self.width = 2
            self.height = 1.5
        #    self.image = pygame.image.load(r"Images\Car.jpg").convert()     #may need to change args
        self.image = pygame.image.load(r"Images\%s.jpg" % type).convert()


class Bus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"Images\bus.jpg").convert()
        self.height = 3 * 50
        self.width = 2.5 * 50 
        self.x = 350
        self.y = 400
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x-(self.width/2), self.y-(self.height/2)))

        


class GUI():
    def __init__(self):
        pygame.init()
        self.fps = 60    
        self.fpsClock = pygame.time.Clock()
        WIDTH, HEIGHT = 700, 800
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Bus surroundings GUI")
        self.screen.fill((255,255,255))
        self.all_sprites = pygame.sprite.Group()
        self.bus = Bus()
        self.all_sprites.add(self.bus)
        self.all_sprites.draw(self.screen)

        


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.quit()
            

            pygame.display.update()
            self.all_sprites.update()

        self.fpsClock.tick(self.fps)








if __name__ == '__main__':
    gui = GUI()
    gui.run()