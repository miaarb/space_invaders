class Shuttle:
    def __init__(self, x, y, v, width, height):
        self.x = x
        self.y = y
        self.velocity = v
        self.width = width
        self.height = height
        self.is_moving_left = False
        self.is_moving_right = False
        self.sprite = None
        self.lives = 3

    def move(self):
        if self.is_moving_right:
            self.x += self.velocity
        if self.is_moving_left:
            self.x -= self.velocity


