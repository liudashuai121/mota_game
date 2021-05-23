import pygame


#Define and initialize equipment
class equipment(object):
    def __init__(self,name,money,level,attack,critical,dodge,image,s):
        self.name=name
        self.money=money
        self.attack=attack
        self.level=level
        self.critical=critical
        self.doge=dodge
        self.img = pygame.image.load('images/%s.jpg' % image)
        self.image = str(image)
        self.s=s

    def addtobag(self, me, changex, changey):
        me.myy += changey * 32
        me.myx += changex * 32
        me.y += changey
        me.x += changex
        me.bag.append(self)

# Achieving equipment weapons
    def use(self, me, number):
        del me.bag[number]
        me.att += self.attack
        me.critical += self.critical
        me.dodge +=self.doge


#Define and initialize consumables
class consumables(object):
    def __init__(self,name,hp,mp,attack,image,s):
        self.name=name
        self.hp=hp
        self.mp=mp
        self.attack=attack
        self.img = pygame.image.load('images/%s.jpg' % image)
        self.image = str(image)
        self.s=s
#Put in the backpack
    def addtobag(self,me,changex,changey):
        me.myy += changey * 32
        me.myx += changex * 32
        me.y += changey
        me.x += changex
        me.bag.append(self)

#Use consumables
    def use(self,me,number):
        del me.bag[number]
        me.hp+=self.hp
        me.mp += self.mp
        me.att += self.attack
