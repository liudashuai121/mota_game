import pygame
from Mmap import guailist,consumableslist,equipmentlist
from Mmap import map

from bag import drawshop

isshop=0
#Initialize my state
class Me(object):
    def __init__(self):
        self.me = pygame.Rect(160,320,30,30)
        self.meimg = [
            pygame.image.load('images/player_1.jpg'),
            pygame.image.load('images/player_2.jpg'),
            pygame.image.load('images/player_3.jpg'),
            pygame.image.load('images/player_4.jpg')
        ]
        #Pixel coordinates
        self.myx = 160
        self.myy = 288
        self.myd = 4   #0:Up 1:Right 2:Douw 3:Left
        #The coordinates of the character in the image array
        self.y = 9
        self.x = 5
        self.floor = 5 #floor

        #my status
        self.level = 1 #LV
        self.money = 0  #Gold
        self.jingyan = 0 #Experience
        self.hp = 500  #helth point
        self.mp = 100 # magic point
        self.dodge=10 # Chance of dodge (%)
        self.critical=10 # Chance of critical hit (%)
        self.att = 10000  #Attack power
        self.fang = 10  #Defensive power
        self.bag=[ ]
        #my  sucess
        self.num_kill =  0 #the num of monster killed
        self.num_daoju = 0  # the num of consumables used
#Update my status
    def updateMe(self,map,screen):
        self.map = map
        if self.myd == 0 :
          if self.y > 0:
               next = self.map[self.y-1][self.x]  #The element at the next position in the array map (data type: int)
               changex = 0
               changey = -1
               self.move(next, changex, changey,screen)
          else:
              next = 0
        elif self.myd == 1:
            if self.x < 10:
                next = self.map[self.y][self.x + 1]
                changex = 1
                changey = 0
                self.move(next, changex, changey, screen)
            else:
                next = 0
        elif self.myd == 2:
            if self.y < 10:
                next = self.map[self.y + 1][self.x]
                changex = 0
                changey = 1
                self.move(next, changex, changey, screen)
            else:
                next = 0

        elif self.myd == 3:
            if self.x > 0:
                    next = self.map[self.y][self.x-1]
                    changex = -1
                    changey = 0
                    self.move(next, changex, changey, screen)
            else:
                    next = 0
        else :
            pass
        self.myd = 4


        return self.map
#Enter the next room or return to the upper room to define my location
    def choosef(self,f,down=False):
      if not down :
        if f == 1 :
            self.myx = 160
            self.myy = 320
            self.y = 10
            self.x = 5

        elif f == 2 :
            self.x = 5
            self.y = 9
            self.myx = 160
            self.myy = 288

        elif f == 3:
            self.x = 0
            self.y = 1
            self.myx = 0
            self.myy = 32
        elif f == 4:
            self.x = 1
            self.y = 10
            self.myx = 32
            self.myy = 320


      else:
          if f == 1:
              self.myx = 160
              self.myy = 32
              self.y = 1
              self.x = 5

          elif f == 2:
              self.x = 5
              self.y = 9
              self.myx = 160
              self.myy = 288
          elif f == 3:
              self.x = 0
              self.y = 9
              self.myx = 0
              self.myy = 288

    def move(self,next,changex,changey,screen):
        if next == 509:# floor
                self.myy += changey*32
                self.myx += changex*32
                self.y += changey
                self.x += changex
        elif next == 507:#Upward stairs
            self.floor += 1
            self.choosef(self.floor)
            self.map = list(map[self.floor])
        elif next == 508:#Down stairs
            self.floor -= 1
            self.choosef(self.floor,True)
            self.map = list(map[self.floor])
        elif (next>=0) and (next < 33):#Monster

            self.money,self.jingyan = guailist[next].attack(self,screen,changex,changey)
            self.map[self.y][self.x] = 509

            if self.jingyan > 100 :
                self.level += 1  # lv
                self.jingyan = 0  # exp
                self.hp += 50  # hp
                self.mp += 50  # mp
                self.dodge += 1  # Chance of dodge
                self.critical += 1  # Chance of critical hit
                self.att += 5  # attack
                self.fang += 5  # denfence


        elif (next>=300) and (next < 310):#item
            consumableslist[next-300].addtobag(self,changex,changey)
            self.map[self.y][self.x] = 509
        elif (next >= 310) and (next < 400):
            equipmentlist[next - 310].addtobag(self, changex, changey)
            self.map[self.y][self.x] = 509
        elif next==200:
            font = pygame.font.SysFont("SimHei", 40)
            font1 = pygame.font.SysFont("SimHei", 30)
            pygame.draw.rect(screen, (220, 220, 220), (0, 0, 352, 522))
            screen.blit(font.render('Warrior！go on!', 1, (51, 161, 201)), (32, 70))
            screen.blit(font1.render('Defeat the monster！', 1, (51, 161, 201)), (32,150))
            screen.blit(font1.render('Pass all the rooms！', 1, (51, 161, 201)), (32, 200))
            pygame.display.update()
            pygame.time.wait(2000)

        elif next==202:
            font = pygame.font.SysFont("SimHei", 60)
            pygame.draw.rect(screen, (220, 220, 220), (0, 0, 352, 522))
            screen.blit(font.render('go on！', 1, (51, 161, 201)), (85, 90))
            pygame.display.update()
            pygame.time.wait(2000)
        elif next==201:
            font = pygame.font.SysFont("SimHei", 60)
            pygame.draw.rect(screen, (220, 220, 220), (0, 0, 352, 522))
            screen.blit(font.render('go on！', 1, (51, 161, 201)), (85, 90))
            pygame.display.update()
            pygame.time.wait(2000)
        elif next==204:
            font = pygame.font.SysFont("SimHei", 30)
            pygame.draw.rect(screen, (220, 220, 220), (0, 0, 352, 522))
            screen.blit(font.render('Thank you mario! ', 1, (51, 161, 201)), (32,150))
            screen.blit(font.render('But our princess is in another castle! ', 1, (51, 161, 201)), (32, 200))
            pygame.display.update()
            pygame.time.wait(2000)






