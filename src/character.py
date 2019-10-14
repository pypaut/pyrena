import constants as c
import pygame

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

    def update_pos(self, block, keys, t):
        # Acceleration
        self.y_a *= 0.9 # Energy loss

        if keys[pygame.K_SPACE] and self.x_pos == c.X_GROUND:
            t['t'] = 1
            self.x_v0 = -20

        if keys[pygame.K_a]:
            self.y_a = -2

        if keys[pygame.K_d]:
            self.y_a = 2

        # Position
        x_old_pos = self.x_pos
        y_old_pos = self.y_pos

        if self.x_pos <= c.X_GROUND:
            self.x_pos = 0.5 * self.x_a * t['t'] ** 2 + self.x_v0 * t['t'] + self.x_pos0
            t['t'] += 0.20
        if self.x_pos > c.X_GROUND:
            self.x_pos = c.X_GROUND

        if self.y_a < 0 and self.y_pos > 0:
            self.y_pos += self.y_a * 1

        if self.y_a > 0 and self.y_pos < c.SURFWIDTH - c.TILESIZE:
            self.y_pos += self.y_a * 1

        if self.collides(block):
            if self.is_above(block): # Can't go down
                self.x_pos = block.x_pos - self.x_size
                self.is_on_block = True
            elif self.is_under(block): # Can't go up
                self.x_pos = x_old_pos
            else:
                self.y_pos = y_old_pos
