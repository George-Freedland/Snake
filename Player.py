import pygame
import time

class Player:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        if direction == 'RIGHT':
            self.moveRight()
        if direction == 'LEFT':
            self.moveLeft()
        if direction == 'UP':
            self.moveUp()
        if direction == 'DOWN':
            self.moveDown()
        self.img = pygame.Surface((20,20))
        self.previous = None
        self.next = None
        self.prevX = None
        self.prevY = None
    
    def show(self, screen):
        self.prevX = self.x
        self.prevY = self.y
        self.x += self.speedX
        self.y += self.speedY 
        screen.blit(self.img, (self.x, self.y))

    def showPrevious(self, screen):
        self.prevX = self.x
        self.prevY = self.y
        self.x = self.next.getPrevX()
        self.y = self.next.getPrevY()
        screen.blit(self.img, (self.x, self.y))


    def canEat(self, food):
        if (self.x + self.speedX == food.getX() and self.y + self.speedY == food.getY()):
            return True
        return False

    def outOfBounds(self):
        if self.x < 0 or self.x > 780 or self.y > 580 or self.y < 60:
            return True
        return False

    def cannotMove(self):
        nextPosition = (self.x + self.speedX, self.y + self.speedY)
        allPositions = []
        allPositions.append((self.x, self.y))
        node = self.previous
        while(node != None):
            allPositions.append((node.getX(), node.getY()))
            node = node.getPrevious()
        if (nextPosition in allPositions):
            return True
        return False

    def moveRight(self):
        self.speedX = 20
        self.speedY = 0
    def moveLeft(self):
        self.speedX = -20
        self.speedY = 0
    def moveUp(self):
        self.speedX = 0
        self.speedY = -20
    def moveDown(self):
        self.speedX = 0
        self.speedY = 20

    def getX(self):
        return self.x
    def setX(self, x):
        self.x = x
    def getY(self):
        return self.y
    def setY(self, y):
        self.y = y
    def getSpeedX(self):
        return self.speedX
    def getSpeedY(self):
        return self.speedY
    def getDirection(self):
        return self.direction
    def setDirection(self, direction):
        self.direction = direction
        if direction == 'RIGHT':
            self.moveRight()
        if direction == 'LEFT':
            self.moveLeft()
        if direction == 'UP':
            self.moveUp()
        if direction == 'DOWN':
            self.moveDown()
    def getPrevious(self):
        return self.previous
    def setPrevious(self, previous):
        self.previous = previous
    def getNext(self):
        return self.next
    def setNext(self, next):
        self.next = next
    def getPrevX(self):
        return self.prevX
    def getPrevY(self):
        return self.prevY
