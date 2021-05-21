import pygame
from pygame.locals import *
import sys
import time


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block_x = 100
        self.block_y = 100

        self.block = pygame.image.load("head.png").convert()
        self.block = pygame.transform.scale(self.block, (20, 20))
        self.direction = 'right'

    def draw(self):
        self.parent_screen.fill((2, 0, 50))
        self.parent_screen.blit(self.block, (self.block_x, self.block_y))
        self.parent_screen.blit(self.block, (self.block_x, self.block_y))

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

    def walk(self):
        if self.direction == "left":
            self.block_x -= 20
            self.draw()
        if self.direction == "right":
            self.block_x += 20
            self.draw()
        if self.direction == "up":
            self.block_y -= 20
            self.draw()
        if self.direction == "down":
            self.block_y += 20
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
        self.snake = Snake(self.surface)
        self.snake.draw()

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
            self.snake.walk()
            time.sleep(0.2)

    def drawGrid(self):
        blockSize = 20  # Set the size of the grid block
        for x in range(0, self.WINDOW_WIDTH, blockSize):
            for y in range(0, self.WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.surface, self.WHITE, rect, 1)


if __name__ == "__main__":
    game = Game()
    game.run()
