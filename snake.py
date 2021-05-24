import random
import pygame
from pygame.locals import *
import sys
import time

# A basic snake game created for an AI as a learning environment.
# Still contains some bugs but feel free to use the code if you'd like.


SIZE = 40


class Snake:

    def __init__(self, parent_screen, length):

        # Variable definitions and image loading and transforming
        self.food = pygame.image.load("food.png").convert()
        self.block = pygame.image.load("head.png").convert()
        self.food = pygame.transform.scale(self.food, (20, 20))
        self.block = pygame.transform.scale(self.block, (20, 20))

        self.length = 5
        self.score = 0
        self.direction = 'right'
        self.parent_screen = parent_screen

        self.block_x = [SIZE] * length
        self.block_y = [SIZE] * length
        self.x_food = random.randint(1, 45) * 20
        self.y_food = random.randint(1, 45) * 20

    def draw(self):
        # Draws snake length and food
        self.parent_screen.fill((2, 0, 50))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.block_x[i], self.block_y[i]))
            self.parent_screen.blit(self.food, (self.x_food, self.y_food))

    def move_left(self):
        # Prevents player from moving the opposite directions
        if self.direction != "right":
            self.direction = 'left'

    def move_right(self):
        if self.direction != "left":
            self.direction = 'right'

    def move_up(self):
        if self.direction != "down":
            self.direction = 'up'

    def move_down(self):
        if self.direction != "up":
            self.direction = 'down'

    def inc_length(self):
        self.block_x.append(-1)
        self.block_y.append(-1)
        self.length += 1

    def walk(self):
        # Getting the snake body to follow the head
        for i in range(self.length - 1, 0, -1):
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]
        # Moving distance definitions
        if self.direction == "left":
            self.block_x[0] -= 20
        if self.direction == "right":
            self.block_x[0] += 20
        if self.direction == "up":
            self.block_y[0] -= 20
        if self.direction == "down":
            self.block_y[0] += 20

    def foodspawn(self):
        # Spawns food and increments snake length per piece eaten
        if self.block_x[0] + 20 > self.x_food > self.block_x[0] - 20 and self.block_y[0] + 20 > self.y_food > \
                self.block_y[0] - 20:
            self.score += 1
            self.inc_length()
            # Respawns food randomly
            self.x_food = random.randint(1, 46) * 20
            self.y_food = random.randint(1, 46) * 20

            print(self.score)

    def gameover(self):
        # Check collision with walls
        if self.block_x[0] > 920 or self.block_y[0] > 920 or self.block_x[0] < 0 or self.block_y[0] < 0:
            self.block_x[0] = 500
            self.block_y[0] = 500
            self.score = self.score - 1
            self.block_x.append(1)
            self.block_y.append(1)
            self.length = 5
            print(self.score)
        # Check collision with self
        for i in range(len(self.block_x)):
            if self.block_x[0] == self.block_x[i] and self.block_y[0] == self.block_y[i] and i > 0:
                self.block_x[0] = 500
                self.block_y[0] = 500
                self.score = self.score - 1
                print(self.score)
                self.block_x.append(1)
                self.block_y.append(1)
                self.length = 5


class Game:
    def __init__(self):
        self.WHITE = (50, 50, 50)
        self.WINDOW_HEIGHT = 920
        self.WINDOW_WIDTH = 920

        # Game initialization & Font initialization (For scores)
        pygame.font.init()
        pygame.init()
        self.default_font = pygame.font.get_default_font()
        self.font_renderer = pygame.font.Font(self.default_font, 20)
        self.surface = pygame.display.set_mode((self.WINDOW_HEIGHT, self.WINDOW_WIDTH))

        # Default snake spawn parameters
        self.surface.fill((2, 0, 50))
        self.snake = Snake(self.surface, 5)

    def numbers(self):
        # Renders score
        label = self.font_renderer.render(str(self.snake.score), True, (255, 255, 255))
        self.snake.parent_screen.blit(label, (5, 1))

    # Main game loop
    def run(self):
        while True:
            # Draws the game and checks keyboard inputs
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
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.time.wait(10)
            self.snake.walk()
            self.snake.foodspawn()
            self.snake.draw()
            self.snake.gameover()
            self.numbers()
            time.sleep(0.15)  # Essentially game tick

    def drawGrid(self):
        # Draws the grid on the display

        blockSize = 20  # Set the size of the grid block
        for x in range(0, self.WINDOW_WIDTH, blockSize):
            for y in range(0, self.WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.surface, self.WHITE, rect, 1)


# Game start
if __name__ == "__main__":
    game = Game()
    game.run()
