# Colors
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

# Map
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

# Block sizes
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
