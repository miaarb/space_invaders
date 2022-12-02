class Bullet:
    def __init__(self, x, y, v, width, height):
        self.x = x
        self.y = y
        self.velocity = v
        self.is_broken = False
        self.width = width
        self.height = height

    def move(self):
        print("moves")
        if self.is_broken:
            return
        self.y -= self.velocity
