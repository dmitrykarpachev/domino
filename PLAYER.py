from Exceptions import *


class Player:
    def __init__(self, bricks: list):
        self.bricks = bricks

    def get_brick(self, n: int):
        n -= 1
        if n < len(self.bricks):
            elem = self.bricks.pop(n)
            return elem
        else:
            raise InvalidIndex(n)

    def __str__(self):
        return '\n'.join([f'-> {i}: {val}' for i, val in enumerate(self.bricks, start=1)])

    def __len__(self):
        return len(self.bricks)
