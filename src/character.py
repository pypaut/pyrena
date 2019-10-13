import constants as c

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
