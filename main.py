import sys, pygame
pygame.init()

size = width, height = 1130, 830
white = 255, 255, 255
black = 0, 0, 0
grey = 133, 133, 133
green = 50, 205, 50
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
    t1 = f1.render(x_names[i], 0, black)
    screen.blit(t1, (x + 44, y))
    x += 100

x, y = 800, 0
for i in range(8):
    pygame.draw.rect(screen, white, (x, y, 30, 100))
    pygame.draw.rect(screen, brown, (x, y, 30, 98), 4)
    t1 = f1.render(str(i+1), 0, black)
    screen.blit(t1, (x+7, y+40))
    y += 100
pygame.draw.rect(screen, brown, (798, 798, 34, 32))

# загружаем картинки
checker_white = pygame.image.load('images/white.png')
checker_black = pygame.image.load('images/black.png')

# уменьшаем их в размере
checker_white = pygame.transform.scale(checker_white, (100, 100))
checker_black = pygame.transform.scale(checker_black, (100, 100))


class Checker:
    def __init__(self, name, checker_color, border, queen, x, y):
        self.name = name
        self.checker_color = checker_color
        self.border = border
        self.queen = queen
        self.x = x
        self.y = y

    def click_1(self):
        # self.possible_kick()
        self.checked()
        self.possible_hod()
        # self.click_2()

    # def click_2(self):


    def checked(self):
        pygame.draw.rect(screen, green, (self.x, self.y, 99, 99), 2)

    def possible_hod(self):
        if self.queen:
            pass
        else:
            # ищем клетки куда можно походить в зависимости от цвета ходящего
            # возможные клетки записываем в масив hodim
            hodim = list()
            a = x_names.index(self.name[:1])
            if a > 0:
                hodim.append(x_names[a - 1])
            if a < 7:
                hodim.append(x_names[a + 1])
            if hod:
                for i in range(len(hodim)):
                    hodim[i] += str(int(self.name[1:]) + 1)
            else:
                for i in range(len(hodim)):
                    hodim[i] += str(int(self.name[1:]) - 1)

            # проверка заняты ли клетки спереди, если да - удаляем
            for i in arr:
                if i.name in hodim:
                    if i.checker_color != 2:
                        hodim.remove(i.name)
            if not hodim:
                print('Ходов у данной шашки нет')
                del hodim
            else:
                self.hodim = hodim
                print(self.hodim)


    def possible_kick(self):
        if self.queen:
            pass
        else:
            pos_kicks = list()
            num = 0
            semicolored = list()
            for i in arr:
                if i.checker_color == hod:
                    num += 1
                    semicolored.append(i.name)
            print(semicolored)
            for j in semicolored:
                kick = list()
                a = x_names.index(j[:1])
                try:
                    kick.append(x_names[a-1])
                    kick.append(x_names[a+1])
                except IndexError:
                    pass

                kick += kick[:]
                b = [int(j[1:])-1, int(j[1:])+1]

                for i in range(2):
                    kick[i] += str(b[0])
                for i in range(2, 4):
                    kick[i] += str(b[1])
                print(kick)

                pos_kicks.append(kick)








names1 = ['b1', 'd1', 'f1', 'h1',
          'a2', 'c2', 'e2', 'g2',
          'b3', 'd3', 'f3', 'h3',
          'a4', 'c4', 'e4', 'g4',
          'b5', 'd5', 'f5', 'h5',
          'a6', 'c6', 'e6', 'g6',
          'b7', 'd7', 'f7', 'h7',
          'a8', 'c8', 'e8', 'g8']

# checker_color
# 2 - пустой
# 0 - белый
# 1 - чорный
# border - 1/0
# queen - 1/0
# создаем список обектов для каждой чорной ячейки, также придаем каждому свое значение.

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
        arr.append(Checker(names1[i], 2, 0, 0, x_coord, y_coord))
    else:
        arr.append(Checker(names1[i], 0, 0, 0, x_coord, y_coord))
        screen.blit(checker_white, (x_coord, y_coord))
    x_coord += 200
    if x_coord > 700:
        y_coord += 100
        x_coord = 0


def find_exemplar(x, y, h):
    x, y = (x // 100) * 100, (y // 100) * 100
    for i in arr:
        if i.x == x and i.y == y and i.checker_color == h:
            return i

# главный цикл
# False  - ходит белый
# True - ходит чорный


# считываем клик и находим обект на который кликнули
def clicks():
    if pygame.mouse.get_pressed() == (1, 0, 0):
        x, y = pygame.mouse.get_pos()
        checker = find_exemplar(x, y, hod)
        return checker


hod = False
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        checker = clicks()
        try:
            print(checker.name)
            # checker.checked()
            # checker.possible_hod()
            checker.click_1()
        except AttributeError:
            del checker


        pygame.display.update()