
import sys
import numpy   #unneeded rn
import pygame
from pygame.locals import *

from Sprites import Obstacle, Bus



        


class GUI:
    def __init__(self):
        pygame.init()
        self.fps = 24    
        self.fpsClock = pygame.time.Clock()
        WIDTH, HEIGHT = 640, 640
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Bus surroundings GUI")
        self.screen.fill((255,255,255))
        self.all_sprites = pygame.sprite.Group()
        self.bus = Bus()
        self.all_sprites.add(self.bus)
        self.person = Obstacle("Person", (200,200))
        self.all_sprites.add(self.person)
        self.all_sprites.draw(self.screen)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            #update display
            pygame.display.update()
            self.all_sprites.update()

            self.fpsClock.tick(self.fps)









if __name__ == '__main__':
    gui = GUI()
    gui.run()