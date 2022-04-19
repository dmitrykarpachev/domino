import pygame as pg
import requests
from functools import reduce

# ============================================
pg.init()
screen = pg.display.set_mode((550, 550))
pg.display.set_caption("Sudoku")
numeric_font = pg.font.SysFont('Comic Sans MS', 35)
menu_font = pg.font.SysFont('Comic Sans MS', 27)
background_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)
grid_color = [[0 for _ in range(9)] for _ in range(9)]
true_color = (60, 179, 113)
line_color = (0, 255, 127)
grid = [[0 for _ in range(9)] for _ in range(9)]
grid_original = [[0 for _ in range(9)] for _ in range(9)]
# ============================================


def get_complexity(lavel):
    global grid, grid_original
    response = requests.get(f"https://sugoku.herokuapp.com/board?difficulty={lavel}")
    grid_original = response.json()['board']
    grid = [[grid_original[x][y] for y in range(len(grid_original[0]))] for x in range(len(grid_original))]


def right_move(grid):
    global grid_color
    lastI = 0
    logic = list()
    for i in range(3, 10, 3):
        lastJ = 0
        for j in range(3, 10, 3):
            mas = reduce(lambda a, b: a + b, list(map(lambda line: line[lastJ:j], grid[lastI:i])))
            if sum(mas) == 45 and len(set(mas)) == len(mas):
                logic.append(True)
                for y in range(lastI, i):
                    for x in range(lastJ, j):
                        grid_color[y][x] = 1
            else:
                logic.append(False)
                for y in range(lastI, i):
                    for x in range(lastJ, j):
                        grid_color[y][x] = 0
            lastJ = j
        lastI = i
        for i in range(9):
            if sum(grid[i]) == 45 and len(set(grid[i])) == len(grid[i]):
                logic.append(True)
                grid_color[i] = [2] * 9
            else:
                logic.append(False)
        for j in range(9):
            new_line = [line[j] for line in grid]
            if sum(new_line) == 45 and len(set(new_line)) == len(new_line):
                logic.append(True)
                for i in range(9):
                    grid_color[i][j] = 2
            else:
                logic.append(False)
        if all(logic):
            return 'finish'


class Menu:
    def __init__(self):
        self.easy_button = (75, 225, 100, 50)
        self.normal_button = (225, 225, 100, 50)
        self.hard_button = (375, 225, 100, 50)
        self.button_width = 100
        self.button_height = 50
        self.easy = (70, 130, 180)
        self.normal = (46, 139, 87)
        self.hard = (139, 0, 0)
        grid_color = [[0 for _ in range(9)] for _ in range(9)]

    def main(self, event):
        screen.fill(background_color)
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            pos = pg.mouse.get_pos()
            if self.easy_button[0] <= pos[0] <= self.easy_button[0] + 100 and self.easy_button[1] <= pos[1] <= self.easy_button[1] + 50:
                get_complexity('easy')
                return 'main'
            if self.normal_button[0] <= pos[0] <= self.normal_button[0] + 100 and self.normal_button[1] <= pos[1] <= self.normal_button[1] + 50:
                get_complexity('medium')
                return 'main'
            if self.hard_button[0] <= pos[0] <= self.hard_button[0] + 100 and self.hard_button[1] <= pos[1] <= self.hard_button[1] + 50:
                get_complexity('hard')
                return 'main'
        else:
            pos = pg.mouse.get_pos()
            if self.easy_button[0] <= pos[0] <= self.easy_button[0] + 100 and self.easy_button[1] <= pos[1] <= self.easy_button[1] + 50:
                self.easy = 95, 158, 160
            else:
                self.easy = (70, 130, 180)
            if self.normal_button[0] <= pos[0] <= self.normal_button[0] + 100 and self.normal_button[1] <= pos[1] <= self.normal_button[1] + 50:
                self.normal = (60, 179, 113)
            else:
                self.normal = (46, 139, 87)
            if self.hard_button[0] <= pos[0] <= self.hard_button[0] + 100 and self.hard_button[1] <= pos[1] <= self.hard_button[1] + 50:
                self.hard = (220, 20, 60)
            else:
                self.hard = (139, 0, 0)
        return 'menu'

    def draw(self, grid, grid_original):
        pg.draw.rect(screen, self.easy, self.easy_button, 5)
        value = menu_font.render('Easy', True, self.easy)
        screen.blit(value, (self.easy_button[0] + 20,
                            self.easy_button[1] + 5,
                            self.button_width,
                            self.button_height))
        # ----------------------------------------------
        pg.draw.rect(screen, self.normal, self.normal_button, 5)
        value = menu_font.render('Normal', True, self.normal)
        screen.blit(value, (self.normal_button[0] + 5,
                            self.normal_button[1] + 5,
                            self.button_width,
                            self.button_height))
        # ----------------------------------------------
        pg.draw.rect(screen, self.hard, self.hard_button, 5)
        value = menu_font.render('Hard', True, self.hard)
        screen.blit(value, (self.hard_button[0] + 15,
                            self.hard_button[1] + 5,
                            self.button_width,
                            self.button_height))


