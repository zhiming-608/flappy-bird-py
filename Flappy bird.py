# -*-coding:utf-8-*-
import pygame
import sys
import random


class Game(object):
    def __init__(self):
        self.status = 0             # 0：开始界面  1：游戏界面  2：死亡画面
        self.start = pygame.image.load("./picture/assets/start.png")
        self.topic = pygame.image.load("./picture/assets/topic.png")
        self.gameover = pygame.image.load("./picture/assets/gameover.png")
        self.score = 0

    def drawBack(self):
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        screen.blit(pipe.pipeUp, (pipe.x_pos, pipe.y_pos))
        screen.blit(pipe.pipeDown, (pipe.x_pos, pipe.y_pos + 790))
        screen.blit(self.topic, (111, 150))
        screen.blit(self.start, (155, 312))


class Bird(object):
    def __init__(self):
        # 初始化
        self.rect = pygame.Rect(50, 350, 34, 24)
        self.status = [pygame.image.load("./picture/assets/0.png"),
                       pygame.image.load("./picture/assets/1.png"),
                       pygame.image.load("./picture/assets/2.png")]
        self.statusIndex = 0
        self.x_pos = 50
        self.y_pos = 350
        self.gravity = 3
        self.jump = True
        self.jumpSpeed = 10

    def updatePos(self):
        if self.jump:
            self.jumpSpeed -= 0.5
            self.y_pos -= self.jumpSpeed
        else:
            self.gravity += 0.02
            self.y_pos -= self.gravity
        self.rect[1] = int(self.y_pos)

    def updateStatus(self):
        if self.jump and self.jumpSpeed > 0:
            self.statusIndex = 2
        else:
            self.statusIndex = 1


class Pipeline(object):
    def __init__(self):
        # 初始化
        self.x_gap = 3
        self.x_pos = width
        self.y_pos = random.randint(-630, -150)
        self.pipeDown = self.pipeUp = pygame.image.load("./picture/assets/pipe.png")

    def updatePos(self):
        self.x_pos -= self.x_gap
        if self.x_pos < -90:
            self.x_pos = width
            self.y_pos = random.randint(-630, -150)


def checkScore():
    if pipe.x_pos + pipe.pipeUp.get_width() // 2 < 50 + 17:         # 小鸟通过管道一半则视为通过
        game.score += 1


def checkIsDead():
    pipeUpRect = pygame.Rect(pipe.x_pos, pipe.y_pos, pipe.pipeUp.get_width(), pipe.pipeUp.get_height())
    pipeDownRect = pygame.Rect(pipe.x_pos, pipe.y_pos + 790, pipe.pipeUp.get_width(), pipe.pipeUp.get_height())
    # 检测是否超过下面边界
    if bird.rect[1] > height or pipeUpRect.colliderect(bird.rect) or pipeDownRect.colliderect(bird.rect):
        game.status = 2
    else:
        game.status = 1


def drawlaunch():
    bird.__init__()
    pipe.__init__()
    game.__init__()
    screen.blit(background, (0, 0))
    tip_text = 'press "SPACE" or click to play'
    tip_text_font = pygame.font.SysFont('Arial', 30)
    tip_text_surf = tip_text_font.render(tip_text, True, (255, 255, 255))
    screen.blit(tip_text_surf, (screen.get_width() // 2 - tip_text_surf.get_width() // 2, 600))
    screen.blit(bird.status[bird.statusIndex], (bird.x_pos, int(bird.y_pos)))           # 显示背景中的鸟和管道
    screen.blit(game.topic, (111, 150))
    screen.blit(game.start, (155, 312))

    pygame.display.update()


def showScore():
    screen.blit(background, (0, 0))
    screen.blit(pipe.pipeUp, (pipe.x_pos, pipe.y_pos))
    screen.blit(pipe.pipeDown, (pipe.x_pos, pipe.y_pos + 790))
    score_text = 'your score is :' + str(game.score)
    score_text_font = pygame.font.SysFont('Arial', 50)
    score_text_surf = score_text_font.render(score_text, True, (0, 0, 0))
    screen.blit(game.gameover, (111, 150))
    screen.blit(score_text_surf, (screen.get_width() // 2 - score_text_surf.get_width() // 2, 200))
    screen.blit(game.start, (155, 312))
    screen.blit(bird.status[bird.statusIndex], (bird.x_pos, int(bird.y_pos)))

    pygame.display.update()


def updateMap():
    screen.blit(background, (0, 0))
    # 显示小鸟
    bird.updatePos()
    bird.updateStatus()
    screen.blit(bird.status[bird.statusIndex], (bird.x_pos, int(bird.y_pos)))

    # 显示管道
    pipe.updatePos()
    screen.blit(pipe.pipeUp, (pipe.x_pos, pipe.y_pos))
    screen.blit(pipe.pipeDown, (pipe.x_pos, pipe.y_pos + 790))      # 上下管道中间差值为150 管道图片长为640

    pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 400, 650
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    game = Game()
    bird = Bird()
    pipe = Pipeline()
    pygame.display.set_icon(bird.status[0])                   # 设置窗口的图标
    pygame.display.set_caption('Flappy bird')       # 设置窗口的名字
    screen.fill((255, 255, 255))
    while True:
        clock.tick(60)
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif key[pygame.K_ESCAPE]:
                # 暂停
                pass
            elif game.status == 1 and (event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_SPACE]):
                bird.jump = True
                bird.jumpSpeed = 10
                bird.gravity = 5
            elif game.status == 0 and ((event.type == pygame.MOUSEBUTTONDOWN and 155 < event.pos[0] < 259 and 312 < event.pos[1] < 370) or key[pygame.K_SPACE]):
                game.status = 1
            elif game.status == 2 and (event.type == pygame.MOUSEBUTTONDOWN and 155 < event.pos[0] < 259 and 312 < event.pos[1] < 370):
                bird.__init__()
                pipe.__init__()
                game.status = 0

        background = pygame.image.load("./picture/assets/background.png")

        if game.status == 0:
            drawlaunch()
        elif game.status == 2:
            # 结束画面
            showScore()
        elif game.status == 1:
            # 游戏界面
            updateMap()
            checkScore()
            checkIsDead()
    pygame.quit()
