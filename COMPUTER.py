from random import choice


class Computer:
    def __init__(self, bricks: list):
        self.bricks = bricks

    def get_brick(self, snake):
        bricks = list(filter(lambda x: x[0] in snake[-1] or x[1] in snake[-1], self.bricks))
        if bool(bricks):
            b = choice(bricks)
            self.bricks.remove(b)
            return b

    def __len__(self):
        return len(self.bricks)

