import pygame
from pygame.locals import *
import sys
def draw_block():
    surface.fill((2, 0, 50))
    surface.blit(block,(block_x,block_y))
    #pygame.display.flip()


def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(surface, WHITE, rect, 1)

if __name__ == "__main__":
    BLACK = (0, 0, 0)
    WHITE = (50, 50, 50)
    WINDOW_HEIGHT = 920
    WINDOW_WIDTH = 920
    block_x = 100
    block_y = 100


    pygame.init()
    surface = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    surface.fill((2, 0, 50))

    block = pygame.image.load("head.png").convert()
    block = pygame.transform.scale(block, (20, 20))

    surface.blit(block,(block_x,block_y))

    display = (WINDOW_HEIGHT, WINDOW_WIDTH)
    pygame.display.flip()
    running = True

    while running:
        drawGrid()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_w:
                    block_y -= 20
                    draw_block()

                if event.key == K_a:
                    block_x -= 20
                    draw_block()
                if event.key == K_s:
                    block_y += 20
                    draw_block()
                if event.key == K_d:
                    block_x += 20
                    draw_block()

                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            elif event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        pygame.time.wait(10)
