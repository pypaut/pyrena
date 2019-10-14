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

    t = {'t': 0} # Dict are mutable, allowing to pass arguments by reference

    while True:
        # EVENT
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        char.update_pos(block, keys, t)

        ### DRAW ###
        for x in range(c.MAPHEIGHT):
            for y in range(c.MAPWIDTH):
                pygame.draw.rect(DISPLAYSURF, c.color[c.tilemap[x][y]], (y * c.TILESIZE, x * c.TILESIZE, c.TILESIZE, c.TILESIZE))

        pygame.draw.rect(DISPLAYSURF, c.RED, (char.y_pos, char.x_pos, c.TILESIZE, c.TILESIZE))

        pygame.display.update()


if __name__ == "__main__":
    main()
