from Map import *       #Package for drawing a map
import pygame
import sys
from Mmap import *    #Load map
from me import  *     #Load characters
import bag              #Loading backpack
from bag import *  #Load backpack map
import copy
import numpy as np
import os

if __name__ == '__main__':


    #Initialize the game window
    screen = pygame.display.set_mode((736,352))
    pygame.display.set_caption('RPG')
    #Generate game characters
    me = Me()
    # Initialization data
    lastimg = 0
    n= 0
    isbag = 0
    pygame.init()
    #Map loading and backup
    #m = list(map[me.floor])
    m = list(map[me.floor])
    ms = copy.deepcopy(list(map[me.floor]))
    mbag = bagmap #Backpack map
    mshop= bagmap
    pygame.font.init()

    #Initialize font
    font = pygame.font.SysFont("SimHei", 25)
    #Responding to keyboard events
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    me.myd = 0
                    lastimg = 0
                elif event.key == pygame.K_RIGHT:
                    me.myd = 1
                    lastimg = 3
                elif event.key == pygame.K_DOWN:
                    me.myd = 2
                    lastimg = 1
                elif event.key == pygame.K_LEFT:
                    me.myd = 3
                    lastimg = 2
                elif event.key == ord('o'):   #Open the bag
                    isbag=1
                elif event.key == ord('p'):   # Close the bag
                    isbag=0
                elif event.key == ord('s'):  # save the game
                    font = pygame.font.SysFont("SimHei", 40)
                    font1 = pygame.font.SysFont("SimHei", 20)
                    pygame.draw.rect(screen, (220, 220, 220), (0, 0, 352, 522))
                    screen.blit(font.render('Successful save', 1, (51, 161, 201)), (32, 70))
                    screen.blit(font1.render('The next time you start ', 1, (51, 161, 201)), (32,150))
                    screen.blit(font1.render('the game from the archive', 1, (51, 161, 201)), (32, 200))
                    pygame.display.update()
                    pygame.time.wait(3000)
                    np.save('map.npy', map)
                elif 49<= int(event.key) <= 57 :  # Use of  items in bag
                    num=(int(event.key)-48)
                    if(len(me.bag)>=num and isbag==1):
                        refresh(mbag, screen, me,num)
                else:
                    me.myd = 4
        if isbag==1:
            bag.drawbag(mbag,screen,me)
        #elif isshop==1:
           # print("s")
        else:
            m = me.updateMe(m,screen) #
            load(m, screen, me)
            screen.blit(me.meimg[lastimg], (me.myx, me.myy))
        pygame.display.update()


