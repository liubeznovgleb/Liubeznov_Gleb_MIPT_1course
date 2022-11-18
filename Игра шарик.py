import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 50      # Насколько быстро обновляется экран
screen = pygame.display.set_mode((1200, 900))   # Размер экрана

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    '''рисует новые шарики, где x, y - координаты, r - радиус vx, vy - скорость, colour - цвет шарика  '''
    x1, x2 = randint(100, 1100), randint(100, 1100)
    y1, y2 = randint(100, 900), randint(100, 900)
    r1, r2 = randint(30, 100), randint(30, 100)
    vx1, vy1 = randint(-10, 10), randint(-10, 10)
    vx2, vy2 = randint(-10, 10), randint(-10, 10)
    color1, color2 = COLORS[randint(0, 5)], COLORS[randint(0, 5)]
    circle(screen, color1, (x1, y1), r1)
    circle(screen, color2, (x2, y2), r2)
    return (x1, y1, r1, vx1, vy1, color1), (x2, y2, r2, vx2, vy2, color2)



def ball_move(ball_1, ball_2):
    '''реализует движение шариков, путем изменения их координат на число, равное скорости шариков и "гравитацию", путём изменения скорости'''
    x1, y1, r1, vx1, vy1, color1 = ball_1
    x2, y2, r2, vx2, vy2, color2 = ball_2
    screen.fill(BLACK)
    x1 += vx1
    y1 += vy1
    x2 += vx2
    y2 += vy2
    vy1 += 1
    vy2 += 1
    circle(screen, color1, (x1, y1), r1)
    circle(screen, color2, (x2, y2), r2)
    return (x1, y1, r1, vx1, vy1, color1), (x2, y2, r2, vx2, vy2, color2)

def collision(ball1, ball2):
    '''реализует столкновение шариков со стенами, при котором скорость шариков меняется на обратную с тем же значением по модулю'''
    ball1, ball2 = list(ball1), list(ball2)
    if ball1[0] <= 0 or ball1[0] >= 1200:
        ball1[3] -= 2*ball1[3]
    if ball1[1] <= 0 or ball1[1] >= 900:
        ball1[4] -= 2*ball1[4]
    if ball2[0] <= 0 or ball2[0] >= 1200:
        ball2[3] -= 2*ball2[3]
    if ball2[1] <= 0 or ball2[1] >= 900:
        ball2[4] -= 2*ball2[4]
    return ball1, ball2


def click(x0, y0, ball1, ball2, hit, misses):
    '''функция реализует попадание или промах нажатия мышки по шарикам'''
    if ((ball1[0] - x0) ** 2 + (ball1[1] - y0) ** 2) <= ball1[2] ** 2:
        print("Попал")
        ball1[2] = 0
        hit += 1
    elif ((ball2[0] - x0) ** 2 + (ball2[1] - y0) ** 2) <= ball2[2] ** 2:
        print("Попал")
        ball2[2] = 0
        hit += 1
    else:
        print("Промазал")
        misses += 1
    return hit, misses


pygame.display.update()
clock = pygame.time.Clock()
finished = False
hit, misses = 0, 0

ball1, ball2 = new_ball()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x0, y0 = event.pos
                hit, misses = click(x0, y0, ball1, ball2, hit, misses)
        if ball1[2] == ball2[2] == 0:
            ball1, ball2 = new_ball()   # спавнит новые шарики кода оба старых исчезли
    ball1, ball2 = ball_move(ball1, ball2)
    ball1, ball2 = collision(ball1, ball2)
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
print("Попаданий -", hit)
print("Промахов -", misses)