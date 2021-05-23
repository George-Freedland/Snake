import pygame
from pygame import mixer

import random
import math
import time

from pygame.draw import line

from Player import Player
from Players import Players
from Food import Food
from Score import Score
from GameOver import GameOver
 
def main():
    pygame.init()
    logo = pygame.image.load('images/snake_logo.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode((800, 600))
     
    # Player
    players = Players(Player(20, 80, 'RIGHT'))

    #Food
    food = Food()

    # Score
    score = Score()

    # Game Over
    gameOver = GameOver()

    # Game Loop
    running = True 
    while running:
        screen.fill((0, 100, 100))
        screen.blit(pygame.Surface((800,60)), (0, 0))
        for i in range(1, 40):
            line(screen, (255, 255, 255), (i*20, 60), (i*20, 600), 1)
        for i in range(1, 40):
            line(screen, (255, 255, 255), (0, 60 + (20* i)), (800, 60 + (20* i)), 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not gameOver.getValue():
                root = players.getRoot()
                if event.key == pygame.K_RIGHT and players.getRoot().getDirection() != 'RIGHT' and players.getRoot().getDirection() != 'LEFT':
                    root.setDirection('RIGHT')
                if event.key == pygame.K_LEFT and players.getRoot().getDirection() != 'LEFT' and players.getRoot().getDirection() != 'RIGHT':
                    root.setDirection('LEFT')
                if event.key == pygame.K_UP and players.getRoot().getDirection() != 'UP' and players.getRoot().getDirection() != 'DOWN':
                    root.setDirection('UP')
                if event.key == pygame.K_DOWN and players.getRoot().getDirection() != 'DOWN' and players.getRoot().getDirection() != 'UP':
                    root.setDirection('DOWN')
                
        # Move and Show Surfaces
        food.show(screen)
        score.show(screen)

        if players.getRoot().outOfBounds() or players.getRoot().cannotMove():
            gameOver.setValue(True)
        
        if gameOver.getValue() == True:
            gameOver.show(screen)

        if players.getRoot().canEat(food):
            score.increase()
            tempRoot = players.getRoot()
            players.setRoot(Player(food.getX(), food.getY(), players.getRoot().getDirection()))
            players.getRoot().setPrevious(tempRoot)
            tempRoot.setNext(players.getRoot())
            food.resetCoordinates()
        
        time.sleep(0.05)
        it = players.getRoot()
        it.show(screen)
        while it.getPrevious() != None:
            it = it.getPrevious()
            it.showPrevious(screen)

        pygame.display.update()
     
if __name__=="__main__":
    main()
