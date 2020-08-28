import sys, pygame
pygame.init()

size = width, height = 1130, 830
white = 255, 255, 255
grey = 133, 133, 133
black = 0, 0, 0
red = 250, 0, 0
brown = 153, 51, 51

screen = pygame.display.set_mode(size)

# Создание доски
x, y = 0, 0
n = True
for i in range(64):
    if n:
        pygame.draw.rect(screen, white, (x, y, 100, 100))
    else:
        pygame.draw.rect(screen, grey, (x, y, 100, 100))
    x += 100
    n = not n
    if x > 700:
        y += 100
        x = 0
        n = not n

# рисуем название ячеек
# добавляем название ячеек сразу
f1 = pygame.font.SysFont('serif', 27)
x_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x, y = 0, 800
for i in range(8):
    pygame.draw.rect(screen, white, (x, y, 100, 30))
    pygame.draw.rect(screen, brown, (x, y, 98, 30), 4)
    t1 = f1.render(x_names[i], 0, (black))
    screen.blit(t1, (x + 44, y))
    x += 100

x, y = 800, 0
for i in range(8):
    pygame.draw.rect(screen, white, (x, y, 30, 100))
    pygame.draw.rect(screen, brown, (x, y, 30, 98), 4)
    t1 = f1.render(str(i+1), 0, (black))
    screen.blit(t1, (x+7, y+40))
    y += 100
pygame.draw.rect(screen, brown, (798, 798, 34, 32))



# загружаем картинки
checker_white = pygame.image.load('images/white.png')
checker_black = pygame.image.load('images/black.png')

# уменьшаем их в размере
checker_white = pygame.transform.scale(checker_white, (100, 100))
checker_black = pygame.transform.scale(checker_black, (100, 100))


class Checker():
    def __init__(self, name, checker_color, border, queen, x, y):
        self.name = name
        self.checker_color = checker_color
        self.border = border
        self.queen = queen
        self.x = x
        self.y = y

    def checked(self):
        pass

    def ris_checker(self):
        pass

    def ris_block(self):
        pass




names1 = ['b1', 'd1', 'f1', 'h1',
          'a2', 'c2', 'e2', 'g2',
          'b3', 'd3', 'f3', 'h3',
          'a4', 'c4', 'e4', 'g4',
          'b5', 'd5', 'f5', 'h5',
          'a6', 'c6', 'e6', 'g6',
          'b7', 'd7', 'f7', 'h7',
          'a8', 'c8', 'e8', 'g8']

# checker_color
# 0 - пустой
# 1 - белый
# 2 - чорный
# border - 1/0
# queen - 1/0

arr = list()
n = False
x_coord, y_coord = 0, 0
for i in range(32):
    if i % 8 == 0:
        n = not n
    if n:
        x_coord = 100
        n = not n
    if i < 12:
        arr.append(Checker(names1[i], 1, 0, 0, x_coord, y_coord))
        screen.blit(checker_black, (x_coord, y_coord))
    elif i < 20:
        arr.append(Checker(names1[i], 0, 0, 0, x_coord, y_coord))
    else:
        arr.append(Checker(names1[i], 2, 0, 0, x_coord, y_coord))
        screen.blit(checker_white, (x_coord, y_coord))
    x_coord += 200
    if x_coord > 700:
        y_coord += 100
        x_coord = 0


def find_exemplar(x, y):
    x, y = (x // 100) * 100, (y // 100) * 100
    print(x, y)
    for i in arr:
        if i.x == x and i.y == y:
            return i



# главный цикл

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if pygame.mouse.get_pressed() == (1, 0, 0):
            x, y = pygame.mouse.get_pos()
            checker = find_exemplar(x, y)
            try:
                print(checker.name)
            except AttributeError:
                print(0)
        pygame.display.update()