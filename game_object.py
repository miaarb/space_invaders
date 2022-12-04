class GameObject:
    def __init__(self, x, y, v, width, height):
        self.x = x
        self.y = y
        self.velocity = v
        self.width = width
        self.height = height
        self.is_alive = True

    def die(self):
        self.is_alive = False

    def is_intersected_with(self, another_game_object):
        # print("is intersected with")
        return GameObject.are_intersected(self, another_game_object)

    @staticmethod
    def are_intersected(game_object_1, game_object_2):
        g1 = game_object_1
        g2 = game_object_2
        is_one_vertical_side_between_anothers = (
                g1.x <= g2.x <= g1.x + g1.width
                or g1.x <= g2.x + g2.width <= g1.x + g1.width
                or g2.x <= g1.x <= g2.x + g2.width
                or g2.x <= g1.x + g1.width <= g2.x + g2.width
        )
        is_one_horizontal_side_between_anothers = (
                g1.y <= g2.y <= g1.y + g1.height
                or g1.y <= g2.y + g2.height <= g1.y + g1.height
                or g2.y <= g1.y <= g2.y + g2.height
                or g2.y <= g1.y + g1.height <= g2.y + g2.height
        )
        # print("check intersection")
        return is_one_vertical_side_between_anothers and is_one_horizontal_side_between_anothers
