from os import path

import pygame as pg
import pygame.image
import random
from settings import *



class Expolosion(pg.sprite.Sprite):
    def __init__(self,game,center):
        self.explosion_animation = []
        img_dir = "C:\\Users\\Administrator\\Desktop\\4_1\\AI lab\\game\\pics"
        for i in range(9):
            filename = 'regularExplosion0{}.png'.format(i)
            img = pg.image.load(path.join(img_dir, filename)).convert()
            img.set_colorkey(BLACK)
            img = pg.transform.scale(img, (TILESIZE, TILESIZE))
            self.explosion_animation.append(img)
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image=self.explosion_animation[0]
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.frame=0
        self.last_update=pg.time.get_ticks()
        self.frame_rate=50

    def update(self):
        now=pg.time.get_ticks()
        if(now-self.last_update>self.frame_rate):
            self.last_update=now
            self.frame+=1
            if self.frame==len(self.explosion_animation):
                self.kill()
            else:
                center=self.rect.center
                self.image=self.explosion_animation[self.frame]
                self.rect=self.image.get_rect()
                self.rect.center=center



class Player(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game

        self.explosion_animation = []
        img_dir = "C:\\Users\\Administrator\\Desktop\\4_1\\AI lab\\game\\pics"
        for i in range(9):
            filename = 'regularExplosion0{}.png'.format(i)
            img = pg.image.load(path.join(img_dir, filename)).convert()
            img.set_colorkey(BLACK)
            img = pg.transform.scale(img, (TILESIZE, TILESIZE))
            self.explosion_animation.append(img)
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 50

        player_img=pygame.image.load("pics//player.png").convert()
        self.image=pygame.transform.scale(player_img,(TILESIZE,TILESIZE))
        self.image.set_colorkey(BLACK)
        # self.image.fill(YELLOW)
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.turn=True
        self.health=1000
        self.yeildeds=0
        self.animate=False

    def move(self,dx=0,dy=0):
        if (self.turn):
            self.x += dx
            self.y += dy
            self.turn = False



    def update(self):
        if(self.x<0):
            self.x=0
        if (self.x >15):
            self.x = 15
        if (self.y < 0):
            self.y = 0
        if (self.y > 11):
            self.y = 11
        self.rect.x=self.x*TILESIZE
        self.rect.y = self.y * TILESIZE

        if (self.animate):
            now = pg.time.get_ticks()
            if (now - self.last_update > self.frame_rate):
                self.last_update = now
                self.frame += 1
                if self.frame == len(self.explosion_animation):
                    self.frame = 0
                    x = self.rect.x
                    y = self.rect.y
                    player_img = pygame.image.load("pics//player.png").convert()
                    self.image = pygame.transform.scale(player_img, (TILESIZE, TILESIZE))
                    self.image.set_colorkey(BLACK)
                    self.rect = self.image.get_rect()
                    self.rect.x = x
                    self.rect.y = y
                    self.animate = False
                else:
                    x = self.rect.x
                    y = self.rect.y
                    self.image = self.explosion_animation[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.x = x
                    self.rect.y = y


class AI(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)

        self.explosion_animation = []
        img_dir = "C:\\Users\\Administrator\\Desktop\\4_1\\AI lab\\game\\pics"
        for i in range(9):
            filename = 'regularExplosion0{}.png'.format(i)
            img = pg.image.load(path.join(img_dir, filename)).convert()
            img.set_colorkey(BLACK)
            img = pg.transform.scale(img, (TILESIZE, TILESIZE))
            self.explosion_animation.append(img)
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 50

        self.game=game
        player_img=pygame.image.load("pics//ai.png").convert()
        self.image=pygame.transform.scale(player_img,(TILESIZE,TILESIZE))
        self.image.set_colorkey(BLACK)
        # self.image.fill(YELLOW)
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.turn=False
        self.health=1000
        self.yeildeds = 0
        self.animate=False

    def move(self,dx=0,dy=0):
        if(self.turn):
            self.x+=dx
            self.y+=dy
            self.turn=False


    def update(self):
        if(self.x<0):
            self.x=0
        if (self.x >15):
            self.x = 15
        if (self.y < 0):
            self.y = 0
        if (self.y > 11):
            self.y = 11
        self.rect.x=self.x*TILESIZE
        self.rect.y = self.y * TILESIZE

        if(self.animate):
            now = pg.time.get_ticks()
            if (now - self.last_update > self.frame_rate):
                self.last_update = now
                self.frame += 1
                if self.frame == len(self.explosion_animation):
                    self.frame=0
                    x = self.rect.x
                    y = self.rect.y
                    player_img = pygame.image.load("pics//ai.png").convert()
                    self.image = pygame.transform.scale(player_img, (TILESIZE, TILESIZE))
                    self.image.set_colorkey(BLACK)
                    self.rect = self.image.get_rect()
                    self.rect.x = x
                    self.rect.y = y
                    self.animate = False
                else:
                    x = self.rect.x
                    y=self.rect.y
                    self.image = self.explosion_animation[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.x=x
                    self.rect.y=y



class W1(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites,game.ww1
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        player_img = pygame.image.load("pics//arrow.png").convert()
        self.image = pygame.transform.scale(player_img, (TILESIZE-10, TILESIZE-10))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.damage=100
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class W2(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites,game.ww2
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        player_img = pygame.image.load("pics//swords.png").convert()
        self.image = pygame.transform.scale(player_img, (TILESIZE-10, TILESIZE-10))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.damage=300
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class W3(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites,game.ww3
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        player_img = pygame.image.load("pics//hand-gun.png").convert()
        self.image = pygame.transform.scale(player_img, (TILESIZE-10, TILESIZE-10))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.damage=700
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class S3(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites,game.ss3
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        player_img = pygame.image.load("pics//bullet-proof.png").convert()
        self.image = pygame.transform.scale(player_img, (TILESIZE-10, TILESIZE-10))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.damage1=60
        self.damage2=200
        self.damage3 = 0
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class S2(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites,game.ss2
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        player_img = pygame.image.load("pics//sword (1).png").convert()
        self.image = pygame.transform.scale(player_img, (TILESIZE-10, TILESIZE-10))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.damage1=70
        self.damage3=600
        self.damage2 = 0
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class S1(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites,game.ss1
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        player_img = pygame.image.load("pics//shield (arrow brown ..).png").convert()
        self.image = pygame.transform.scale(player_img, (TILESIZE-10, TILESIZE-10))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.damage2=260
        self.damage3=650
        self.damage1 = 0
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE