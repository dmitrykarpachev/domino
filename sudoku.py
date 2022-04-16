import pygame
import requests
from functools import reduce


WIDTH = HEIGHT = 550
background_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)
offset = 3
grid_color = [[0 for _ in range(9)] for _ in range(9)]
true_color = (60, 179, 113)
line_color = (0, 255, 127)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
my_font = pygame.font.SysFont('Comic Sans MS', 35)


def right_move(grid):
    global grid_color
    lastI = 0
    for i in range(3, 10, 3):
        lastJ = 0
        for j in range(3, 10, 3):
            mas = reduce(lambda a, b: a + b, list(map(lambda line: line[lastJ:j], grid[lastI:i])))
            if sum(mas) == 45 and len(set(mas)) == len(mas):
                for y in range(lastI, i):
                    for x in range(lastJ, j):
                        grid_color[y][x] = 1
            else:
                for y in range(lastI, i):
                    for x in range(lastJ, j):
                        grid_color[y][x] = 0
            lastJ = j
        lastI = i
        for i in range(9):
            if sum(grid[i]) == 45 and len(set(grid[i])) == len(grid[i]):
                grid_color[i] = [2] * 9
        for j in range(9):
            new_line = [line[j] for line in grid]
            if sum(new_line) == 45 and len(set(new_line)) == len(new_line):
                for i in range(9):
                    grid_color[i][j] = 2


def insert(screen, position, grid, grid_original):
    global my_font
    i, j = position[1], position[0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if grid_original[i - 1][j - 1] != 0:
                    return
                if event.key == 48:
                    grid[i - 1][j - 1] = event.key - 48
                    pygame.draw.rect(screen, background_color, (
                        position[0] * 50 + offset, position[1] * 50 + offset, 50 - 2 * offset, 50 - 2 * offset))
                    pygame.display.update()
                    return
                if 0 < event.key - 48 < 10:
                    print(event.key)
                    pygame.draw.rect(screen, background_color, (
                        position[0] * 50 + offset, position[1] * 50 + offset, 50 - 2 * offset, 50 - 2 * offset))
                    value = my_font.render(str(event.key - 48), True, (0, 0, 0))  # печать цифры
                    screen.blit(value, (position[0] * 50 + 15, position[1] * 50))
                    grid[i - 1][j - 1] = event.key - 48
                    pygame.display.update()
                    return
                return


def game(grid, grid_original):
    for i in range(9):
        for j in range(9):
            if grid_color[i][j] == 1:
                pygame.draw.rect(screen, true_color, (50 * (j + 1), 50 * (i + 1), 50, 50))
            elif grid_color[i][j] == 2:
                pygame.draw.rect(screen, line_color, (50 * (j + 1), 50 * (i + 1), 50, 50))
            else:
                pygame.draw.rect(screen, background_color, (50 * (j + 1), 50 * (i + 1), 50, 50))
    pygame.display.update()
    for i in range(10):
        if not i % 3:
            pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()
    for i in range(len(grid[0])):
        for j in range(len(grid[0])):
            if 0 < grid[i][j] < 10:
                value = my_font.render(str(grid[i][j]), True, (0, 0, 0))
                screen.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()
    for i in range(len(grid_original[0])):
        for j in range(len(grid_original[0])):
            if 0 < grid_original[i][j] < 10:
                value = my_font.render(str(grid_original[i][j]), True, original_grid_element_color)
                screen.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(screen, (pos[0] // 50, pos[1] // 50), grid, grid_original)
                right_move(grid)
                game(grid, grid_original)
            if event.type == pygame.QUIT:
                pygame.quit()
                return

def main():
    screen.fill(background_color)

    response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")

    grid_original = response.json()['board']
    grid = [[grid_original[x][y] for y in range(len(grid_original[0]))] for x in range(len(grid_original))]
    game(grid, grid_original)


if __name__ == '__main__':
    main()
