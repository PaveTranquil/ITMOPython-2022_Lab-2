import csv
import os
import time


def esc(code):
    return f'\u001b[{code}m'


BLACK, RED, BLUE, WHITE, END = esc(40), esc(41), esc(44), esc(47), esc(0)


# Задание №1 (флаг)
def flag_th():
    for color in RED, WHITE, BLUE, BLUE, WHITE, RED:
        print(color + '  ' * 9 + END)


flag_th()
print()


# Задание №2 (узор)
def print_graphics(grph):
    for i in range(len(grph)):
        line = ''
        for j in range(len(grph[i])):
            if grph[i][j] == 0:
                line += ' '
            elif grph[i][j] == 1:
                line += BLACK + ' ' + END
        for j in range(len(grph[i]) - 1, -1, -1):
            if grph[i][j] == 0:
                line += ' '
            elif grph[i][j] == 1:
                line += BLACK + ' ' + END
        print(line)


graphics = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print_graphics(graphics)
print()


# Задание №3 (функция)
def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 14:
                array_in[i][j] = round(INPUT_VALUES[j], 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[8 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(plot[i][0]) + ' '
            if plot[i][j] == 0:
                line += '     '
            elif plot[i][j] == 1:
                line += BLACK + '     ' + WHITE
        line += END
        print(line)
    print(WHITE + '0   ' + ''.join([str(n) + ' ' * (5 - len(str(n))) for n in INPUT_VALUES]) + END)


INPUT_VALUES = [0.1, 0.125, 0.2, 0.5, 1, 2, 4, 5, 10]

array_plot = [[0 for __ in range(10)] for _ in range(10)]
result = [1 / i for i in INPUT_VALUES]

step = round(abs((result[8] - result[0])) / 9, 1)

array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)
print()


# Задание №4 (диаграмма)
with open('books.csv', encoding='windows-1251') as f:
    reader = csv.DictReader(f, delimiter=';', quotechar='"')
    books = list(reader)

lae_50 = len(list(filter(lambda x: float(x['Цена поступления'].replace(',', '.')) <= 50, books)))
m_50 = len(list(filter(lambda x: float(x['Цена поступления'].replace(',', '.')) > 50, books)))
more_50 = str(100 - round(lae_50 * 100 / m_50, 1)) + '  '
less_and_equal_50 = str(round(lae_50 * 100 / m_50, 1)) + '  '
spaces = max(len(str(less_and_equal_50)), len(str(more_50))) * ' '
to_black, to_white = lambda a: BLACK + a + END, lambda a: WHITE + a + END

graphics = [
    [to_white(more_50), to_white(spaces), to_white(spaces), to_black(spaces)],
    [to_white(spaces), to_white(spaces), to_white(spaces), to_black(spaces)],
    [to_white(spaces), to_white(spaces), to_white(spaces), to_black(spaces)],
    [to_white(spaces), to_white(spaces), to_white(spaces), to_black(spaces)],
    [to_white(spaces), to_white(spaces), to_white(spaces), to_black(spaces)],
    [to_white(spaces), to_white(spaces), to_white(spaces), to_black(spaces)],
    [to_white(spaces), to_white(spaces), to_white(spaces), to_black(spaces)],
    [to_white(spaces), to_white(spaces), to_white(spaces), to_black(spaces)],
    [to_white(spaces), to_white(spaces), to_white(spaces), to_black(spaces)],
    [to_white(less_and_equal_50), to_black(spaces), to_white(spaces), to_black(spaces)],
    [to_white(spaces), to_black(spaces), to_white(spaces), to_black(spaces)],
    [to_white(spaces + ' '), to_white('≤ 50 '), to_white(spaces + ' '), to_white('> 50 ')]
]

print('\n'.join([''.join(line) for line in graphics]))

input('Нажмите для проигрывания анимации допзадания...')


# Допзадание (анимация)
mario_main = [
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 2, 2, 2, 3, 3, 2, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0, 0],
    [0, 0, 0, 2, 3, 2, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0],
    [0, 0, 0, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 2, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 0, 0, 0],
    [0, 0, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 0, 0],
    [0, 0, 3, 3, 2, 1, 3, 1, 1, 3, 1, 2, 3, 3, 0, 0],
    [0, 0, 3, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 3, 0, 0],
    [0, 0, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0]
]

mario_animation = [
    [
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 2, 3, 3, 2, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0, 0],
        [0, 0, 0, 2, 3, 2, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0],
        [0, 0, 0, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0],
        [0, 0, 2, 2, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0],
        [3, 3, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3, 0],
        [3, 3, 3, 0, 2, 2, 1, 3, 1, 1, 1, 2, 2, 3, 3, 0],
        [3, 3, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0, 0],
        [0, 2, 2, 1, 1, 1, 0, 0, 0, 1, 1, 1, 2, 2, 0, 0],
        [0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 2, 3, 3, 2, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0, 0],
        [0, 0, 0, 2, 3, 2, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0],
        [0, 0, 0, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 2, 1, 1, 3, 1, 1, 3, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 2, 3, 3, 3, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 3, 3, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 2, 2, 2, 3, 3, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0],
        [0, 0, 0, 0, 2, 3, 2, 2, 3, 3, 3, 2, 3, 3, 3, 0],
        [0, 0, 0, 0, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 2, 2, 2, 1, 2, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 3, 2, 2, 2, 2, 2, 2, 3, 3, 3, 0, 0],
        [0, 0, 0, 3, 3, 1, 2, 2, 2, 2, 2, 3, 3, 0, 0, 0],
        [0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 2, 2, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0]
    ]
]

GREEN, YELLOW = esc(42), esc(43)

os.system('cls' if os.name == 'nt' else 'clear')
print('Mario')
for row in range(16):
    for col in range(16):
        if mario_main[row][col] == 0:
            print(WHITE + ' ', end='')
        elif mario_main[row][col] == 1:
            print(RED + ' ', end='')
        elif mario_main[row][col] == 2:
            print(GREEN + ' ', end='')
        elif mario_main[row][col] == 3:
            print(YELLOW + ' ', end='')
    print(END)

time.sleep(2)

for s in [0, 1, 2] * 100:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Mario')
    mario = mario_animation[s]
    for row in range(16):
        for col in range(16):
            if mario[row][col] == 0:
                print(WHITE + ' ', end='')
            elif mario[row][col] == 1:
                print(RED + ' ', end='')
            elif mario[row][col] == 2:
                print(GREEN + ' ', end='')
            elif mario[row][col] == 3:
                print(YELLOW + ' ', end='')
        print(END)
    time.sleep(0.05)
