from random import choice


class Computer:
    def __init__(self, bricks: list):
        self.bricks = bricks

    def get_brick(self, snake):
        bricks = list(filter(lambda x: x[0] == snake[-1][1], self.bricks))
        r = [False, False]
        if not bool(bricks):
            bricks = list(filter(lambda x: x[1] == snake[-1][1], self.bricks))
            r = [True, False]
        if not bool(bricks):
            bricks = list(filter(lambda x: x[0] == snake[0][0], self.bricks))
            r = [True, True]
        if not bool(bricks):
            bricks = list(filter(lambda x: x[1] == snake[0][0], self.bricks))
            r = [False, True]
        if bool(bricks):
            b = choice(bricks)
            self.bricks.remove(b)
            return [b, r[0], r[1]]

    def __len__(self):
        return len(self.bricks)

