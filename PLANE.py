from Exceptions import *
from random import choice
from functools import reduce


class Plane:
    def __init__(self, player_obj, computer_obj, stock: list, state: str, start_brick: tuple):
        self.stock = stock
        self.state = state
        self.snake = [start_brick]
        self.player = player_obj
        self.computer = computer_obj

    def step(self, input_: str):
        if self.state == 'computer' and input_ == '':
            cIn = self.computer.get_brick(self.snake)
            if cIn is not None:
                self.snake.append(cIn)
            else:
                bone = choice(self.stock)
                self.computer.bricks.append(bone)
                self.stock.remove(bone)
        elif self.state == 'player' and input_ != '':
            if input_.isdigit() and input_ != '-':
                self.snake.append(self.player.get_brick(int(input_)))
            elif input_ == '-':
                bone = choice(self.stock)
                self.player.bricks.append(bone)
                self.stock.remove(bone)
            else:
                raise InvalidIndex(input_)
        else:
            raise InvalidInput(input_)
        if self.state == 'player':
            self.state = 'computer'
        else:
            self.state = 'player'

    def finish(self):
        if not bool(self.player.bricks):
            return '⁙          🎂🎂🎂 The game is over. You won! 🎂🎂🎂          ⁙'
        if not bool(self.computer.bricks):
            return '⁙            The game is over. The computer won!           ⁙'
        if self.snake[0][0] == self.snake[-1][1] and reduce(lambda x, y: x + y, self.snake).count(self.snake[0][0]) == 8:
            return '⁙               The game is over. It`s draw!               ⁙'
        return

    def __str__(self):
        if self.state == 'computer':
            status = 'Computer is about to make a move. Press Enter to continue...'
        else:
            status = 'It`s your turn to make a move. Enter your command.'
        if len(self.snake) > 6:
            return f'{" ".join(map(str, self.snake[:3]))} ... {" ".join(map(str, self.snake[-3:]))}\nStatus: {status}'
        return f'{" ".join(map(str, self.snake))}\nStatus: {status}'

    def __len__(self):
        return len(self.stock)
