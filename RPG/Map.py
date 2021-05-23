import pygame
#Draw a map
#The size of each image grid
awidth = 32
aheight = 32

#Load the image of the map and print
def load(map,screen,me):
        x = 0
        y = 0
        for i in map:
            for one in i :
                img = pygame.image.load('images/%s.jpg' % str(one))
                screen.blit(img,(y*32,x*32))
                y += 1
            y = 0
            x += 1

        img = pygame.image.load('images/990.jpg')
        for i in range(6):
            for one in range(11):
                screen.blit(img, (352+i*32,one*32))

        img = pygame.image.load('images/991.jpg')
        for i in range(6):
            for one in range(11):
                screen.blit(img, (544+i*32,one*32))

        ##Load the Status of character
        font = pygame.font.SysFont("SimHei", 16)
        font1 = pygame.font.SysFont("SimHei", 24)
        y = 0
        text = str(me.floor)+'FLOOR'
        surf = font.render(text, 1, (255, 255, 255))
        screen.blit(surf, (362, 20+y*30))

        y += 1
        text = 'Your Status '
        surf = font1.render(text, 1, (25, 25, 155))
        screen.blit(surf, (362, 20 + y * 30-5))

        y += 1
        text = 'LV：'+str(me.level)+'   EXP  '+str(me.jingyan)+'/100'
        surf = font.render(text, 1, (255, 255, 255))
        screen.blit(surf,(362,20+y*30))

        y += 1
        text = 'HP：' + str(me.hp)
        surf = font.render(text, 1, (255, 255, 255))
        screen.blit(surf, (362, 20 + y * 30))

        y += 1
        text = 'ATTACK：' + str(me.att)
        surf = font.render(text, 1, (255, 255, 255))
        screen.blit(surf, (362, 20 + y * 30))

        y += 1
        text = 'DEFENCE：' + str(me.fang)
        surf = font.render(text, 1, (255, 255, 255))
        screen.blit(surf, (362, 20 + y * 30))

        y += 1
        text = 'GOLD：' + str(me.money)
        surf = font.render(text, 1, (255, 255, 255))
        screen.blit(surf, (362, 20 + y * 30))

        y += 1
        text = 'MP：' + str(me.mp)
        surf = font.render(text, 1, (255, 255, 255))
        screen.blit(surf, (362, 20 + y * 30))
        y += 1
        text = 'DODGE：' + str(me.dodge)+'%'
        surf = font.render(text, 1, (255, 255, 255))
        screen.blit(surf, (362, 20 + y * 30))
        y += 1
        text = 'CRITICAL：' + str(me.critical)+'%'
        surf = font.render(text, 1, (255, 255, 255))
        screen.blit(surf, (362, 20 + y * 30))
        y += 1
        text = 'O:Open bag  P:Close bag'
        surf = font.render(text, 1, (255, 255, 255))
        screen.blit(surf, (362, 20 + y * 30))


       #table of sucess
        font1 = pygame.font.SysFont("SimHei", 20)
        font2 = pygame.font.SysFont("SimHei", 30)
        y = 0
        text = 'HONNOR Table'
        surf = font2.render(text, 1, (0, 49, 237))
        screen.blit(surf, (554, 20 + y * 45))


        y += 1
        if me.num_kill>2:
                text = 'Monster Killer'
        else:
                text =  'Kill point: '  +str(me.num_kill)
        surf = font1.render(text, 1, (255, 255, 255))
        screen.blit(surf, (554, 30 + y * 45))

        y += 1
        if me.num_daoju>2:
                text = 'ConsumablesMaster'
        else:
                text =  'Consumables used:'  +str(me.num_daoju)
        surf = font1.render(text, 1, (255, 255, 255))
        screen.blit(surf, (554, 30 + y * 45))

        y += 1
        if me.floor>2:
                text = 'Explorer'
        else:
                text = 'Reached: '+str(me.floor)+ 'floor'
        surf = font1.render(text, 1, (255, 255, 255))
        screen.blit(surf, (554, 30 + y * 45))

        y += 1
        text = 'Move By'
        surf = font1.render(text, 1, (255, 255, 255))
        screen.blit(surf, (554, 30 + y * 45))

        y += 1
        text = '   ↑'
        surf = font2.render(text, 1, (255, 255, 255))
        screen.blit(surf, (567, 30 + y * 45))

        y += 1
        text = '  ←↓→'
        surf = font2.render(text, 1, (255, 255, 255))
        screen.blit(surf, (554, 30 + y * 45))