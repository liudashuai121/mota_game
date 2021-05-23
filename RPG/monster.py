import pygame
import sys
from time import sleep
import time
import random
ADDENEMY = pygame.USEREVENT +1
#Monster definition and initialization
class monster(object):
    def __init__(self,name,life,att,fang,money,jingyan,image):
        self.name = name
        self.hp = life
        self.att = att
        self.fang = fang
        self.money = money
        self.jingyan = jingyan
        self.img = pygame.image.load('images/%s.jpg' % image)
        self.image = str(image)

#Define battle and its screens
    def attack(self,me,screen,changex,changey):
        img1 = pygame.image.load('images/player_2.jpg')
        img2 = pygame.image.load('images/%s.jpg' % self.image)
        font = pygame.font.SysFont("SimHei", 22)
        font1 = pygame.font.SysFont("SimHei", 35)
        hp=self.hp

        while True :
            pygame.draw.rect(screen, (220, 220, 220), (0, 0, 352, 522))
            #My status
            screen.blit(img1, (20, 170))
            screen.blit(font.render('HP:' + str(me.hp), 1, (253, 0, 0)), (20, 90))
            screen.blit(font.render('ATTACK:' + str(me.att), 1, (253, 177, 6)), (20, 115))
            screen.blit(font.render('Defense:' + str(me.fang), 1, (253, 177, 6)), (20, 140))
            #Monster status
            screen.blit(img2, (240, 170))
            screen.blit(font.render(str(self.name), 1, (253, 0, 0)), (140, 60))
            screen.blit(font.render('HP:' + str(hp), 1, (253, 0, 0)), (240, 90))
            screen.blit(font.render('ATTACK:' + str(self.att), 1, (253, 177, 6)), (240, 115))
            screen.blit(font.render('Defense:' + str(self.fang), 1, (253, 177, 6)), (240, 140))
            #My actions
            screen.blit(font.render('Action', 1, (253, 177, 6)), (15, 220))
            screen.blit(font.render('a.attack', 1, (253, 177, 6)), (45, 240))
            screen.blit(font.render('s.spell', 1, (253, 177, 6)), (45, 260))
            screen.blit(font.render('p.parry', 1, (253, 177, 6)), (190, 240))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == ord('a'):
                        if random.random()>(me.critical/100):
                            a=me.att
                            screen.blit(font.render('HP-' + str(a - self.fang), 1, (253, 0, 0)), (275, 190))
                        else:
                            a=me.att*2
                            screen.blit(font.render('HP-' + str(a - self.fang), 1, (253, 0, 0)), (275, 190))
                            screen.blit(font1.render('CRIT', 1, (253, 177, 6)), (130, 170))

                        hp -= a - self.fang

                        pygame.display.update()
                        time.sleep(0.6)

                        me.hp -= self.att - me.fang
                        screen.blit(font.render('HP-' + str(a - me.fang), 1, (253, 0, 0)), (55, 190))
                    if event.key == ord('s'):
                        if me.mp > 50 :
                            screen.blit(font1.render('SPELL', 1, (253, 177, 6)), (130, 170))
                            hp -= me.att * 2 - self.fang
                            screen.blit(font.render('HP-'+str(me.att * 2 - self.fang), 1, (253, 0, 0)), (240, 70))
                            pygame.display.update()
                            time.sleep(0.6)

                            me.mp-=50
                            me.hp -= self.att - me.fang
                            screen.blit(font.render('HP-'+str(self.att - me.fang), 1, (253, 0, 0)), (20, 70))
                        else:
                            screen.blit(font.render('MP is not enough', 1, (253, 177, 6)), (80, 170))
                        pygame.display.update()
                    if event.key == ord('p'):
                        screen.blit(font1.render('parry', 1, (253, 177, 6)), (130, 170))
                        hp -= int((me.att - self.fang)*0.7)
                        me.hp -= int((self.att - me.fang)*0.5)
                        pygame.display.update()
            if me.hp < 1:
                font2 = pygame.font.SysFont("SimHei", 45)
                pygame.draw.rect(screen, (225, 0, 0), (0, 0, 352, 522))
                screen.blit(font2.render('You Die,Game Over！', 1, (51, 161, 201)), (35, 90))
                pygame.display.update()
                pygame.time.wait(2000)
                pygame.quit()
            else:
                if hp < 1:
                    font2 = pygame.font.SysFont("SimHei", 30)
                    me.myy += changey * 32
                    me.myx += changex * 32
                    me.y += changey
                    me.x += changex
                    me.jingyan += self.jingyan
                    me.money += self.money
                    me.num_kill+=1
                    pygame.draw.rect(screen, (220, 220, 220), (0, 0, 352, 522))
                    if me.num_kill==3:
                        pygame.draw.rect(screen, (220, 220, 220), (0, 0, 352, 522))
                        screen.blit(font2.render('Get Honor MonsterKiller', 1, (51, 161, 201)), (10, 200))
                    screen.blit(font2.render('get EX '+  str(self.jingyan)+'  Gold'+ str(self.money), 1, (51, 161, 201)), (65, 135))
                    pygame.display.update()
                    pygame.time.wait(2000)
                    return me.money, me.jingyan
                elif hp < 0:
                    hp = 0
                    pygame.display.update()
                    pygame.time.wait(500)
                else:
                    pygame.display.update()
                    pygame.time.wait(500)
            pygame.display.update()


