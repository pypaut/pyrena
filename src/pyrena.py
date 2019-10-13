import pygame, sys
import importlib
import constants as c

from character import Character
from block import Block
from pygame.locals import *


def main():
    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((c.SURFWIDTH, c.SURFHEIGHT))
    pygame.display.set_caption("My first (working?) game")

    char = Character()
    block = Block()

    t = 0

    while True:
        # EVENT
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # LOSING ENERGY
        char.y_a *= 0.9

        # UPDATE ACCELERATION
        keys = pygame.key.get_pressed()

        if keys[K_SPACE] and char.x_pos == c.X_GROUND:
            t = 1
            char.x_v0 = -20

        if keys[K_a]:
            char.y_a = - 2

        if keys[K_d]:
            char.y_a = 2

        # UPDATE POS
        x_old_pos = char.x_pos
        y_old_pos = char.y_pos

        if char.x_pos <= c.X_GROUND:
            char.x_pos = 0.5 * char.x_a * t ** 2 + char.x_v0 * t + char.x_pos0
            t += 0.20
        if char.x_pos > c.X_GROUND:
            char.x_pos = c.X_GROUND

        if char.y_a < 0 and char.y_pos > 0:
            char.y_pos += char.y_a * 1

        if char.y_a > 0 and char.y_pos < c.SURFWIDTH - c.TILESIZE:
            char.y_pos += char.y_a * 1

        if char.collides(block):
            if char.is_above(block): # Can't go down
                char.x_pos = block.x_pos - char.x_size
                char.is_on_block = True
            elif char.is_under(block): # Can't go up
                char.x_pos = x_old_pos
            else:
                char.y_pos = y_old_pos

        ### DRAW ###
        for x in range(c.MAPHEIGHT):
            for y in range(c.MAPWIDTH):
                pygame.draw.rect(DISPLAYSURF, c.color[c.tilemap[x][y]], (y * c.TILESIZE, x * c.TILESIZE, c.TILESIZE, c.TILESIZE))

        pygame.draw.rect(DISPLAYSURF, c.RED, (char.y_pos, char.x_pos, c.TILESIZE, c.TILESIZE))

        pygame.display.update()


if __name__ == "__main__":
    main()
