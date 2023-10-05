import sys
import random
from os import path

import numpy as np
import pygame as pg
import pygame.font

from settings import *
from sprites import *
from a_star import *



class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen=pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock=pg.time.Clock()
        self.restricted_points=[]
        print(WIDTH//TILESIZE,HEIGHT//TILESIZE)
        self.snd_dir=path.join(path.dirname(__file__),'sound')
        pg.mixer.music.load(path.join(self.snd_dir,'Opening.mp3'))
        self.pw_sound=pg.mixer.Sound(path.join(self.snd_dir,'Powerup4.wav'))
        self.s_sound = pg.mixer.Sound(path.join(self.snd_dir, 's.wav'))
        self.d_sound=pg.mixer.Sound(path.join(self.snd_dir, 'Explosion4.wav'))
        pg.mixer.music.set_volume(.5)
        self.mat=[['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],
                  ['','','','','','','','','','','',''],]
        for i in range(0,WIDTH//TILESIZE):
            for j in range(0,HEIGHT//TILESIZE):
                self.mat[i][j]='0'
        pg.key.set_repeat(500,100)





    def no_weapons_left(self):
        flag=True
        for i in range(0,WIDTH//TILESIZE):
            for j in range(0,HEIGHT//TILESIZE):
                if(self.mat[i][j]=='w11' or self.mat[i][j]=='w12' or self.mat[i][j]=='w21' or self.mat[i][j]=='w22' or self.mat[i][j]=='w31' or self.mat[i][j]=='w32'):
                    flag=False
        return flag

    def draw_text(self,surf,text,size,x,y):
        font_name = pygame.font.match_font('arial')
        font=pygame.font.Font('font/ka1.ttf',size)
        text_surface=font.render(text,True,WHITE)
        text_react=text_surface.get_rect()
        text_react.x=x*TILESIZE
        text_react.y = y * TILESIZE
        surf.blit(text_surface,text_react)


    def generate_corordinates(self):
        while (True):
            flag = True
            x = random.randrange(0, 16)
            y = random.randrange(0, 12)
            for i in self.restricted_points:
                if ((x, y) == i):
                    flag = False
                    break
            if (flag):
                break
        self.restricted_points.append((x, y))
        return (x,y)

    def new(self):
        self.all_sprites=pg.sprite.Group()
        self.ww1=pg.sprite.Group()
        self.ww2 = pg.sprite.Group()
        self.ww3 = pg.sprite.Group()
        self.ss1 = pg.sprite.Group()
        self.ss2 = pg.sprite.Group()
        self.ss3 = pg.sprite.Group()
        self.player=Player(self,0,11)
        self.mat[0][11]='p'
        self.ai=AI(self,15,0)
        self.mat[15][0] = 'a'
        self.restricted_points.append((15,0))
        self.restricted_points.append((0,11))

        # w1
        (x,y)=self.generate_corordinates()
        self.w1=W1(self,x,y)
        self.mat[x][y]='w1'
        # w2

        (x,y)=self.generate_corordinates()
        self.w2 = W2(self, x, y)
        self.mat[x][y] = 'w2'
        # w3

        (x, y) = self.generate_corordinates()
        self.w3 = W3(self, x, y)
        self.mat[x][y] = 'w3'
        #s3
        (x, y) = self.generate_corordinates()
        self.s3 = S3(self, x, y)
        self.mat[x][y] = 's3'
        # s2
        (x, y) = self.generate_corordinates()
        self.s2 = S2(self, x, y)
        self.mat[x][y]='s2'

        # s1
        (x, y) = self.generate_corordinates()
        self.s1 = S1(self, x, y)
        self.mat[x][y] = 's1'
        # w1
        (x, y) = self.generate_corordinates()
        self.w1 = W1(self, x, y)
        self.mat[x][y] = 'w1'
        # w2

        (x, y) = self.generate_corordinates()
        self.w2 = W2(self, x, y)
        self.mat[x][y] = 'w2'
        # w3

        (x, y) = self.generate_corordinates()
        self.w3 = W3(self, x, y)
        self.mat[x][y] = 'w3'
        print(self.mat)
    def show_game_over(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        print("here")
        self.draw_text(self.screen,"GAME OVER !!!",64,5-1,(HEIGHT//TILESIZE)//4)

        print("here")
        if(self.player.health<self.ai.health):
            print("here")
            self.draw_text(self.screen, "AI WON !!!",34, 6,(HEIGHT//TILESIZE)//2)
        elif(self.player.health>self.ai.health):
            print("here")
            self.draw_text(self.screen, "PLAYER WON !!!",34,6, (HEIGHT//TILESIZE)//2)
        else:
            self.draw_text(self.screen, "GAME DREW !!!",34, 6, (HEIGHT//TILESIZE)//2)
        self.draw_text(self.screen, "Press ANY KEY TO RESTART:", 34,3, (HEIGHT // TILESIZE) // 5)
        pg.display.flip()
        waiting=True
        while(waiting):
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.type==pygame.KEYDOWN:
                    g = Game()
                    g.show_start_screen()
                    while True:
                        g.new()
                        g.run()
                        g.show_go_screen()
    def damage_ret_w1(self, temp):
        if (temp == 1):
            return self.s1.damage1
        if (temp == 2):
            return self.s2.damage1
        else:
            return self.s3.damage1

    def damage_ret_w2(self, temp):
        if (temp == 1):
            return self.s1.damage2
        if (temp == 2):
            return self.s2.damage2
        else:
            return self.s3.damage2

    def damage_ret_w3(self, temp):
        if (temp == 1):
            return self.s1.damage3
        if (temp == 2):
            return self.s2.damage3
        else:
            return self.s3.damage3

    def run(self):
        pg.mixer.music.play(-1)
        self.playing=True
        game_over=False
        while self.playing:
            if(game_over):
                self.show_game_over()
                self.quit()
            self.dt=self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()
            weapons_left=self.no_weapons_left()
            if self.ai.health <= 0 or self.player.health <= 0 or weapons_left==False:
                game_over=True

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.mat[self.player.x][self.player.y] = 'p'
        self.mat[self.ai.x][self.ai.y]='a'
        grabs=pg.sprite.spritecollide(self.player,self.ww1,True)
        if(grabs):
            print("W1 yeilded by player",self.w1.damage)
            self.pw_sound.play()
            temp = self.ai.yeildeds
            self.ai.animate=True
            # col=Expolosion(self,(self.player.x,self.player.y))
            print(temp)
            if (temp != 0):
                self.ai.health-=self.damage_ret_w1(temp)
                self.ai.yeildeds=0
            else:
                self.ai.health -= self.w1.damage
            print("ai health", self.ai.health)
        grabs = pg.sprite.spritecollide(self.ai, self.ww1, True)
        if (grabs):
            print("W1 yeilded by ai", self.w1.damage)
            self.d_sound.play()
            self.player.animate=True
            temp = self.player.yeildeds
            print(temp)
            if (temp != 0):
                self.player.health -= self.damage_ret_w1(temp)
                self.player.yeildeds=0
            else:
                self.player.health -= self.w1.damage
            print("player health", self.player.health)
        grabs=pg.sprite.spritecollide(self.player,self.ww2,True)
        if (grabs):
            print("W2 yeilded by player", self.w2.damage)
            self.ai.animate=True
            self.pw_sound.play()

            temp = self.ai.yeildeds
            print(temp)
            if (temp != 0):
                self.ai.health -= self.damage_ret_w2(temp)
                self.ai.yeildeds=0
            else:
                self.ai.health -= self.w2.damage
            print("ai health", self.ai.health)
        grabs = pg.sprite.spritecollide(self.ai, self.ww2, True)
        if (grabs):
            print("W2 yeilded by ai", self.w2.damage)
            self.d_sound.play()

            self.player.animate = True
            temp = self.player.yeildeds
            print(temp)
            if (temp != 0):
                self.player.health -= self.damage_ret_w2(temp)
                self.player.yeildeds=0
            else:
                self.player.health -= self.w2.damage
            print("player health", self.player.health)
        grabs = pg.sprite.spritecollide(self.player, self.ww3, True)
        if (grabs):
            print("W3 yeilded by player", self.w3.damage)
            self.ai.animate = True
            self.pw_sound.play()
            temp = self.ai.yeildeds
            print(temp)
            if (temp != 0):
                self.ai.health -= self.damage_ret_w3(temp)
                self.ai.yeildeds=0
            else:
                self.ai.health -= self.w3.damage
            print("ai health",self.ai.health)
        grabs = pg.sprite.spritecollide(self.ai, self.ww3, True)
        if (grabs):
            print("W3 yeilded by ai", self.w3.damage)
            self.d_sound.play()

            self.player.animate = True
            temp = self.player.yeildeds
            print(temp)
            if (temp != 0):
                self.player.health -= self.damage_ret_w3(temp)
                self.player.yeildeds=0
            else:
                self.player.health -= self.w3.damage
            print("player health", self.player.health)
        grabs = pg.sprite.spritecollide(self.player, self.ss3, True)
        if (grabs):
            self.s_sound.play()
            print("S3 yeilded by player", self.s3.damage1,self.s3.damage2)
            self.player.yeildeds = 3
        grabs = pg.sprite.spritecollide(self.ai, self.ss3, True)
        if (grabs):
            print("S3 yeilded by ai", self.s3.damage1,self.s3.damage2)
            self.ai.yeildeds = 3
        grabs = pg.sprite.spritecollide(self.player, self.ss2, True)
        if (grabs):
            self.s_sound.play()
            print("S2 yeilded by player", self.s2.damage1,self.s2.damage3)
            self.player.yeildeds = 2
        grabs = pg.sprite.spritecollide(self.ai, self.ss2, True)
        if (grabs):
            print("S2 yeilded by ai", self.s2.damage1,self.s2.damage3)
            self.ai.yeildeds = 2
        grabs = pg.sprite.spritecollide(self.player, self.ss1, True)
        if (grabs):
            self.s_sound.play()
            print("S1 yeilded by player", self.s1.damage2,self.s1.damage3)
            self.player.yeildeds = 1
        grabs = pg.sprite.spritecollide(self.ai, self.ss1, True)
        if (grabs):
            print("S1 yeilded by ai", self.s1.damage2,self.s1.damage3)
            self.ai.yeildeds = 1

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen,LIGHTGRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGRAY, (0, y), (WIDTH, y))


    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen,"AI HEALTH "+str(self.ai.health),14,0,0)
        self.draw_text(self.screen, "AI SHEILD " + str(self.ai.yeildeds), 14, 0, 1)
        self.draw_text(self.screen, "PLAYER HEALTH " + str(self.player.health), 14, 13,11)
        self.draw_text(self.screen, "PLAYER SHEILD " + str(self.player.yeildeds), 14, 13,10)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if(self.player.turn==True):
                    print(self.mat)
                    self.mat[self.player.x][self.player.y]='0'
                    if event.key == pg.K_LEFT:
                        self.player.move(dx=-1)
                    if event.key == pg.K_RIGHT:
                        self.player.move(dx=1)
                    if event.key == pg.K_UP:
                        self.player.move(dy=-1)
                    if event.key == pg.K_DOWN:
                        self.player.move(dy=1)
                    self.ai.turn=True

                    continue
            if (self.ai.turn == True):
                pg.time.wait(50)
                print(self.mat)
                # temp = random.choice([0, 1, 2, 3])
                # if temp == 0:
                #     self.ai.move(dx=-1)
                # if temp == 1:
                #     self.ai.move(dx=1)
                # if temp == 2:
                #     self.ai.move(dy=-1)
                # if temp == 3:
                #     self.ai.move(dy=1)
                mat2=np.copy(self.mat)
                self.mat[self.ai.x][self.ai.y] = '0'
                player_sheild=''
                if(self.player.yeildeds==1):
                    player_sheild='s1'
                if (self.player.yeildeds == 2):
                    player_sheild = 's2'
                if (self.player.yeildeds == 3):
                    player_sheild = 's3'
                ai_coordinate=ai(mat2,player_sheild)
                print(ai_coordinate)
                self.ai.move(ai_coordinate[0]-self.ai.x,ai_coordinate[1]-self.ai.y)
                self.player.turn = True
                continue
    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()