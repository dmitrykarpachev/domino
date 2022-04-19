from random import choice
from functools import reduce


class Computer:
    def __init__(self, bricks: list, intellect=0):
        self.bricks = bricks
        self.intel = intellect

    def get_brick(self, snake):
        bricks = list()
        r = [[False, False], [True, False], [True, True], [False, True]]
        bricks.append(list(filter(lambda x: x[0] == snake[-1][1], self.bricks)))
        bricks.append(list(filter(lambda x: x[1] == snake[-1][1], self.bricks)))
        bricks.append(list(filter(lambda x: x[0] == snake[0][0], self.bricks)))
        bricks.append(list(filter(lambda x: x[1] == snake[0][0], self.bricks)))
        return self.intellect_(bricks, r, snake)

    def intellect_(self, bricks, r, snake):
        if bool(reduce(lambda x, y: x + y, bricks)):
            if self.intel == 1:
                future = list()
                for group, rs in zip(bricks, r):
                    if bool(group):
                        future.append([self.brick_connections(brick, rs[0], rs[1]) for brick in group])
                    else:
                        future.append([0])
                I = future.index(max(future))
                J = future[I].index(max(future[I]))
                self.bricks.remove(bricks[I][J])
                return bricks[I][J], r[I][0], r[I][1]
            elif self.intel == 2:
                data = dict()
                for group, rs in zip(bricks, r):
                    for brick in group:
                        if not not brick:
                            new_snake = reduce(lambda a, b: a + b, snake + self.bricks)
                            data[new_snake.count(brick[0]) + new_snake.count(brick[1])] = [brick, rs[0], rs[1]]
                if bool(data.keys()):
                    res = data[max(data.keys())]
                    return res[0], res[1], res[2]

            else:
                for brick, rs in zip(bricks, r):
                    if bool(brick):
                        brick = choice(brick)
                        self.bricks.remove(brick)
                        return brick, rs[0], rs[1]

    def brick_connections(self, brick, rev, pos):
        a, b = list(reversed(brick)) if rev else brick
        if pos:
            l = len(list(filter(lambda x: a in x, self.bricks)))
        else:
            l = len(list(filter(lambda x: b in x, self.bricks)))
        return l

    def __len__(self):
        return len(self.bricks)
