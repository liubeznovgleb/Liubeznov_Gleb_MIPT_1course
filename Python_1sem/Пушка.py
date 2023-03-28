import math
from random import randint
from random import choice
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

count = 0


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        k = 0.4
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy -= 1  # гравитация
        self.x += self.vx
        self.y -= self.vy
        if (self.x >= 800 and self.vx > 0) or (self.x <= 0 and self.vx < 0):
            self.vx = -self.vx
            self.vx *= k
        if (self.y >= 500 and self.vy < 0) or (self.y <= 0 and self.vy > 0):
            self.vy *= k
            self.vx *= k
            self.vy = -self.vy
        if abs(self.vx) <= 0.001:
            self.r = 0
            self.vx = 0
            self.vy = 0

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x1)**2 + (self.y - obj.y1)**2 <= (self.r + obj.r1)**2:
            self.live1 = 0
            return True
        elif ((self.x - obj.x2)**2 + (self.y - obj.y2)**2 <= (self.r + obj.r2)**2):
            self.level2 = 0
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event, count):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        count += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2(
            (event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        return count

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0]-20 == 0:
                self.an = - math.pi / 2
            else:
                self.an = math.atan((event.pos[1]-500) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        l = self.f2_power * 0.5
        if self.f2_power <= 10:
            self.color = GREY
        else:
            self.color = RED
        pygame.draw.polygon(screen, self.color, [[20 - 6 * math.sin(self.an), 500 + 6 * math.cos(self.an)], [20, 500], [20 + 1.3 * l * math.cos(
            self.an), 500 + 1.3 * l * math.sin(self.an)], [20 + 1.3 * l * math.cos(self.an) - 6 * math.sin(self.an), 500 + 1.3 * l * math.sin(self.an) + 6 * math.cos(self.an)]])

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        self.points = 0
        self.live1 = 1
        self.x1 = randint(600, 780)
        self.y1 = randint(300, 490)
        self.r1 = randint(20, 75)
        self.vx1 = randint(1, 10)
        self.vy1 = randint(1, 10)
        self.color1 = RED
        self.live2 = 1
        self.x2 = randint(600, 780)
        self.y2 = randint(300, 490)
        self.r2 = randint(20, 75)
        self.vx2 = randint(1, 10)
        self.vy2 = randint(1, 10)
        self.color2 = RED

    def new_target(self):
        """ Инициализация новой цели. """
        self.live1 = 1
        self.live2 = 1
        x1 = self.x1 = randint(600, 780)
        y1 = self.y1 = randint(300, 450)
        r1 = self.r1 = randint(10, 50)
        color1 = self.color1 = RED
        x2 = self.x2 = randint(600, 780)
        y2 = self.y2 = randint(300, 450)
        r2 = self.r2 = randint(10, 50)
        color2 = self.color2 = RED
        pygame.draw.circle(screen, self.color1, (self.x1, self.y1), self.r1)
        pygame.draw.circle(screen, self.color2, (self.x2, self.y2), self.r2)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(screen, self.color1, (self.x1, self.y1), self.r1)
        pygame.draw.circle(screen, self.color2, (self.x2, self.y2), self.r2)

    def move(self):
        self.x1 += self.vx1
        self.y1 -= self.vy1
        if (self.x1 >= 800 and self.vx1 > 0) or (self.x1 <= 0 and self.vx1 < 0):
            self.vx1 = -self.vx1
        if (self.y1 >= 500 and self.vy1 < 0) or (self.y1 <= 0 and self.vy1 > 0):
            self.vy1 = -self.vy1
        self.x2 += self.vx2
        self.y2 -= self.vy2
        if (self.x2 >= 800 and self.vx2 > 0) or (self.x2 <= 0 and self.vx2 < 0):
            self.vx2 = -self.vx2
        if (self.y2 >= 500 and self.vy2 < 0) or (self.y2 <= 0 and self.vy2 > 0):
            self.vy2 = -self.vy2


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
finished = False

delay_after_hit = 100

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    target.move()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            count = gun.fire2_end(event, count)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target) and target.live1:
            target.hit()
            target.live1 = 0
            print("Вы попали за", count, "выстрелов")
            count = 0
        if b.hittest(target) and target.live2:
            target.hit()
            target.live2 = 0
            print("Вы попали за", count, "выстрелов")
            count = 0
        if target.live1 == target.live2 == 0:
            if not delay_after_hit:
                delay_after_hit -= 1
            else:
                delay_after_hit = 100
                target.new_target()
    gun.power_up()

pygame.quit()

print("Всего уничтожено", 2 * target.points, "целей")
