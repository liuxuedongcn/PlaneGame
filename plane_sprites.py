# encoding=UTF-8
import random
import pygame
import plane_game

# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 600)
# 刷新频率
FRAME_PER_SEC = 60
# 敌机定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#发射子弹
HERO_FIRE_EVENT=pygame.USEREVENT+1


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    def __init__(self, is_alt=False):
        super().__init__("./image/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height
        pass


class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./image/enemy0.png")
        self.speed = random.randint(1, 3)
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("敌机被销毁了")


class Hero(GameSprite):
    def __init__(self):
        super().__init__("./image/hero1.png", 0)
        self.rect.x = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.bottom - 120

        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x-=self.speed
        if self.rect.x>SCREEN_RECT.width-100:
            self.rect.x-=self.speed
    def fire(self):
        bullet = Bullet()
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.y = self.rect.y-20

        self.bullets.add(bullet)

class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./image/bullet1.png",-2)

    def update(self):
        super().update()
        if self.rect.bottom <0:
            self.kill()
    def __del__(self):
        print("子弹销毁了")