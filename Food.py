import pygame
import random

class Food:
    def __init__(self):
        xMult = random.randint(1, 38)
        self.x = 20 * xMult
        yMult = random.randint(4, 28)
        self.y = 20 * yMult
        # self.img = pygame.Surface((20, 20))
        self.img = pygame.image.load('images/food.png')
    
    def show(self, screen):
        screen.blit(self.img, (self.x + 3, self.y + 2))

    def resetCoordinates(self):
        xMult = random.randint(1, 38)
        self.x = 20 * xMult
        yMult = random.randint(4, 28)
        self.y = 20 * yMult

    def getX(self):
        return self.x

    def getY(self):
        return self.y