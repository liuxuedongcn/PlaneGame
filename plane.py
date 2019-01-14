#encoding=UTF-8
import pygame
from plane_sprites import *
pygame.init()
#创建窗口
screem = pygame.display.set_mode((480,600))

bg=pygame.image.load("./image/background.png")
hero = pygame.image.load("./image/hero1.png")
screem.blit(bg,(0,0))
screem.blit(hero,(200,500))
pygame.display.update()
clock = pygame.time.Clock()

hero_rect = pygame.Rect(200,500,100,122)

enemy = GameSprite("./image/enemy0.png")
enemy_grop = pygame.sprite.Group(enemy)
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit();
            exit();


    if hero_rect.y<=-122 :
        hero_rect.y=600
    hero_rect.y -= 1
    screem.blit(bg, (0, 0))
    screem.blit(hero,hero_rect)

    enemy_grop.update()
    enemy_grop.draw(screem)

    pygame.display.update()
pygame.quit()
