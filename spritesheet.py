import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, x, y, width, height, scale, colour):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet, (0,0), (x,y, width, height))
        image = pygame.transform.scale(image ,(width*3,height*3))
        image.set_colorkey(colour)
        return image