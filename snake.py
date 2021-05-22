import random

import pygame
from pygame.locals import *
import sys
import time

SIZE = 40


class Snake:
    LENGTH = 5

    def __init__(self, parent_screen, length):
        self.food = pygame.image.load("food.png").convert()
        self.food = pygame.transform.scale(self.food, (20, 20))
        self.length = 5
        self.score = 0
        self.parent_screen = parent_screen
        self.block_x = [SIZE] * length
        self.block_y = [SIZE] * length

        self.block = pygame.image.load("head.png").convert()
        self.block = pygame.transform.scale(self.block, (20, 20))
        self.direction = 'right'
        self.y_food = random.randint(0, 920)
        self.x_food = random.randint(0, 920)

    def draw(self):
        self.parent_screen.fill((2, 0, 50))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.block_x[i], self.block_y[i]))
            self.parent_screen.blit(self.food, (self.x_food, self.y_food))

    def move_left(self):
        self.draw()
        if self.direction != "right":
            self.direction = 'left'

    def move_right(self):
        self.draw()
        if self.direction != "left":
            self.direction = 'right'

    def move_up(self):
        self.draw()
        if self.direction != "down":
            self.direction = 'up'

    def move_down(self):
        self.draw()
        if self.direction != "up":
            self.direction = 'down'

    def inc_length(self):
        self.length += 1
        self.block_x.append(-1)
        self.block_y.append(-1)

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]
            print(self.x_food, self.y_food)
            if self.block_x[0] + 20 > self.x_food > self.block_x[0] - 20 and self.block_y[
                0] + 20 > self.y_food > self.block_y[0] - 20:
                self.score += 1
                self.inc_length()

                self.x_food = random.randint(0, 920)
                self.y_food = random.randint(0, 920)



                self.draw()
                print(self.score)
                print(self.length)

        if self.direction == "left":
            self.block_x[0] -= 20
            self.draw()
        if self.direction == "right":
            self.block_x[0] += 20
            self.draw()
        if self.direction == "up":
            self.block_y[0] -= 20
            self.draw()
        if self.direction == "down":
            self.block_y[0] += 20
            self.draw()


class Game:
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.WHITE = (50, 50, 50)
        self.WINDOW_HEIGHT = 920
        self.WINDOW_WIDTH = 920

        pygame.init()
        self.surface = pygame.display.set_mode((self.WINDOW_HEIGHT, self.WINDOW_WIDTH))
        self.surface.fill((2, 0, 50))
        self.snake = Snake(self.surface, 5)

    def run(self):
        running = True

        while running:
            game.drawGrid()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_w:
                        self.snake.move_up()
                    if event.key == K_a:
                        self.snake.move_left()
                    if event.key == K_s:
                        self.snake.move_down()
                    if event.key == K_d:
                        self.snake.move_right()

                    elif event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit(0)
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.time.wait(10)
            self.snake.draw()
            self.snake.walk()
            time.sleep(0.15)

    def drawGrid(self):
        blockSize = 20  # Set the size of the grid block
        for x in range(0, self.WINDOW_WIDTH, blockSize):
            for y in range(0, self.WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.surface, self.WHITE, rect, 1)


if __name__ == "__main__":
    game = Game()
    game.run()
