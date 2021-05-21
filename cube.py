import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pyglet
from definitions import *



def Cube():
    glBegin(GL_QUADS)

    for face in faces:
        x = 0
        for vertex in face:
            x += 1
            glColor3fv((1, 1, 1))
            glVertex3fv(vertexes[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((255, 0, 0))
            glVertex3fv(vertexes[vertex])

    glEnd()


def Line():
    glBegin(GL_LINES)
    for edge2 in lineedge:
        for vertex2 in line:
            glColor3fv((255, 255, 255))
            glVertex3fv(vertex2)

    glEnd()


def head():
    glBegin(GL_QUADS)
    for face in snakefaces:
        for vertex in face:
            glColor3fv((0, 255, 0))
            glVertex3fv(snake[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in snakeedges:
        for vertex in edge:
            glColor3fv((0, 0, 0))
            glVertex3fv(snake[vertex])

    glEnd()


def main():
    pygame.init()
    display = (920, 920)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glRotatef(0, 0, 0, 0)
    while True:
        mouseMove = pygame.mouse.get_rel()
        glRotatef(mouseMove[0] * 0.3, 0.0, 1.0, 0.0)
        # glRotatef(mouseMove[1] * 0.3, 1, 0.0, 0.0) # This is yaxis mouse input rotation / Disabled for now
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        Line()
        head()
        Cube()

        pygame.display.flip()
        pygame.time.wait(10)


main()
