import pygame, sys
import importlib
import constants as c

from pygame.locals import *

class Character:
    x_a = c.g
    y_a = 0

    x_v = 0
    y_v = 0

    x_pos = c.X_GROUND
    y_pos = 10 * c.TILESIZE

    x_v0 = 0
    y_v0 = 0

    x_pos0 = x_pos
    y_pos0 = y_pos

    x_size = 1 * c.TILESIZE
    y_size = 1 * c.TILESIZE

    is_on_block = False

    def collides(self, block):
        return (block.x_pos - self.x_size < self.x_pos < block.x_pos + block.x_size
        and block.y_pos - self.y_size < self.y_pos < block.y_pos + block.y_size)

    def is_above(self, block):
        """
        Strictly above
        """
        return (block.y_pos - self.y_size < self.y_pos < block.y_pos + block.y_size
        and self.x_pos <= block.x_pos)

    def is_under(self, block):
        """
        Strictly under
        """
        return (block.y_pos - self.y_size < self.y_pos < block.y_pos + block.y_size
        and block.x_pos + block.x_size <= self.x_pos)


class Block:
    x_pos = 7 * c.TILESIZE
    y_pos =  2 * c.TILESIZE

    x_size = 1 * c.TILESIZE
    y_size = 4 * c.TILESIZE


char = Character()
block = Block()


#####################
##### GAME LOOP #####
#####################

pygame.init()

DISPLAYSURF = pygame.display.set_mode((c.SURFWIDTH, c.SURFHEIGHT))
pygame.display.set_caption("My first (working?) game")

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
