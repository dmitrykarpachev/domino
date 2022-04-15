from Exceptions import *


class Player:
    def __init__(self, bricks: list):
        self.bricks = bricks

    def get_brick(self, n: int, end: int, rev=False):
        n -= 1
        if n < len(self.bricks):
            if end in self.bricks[n]:
                if (rev and end == self.bricks[n][1]) or (not rev and end == self.bricks[n][0]):
                    elem = self.bricks.pop(n)
                else:
                    elem = tuple(reversed(self.bricks.pop(n)))
                return elem
            else:
                raise ConnectionError(str(self.bricks[n]))
        else:
            raise InvalidIndex(n)

    def __str__(self):
        return '\n'.join([f'-> {i}: {val} - {tuple(reversed(val))}' for i, val in enumerate(self.bricks, start=1)])

    def __len__(self):
        return len(self.bricks)
