# -*-coding:utf-8-*-
import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = 1920, 1080
color = 255, 255, 255
ball = pygame.image.load('E:/vsc test/test-python/picture/ball.png')
ballrect = ball.get_rect()
# pygame.display.set_icon(ball)            # 设置窗口的图标
# pygame.display.set_caption('连连看')      # 设置窗口的名字
clock = pygame.time.Clock()     # 设置始终

speed = [5, 5]
while True:
    clock.tick(60)      # 每秒执行60次
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            sys.exit(0)
    ballrect = ballrect.move(speed)         # 移动小球
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]

    screen.fill(color)
    screen.blit(ball, ballrect)
    pygame.display.update()