class Main:
    def main(self, event):
        screen.fill(background_color)
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                return 'menu'
        return 'main'

    def draw(self, grid, grid_original):
        for i in range(9):
            for j in range(9):
                if grid_color[i][j] == 1:
                    pg.draw.rect(screen, true_color, (50 * (j + 1), 50 * (i + 1), 50, 50))
                elif grid_color[i][j] == 2:
                    pg.draw.rect(screen, line_color, (50 * (j + 1), 50 * (i + 1), 50, 50))
                else:
                    pg.draw.rect(screen, background_color, (50 * (j + 1), 50 * (i + 1), 50, 50))
        pg.display.update()
        for i in range(10):
            if not i % 3:
                pg.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
                pg.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
            pg.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
            pg.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
        pg.display.update()
        for i in range(len(grid[0])):
            for j in range(len(grid[0])):
                if 0 < grid[i][j] < 10:
                    value = numeric_font.render(str(grid[i][j]), True, (0, 0, 0))
                    screen.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
        pg.display.update()
        for i in range(len(grid_original[0])):
            for j in range(len(grid_original[0])):
                if 0 < grid_original[i][j] < 10:
                    value = numeric_font.render(str(grid_original[i][j]), True, original_grid_element_color)
                    screen.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
        pg.display.update()


class Finish:
    def main(self, event):
        screen.fill(background_color)
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                return 'menu'
        return 'finish'

    def draw(self, grid, grid_original):
        value = numeric_font.render('You are won!', True, (0, 0, 0))
        screen.blit(value, (250, 225))


def main():
    # ===================
    FPS = 10
    scenes = {'menu': Menu(), 'main': Main(), 'finish': Finish()}
    scene = scenes['menu']
    # ===================
    clock = pg.time.Clock()
    while True:
        offset = 3
        for event in pg.event.get():
            new = scene.main(event)
            if event.type == pg.KEYDOWN:
                position = pg.mouse.get_pos()
                i, j = position[1] // 50, position[0] // 50
                if grid_original[i - 1][j - 1] == 0:
                    if event.key == 48:
                        grid[i - 1][j - 1] = event.key - 48
                        pg.draw.rect(screen, background_color, (
                            position[0] * 50 + offset, position[1] * 50 + offset, 50 - 2 * offset, 50 - 2 * offset))
                        pg.display.update()
                        r = right_move(grid)
                        if r is not None:
                            new = r
                    elif 0 < event.key - 48 < 10:
                        pg.draw.rect(screen, background_color, (
                            position[0] * 50 + offset, position[1] * 50 + offset, 50 - 2 * offset, 50 - 2 * offset))
                        value = numeric_font.render(str(event.key - 48), True, (0, 0, 0))
                        screen.blit(value, (position[0] * 50 + 15, position[1] * 50))
                        grid[i - 1][j - 1] = event.key - 48
                        r = right_move(grid)
                        if r is not None:
                            new = r
            scene = scenes[new]
            scene.draw(grid, grid_original)
            pg.display.update()
            if event.type == pg.QUIT:
                return
        clock.tick(FPS)


if __name__ == "__main__":
    main()
