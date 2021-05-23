import pygame
from Map import *
import time
#Initial backpack map
bagmap=[
    [991, 991, 991, 991, 991, 991, 991, 991, 991, 991, 991],
    [991, 991, 991, 991, 991, 991, 991, 991, 991, 991, 991],
    [991, 991, 991, 991, 991, 991, 991, 991, 991, 991, 991],
    [991, 701, 702, 703, 704, 705, 706, 707, 708, 709, 991],
    [991, 509, 509, 509, 509, 509, 509, 509, 509, 509, 991],
    [991, 509, 509, 509, 509, 509, 509, 509, 509, 509, 991],
    [991, 509, 509, 509, 509, 509, 509, 509, 509, 509, 991],
    [991, 509, 509, 509, 509, 509, 509, 509, 509, 509, 991],
    [991, 991, 991, 991, 991, 991, 991, 991, 991, 991, 991],
    [991, 991, 991, 991, 991, 991, 991, 991, 991, 991, 991],
    [991, 991, 991, 991, 991, 991, 991, 991, 991, 991, 991],
]
#Items printed in your backpack
def openbag(map,me):
    m=map
    for i in range(len(me.bag)):
        m[4][1+i]=(me.bag[i]).image
    return m
#Print backpack
def drawbag(mbag,screen,me):
    mbag = openbag(mbag, me)  # Returns a map loaded with the contents of the backpack (data type: two-dimensional array)
    load(mbag, screen, me)
    font = pygame.font.SysFont("SimHei", 25)
    screen.blit(font.render('Press the number to use', 1, (0, 0, 0)), (32, 40))

#Use items in your backpack
def refresh(mbag,screen,me,num):
    font = pygame.font.SysFont("SimHei", 25)
    me.num_daoju += 1
    s = me.bag[num-1].s
    drawbag(mbag, screen, me)
    me.bag[num-1].use(me, num-1)
    for i in range(9):
        mbag[4][i + 1] = 509
    drawbag(mbag, screen, me)
    screen.blit(font.render(s, 1, (0, 0, 0)), (128, 200))
    if me.num_daoju==3:
        screen.blit(font.render('Get ConsumablesMaster', 1, (0, 0, 0)), (45, 150))
    pygame.display.update()
    time.sleep(1.2)



def drawshop(mshop,screen,me,num):
    for i in range(len(me.bag)):
        mshop[4][1 + i] = (me.bag[i]).image
    load(mshop, screen, me)


