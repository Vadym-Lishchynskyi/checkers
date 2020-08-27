import sys, pygame
pygame.init()

size = width, height = 800, 800
white = 255, 255, 255
black = 133, 133, 133
red = 250, 0, 0

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

# загружаем картинки
checker_white = pygame.image.load('images/white.png')
checker_black = pygame.image.load('images/black.png')

# уменьшаем их в размере
checker_white = pygame.transform.scale(checker_white, (100, 100))
checker_black = pygame.transform.scale(checker_black, (100, 100))







# главный цикл

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()



        pygame.display.update()