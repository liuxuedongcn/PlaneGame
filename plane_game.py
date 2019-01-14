# encoding=UTF-8
import pygame
from plane_sprites import *


class PlaneGame(object):
    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_spries()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __create_spries(self):
        bg1 = Background()
        bg2 = Background(True)
        self.bg_grop = pygame.sprite.Group(bg1, bg2)
        self.enemy_grop = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_grop = pygame.sprite.Group(self.hero)



    def start_game(self):
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()
            # 查看事件

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出厂")
                enemy = Enemy()
                self.enemy_grop.add(enemy)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.hero.speed=2
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.hero.speed=-2
            elif event.type == pygame.KEYUP:
                self.hero.speed=0
            elif event.type==HERO_FIRE_EVENT:
                self.hero.fire()
    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_grop,True,True)
        pygame.sprite.groupcollide(self.hero_grop,self.enemy_grop,True,True)
        if not self.hero_grop.has(self.hero):
            PlaneGame.__game_over()
    # 更新精灵
    def __update_sprites(self):
        self.bg_grop.update()
        self.bg_grop.draw(self.screen)

        self.enemy_grop.update()
        self.enemy_grop.draw(self.screen)

        self.hero_grop.update()
        self.hero_grop.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("退出游戏")
        pygame.quit();
        exit();


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
