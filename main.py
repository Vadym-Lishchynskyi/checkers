import sys, pygame
pygame.init()

size = width, height = 1020, 820
white = 255, 255, 255
black = 133, 133, 133
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
        pygame.draw.rect(screen, black, (x, y, 100, 100))
    x += 100
    n = not n
    if x > 700:
        y += 100
        x = 0
        n = not n

# рисуем название ячеек
x, y = 0, 800
for i in range(8):
    pygame.draw.rect(screen, white, (x, y, 100, 20))
    pygame.draw.rect(screen, brown, (x, y, 98, 20),4)
    x += 100

x, y = 800, 0
for i in range(8):
    pygame.draw.rect(screen, white, (x, y, 20, 100))
    pygame.draw.rect(screen, brown, (x, y, 20, 98),4)
    y += 100
pygame.draw.rect(screen, brown, (798, 798, 24, 23))


# загружаем картинки
checker_white = pygame.image.load('images/white.png')
checker_black = pygame.image.load('images/black.png')

# уменьшаем их в размере
checker_white = pygame.transform.scale(checker_white, (100, 100))
checker_black = pygame.transform.scale(checker_black, (100, 100))


class Checker:
    pass







# главный цикл

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()



        pygame.display.update()