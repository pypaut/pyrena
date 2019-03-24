import pygame, sys
import importlib

from pygame.locals import *

###############
##### MAP #####
###############

GREY = (50, 50, 50)
BROWN = (153, 76, 0)
BLUE = (0, 200, 255)
RED = (200, 0, 0)


GROUND = 0
BLOCK = 1
SKY = 2
CHAR = 3

color = {
    GROUND : GREY,
    BLOCK : GREY,
    SKY : BLUE,
    CHAR : RED
}

tilemap = [
    [SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY],
    [SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY],
    [SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY],
    [SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY],
    [SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY],
    [SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY],
    [SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY],
    [SKY,    SKY,    GROUND, GROUND, GROUND, GROUND, SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY],
    [SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY],
    [SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY,    SKY],
    [GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND],
    [GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND, GROUND],
]

TILESIZE = 50
MAPWIDTH = 20
MAPHEIGHT = 12

X_GROUND = (MAPWIDTH * TILESIZE) // 2 - TILESIZE
X_BLOCK = 6 * TILESIZE
Y_BEGIN_BLOCK = 2 * TILESIZE
Y_END_BLOCK = 6 * TILESIZE

SURFWIDTH = MAPWIDTH * TILESIZE
SURFHEIGHT = MAPHEIGHT * TILESIZE


g = 1

class Character:
    x_a = g
    y_a = 0

    x_v = 0
    y_v = 0

    x_pos = X_GROUND
    y_pos = 10 * TILESIZE

    x_v0 = 0
    y_v0 = 0

    x_pos0 = x_pos
    y_pos0 = y_pos

    x_size = 1 * TILESIZE
    y_size = 1 * TILESIZE

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
    x_pos = 7 * TILESIZE
    y_pos =  2 * TILESIZE

    x_size = 1 * TILESIZE
    y_size = 4 * TILESIZE


char = Character()
block = Block()


#####################
##### GAME LOOP #####
#####################

pygame.init()


DISPLAYSURF = pygame.display.set_mode((SURFWIDTH, SURFHEIGHT))
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

    if keys[K_SPACE] and char.x_pos == X_GROUND:
        t = 1
        char.x_v0 = -20

    if keys[K_a]:
        char.y_a = - 2

    if keys[K_d]:
        char.y_a = 2

    # UPDATE POS
    x_old_pos = char.x_pos
    y_old_pos = char.y_pos

    if char.x_pos <= X_GROUND:
        char.x_pos = 0.5 * char.x_a * t ** 2 + char.x_v0 * t + char.x_pos0
        t += 0.20
    if char.x_pos > X_GROUND:
        char.x_pos = X_GROUND

    if char.y_a < 0 and char.y_pos > 0:
        char.y_pos += char.y_a * 1

    if char.y_a > 0 and char.y_pos < SURFWIDTH - TILESIZE:
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
    for x in range(MAPHEIGHT):
        for y in range(MAPWIDTH):
            pygame.draw.rect(DISPLAYSURF, color[tilemap[x][y]], (y * TILESIZE, x * TILESIZE, TILESIZE, TILESIZE))

    pygame.draw.rect(DISPLAYSURF, RED, (char.y_pos, char.x_pos, TILESIZE, TILESIZE))

    pygame.display.update()
