import os,sys
import pygame
import math
from pygame.locals import*
import numpy as np
import random

class Game():
    """This is the class that handles the main initialization and creation of the game."""
    def __init__(self,width = 1024,height = 760):
        pygame.init()
        self.width = width
        self.height = height
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)
        self.background_surf = pygame.image.load("haunted-houses.png")
        self.rect = self.background_surf.get_rect()
        # self.cropx,self.cropy = 1400,788
        # self.cropRect = (self.cropx, self.cropy, self.rect.width,self.rect.height)

        self.player1 = Player(980,random.randint(0,786))
        #self.player1 = Player(200,300) #this is for helping us debug
        self.zombie1 = Zombie(random.randint(0,970),random.randint(0,786))
        self.zombie2 = Zombie(random.randint(0,970),random.randint(0,786))
        self.zombie3 = Zombie(random.randint(0,970),random.randint(0,786))
        self.zombie4 = Zombie(random.randint(0,970),random.randint(0,786))
        self.safezone = SafeZone()

    def win(self):
        pygame.mixer.init()
        pygame.mixer.music.load('victory.ogg')
        pygame.mixer.music.play()
        while 1:
             self.screen.blit(self.background_surf,(0,0))
             pygame.font.init()
             myfont = pygame.font.SysFont('arial', 40)
             textsurface = myfont.render('YOU WIN!', False, (50, 255, 50))
             self.screen.blit(textsurface, (200, 600))
             pygame.display.flip()
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     sys.exit()

    def MainLoop(self):
        """This is the main loop of the game"""
        count = 0
        while 1:
            self.refresh()
            count +=1
            if count % 7 == 0:
                self.zombie1.move_zombie(self.player1,4)
                self.zombie2.move_zombie(self.player1,3)
                self.zombie3.move_zombie(self.player1,3)
                self.zombie4.move_zombie(self.player1,4)
                if self.detect_collision(self.player1,self.zombie1,self.player1.loc,self.zombie1.loc):
                    zombies = Game()
                    pygame.mixer.init()
                    pygame.mixer.music.load('raze_music.ogg')
                    pygame.mixer.music.play()
                    zombies.MainLoop()
                if self.detect_collision(self.player1,self.zombie2,self.player1.loc,self.zombie2.loc):
                    zombies = Game()
                    pygame.mixer.init()
                    pygame.mixer.music.load('raze_music.ogg')
                    pygame.mixer.music.play()
                    zombies.MainLoop()
                if self.detect_collision(self.player1,self.zombie3,self.player1.loc,self.zombie3.loc):
                    zombies = Game()
                    pygame.mixer.init()
                    pygame.mixer.music.load('raze_music.ogg')
                    pygame.mixer.music.play()
                    zombies.MainLoop()
                if self.detect_collision(self.player1,self.zombie4,self.player1.loc,self.zombie4.loc):
                    zombies = Game()
                    pygame.mixer.init()
                    pygame.mixer.music.load('raze_music.ogg')
                    pygame.mixer.music.play()
                    zombies.MainLoop()
                if self.detect_collision(self.player1, self.safezone, self.player1.loc, self.safezone.loc):
                    zombies = Game()
                    zombies.win()

            for event in pygame.event.get():
                self.player1.move_player(event, 5)

                if event.type == pygame.QUIT:
                    sys.exit()

    def refresh(self):
        self.screen.blit(self.background_surf,(0,0))
        self.screen.blit(self.player1.surf,(self.player1.loc[0],self.player1.loc[1]))
        self.screen.blit(self.zombie1.surf,(self.zombie1.loc[0],self.zombie1.loc[1]))
        self.screen.blit(self.zombie2.surf,(self.zombie2.loc[0],self.zombie2.loc[1]))
        self.screen.blit(self.zombie3.surf,(self.zombie3.loc[0],self.zombie3.loc[1]))
        self.screen.blit(self.zombie4.surf,(self.zombie4.loc[0],self.zombie4.loc[1]))
        self.screen.blit(self.safezone.surf, (self.safezone.loc[0], self.safezone.loc[1]))
        pygame.display.flip()

    def detect_collision(self,rect1,rect2,loc1,loc2):
        rect1_center_x = loc1[0] + (rect1.xsize)/2
        rect2_center_x = loc2[0] + (rect2.xsize)/2

        rect1_center_y = loc1[1] + (rect1.ysize)/2
        rect2_center_y = loc2[1] + (rect2.ysize)/2

        if abs(rect2_center_x - rect1_center_x) <= (rect1.xsize)/2 + (rect2.xsize)/2:
            if abs(rect2_center_y - rect1_center_y) <= (rect1.ysize)/2 + (rect2.ysize)/2:
                #print(rect1_center_x)
                print("Collision detected!")
                return True

class Player():
    """This is the player class that the player will move around as"""
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.xsize = 40
        self.ysize = 40
        self.surf = pygame.image.load("char.jpg")
        self.surf = pygame.transform.scale(self.surf,(40,40))
        # self.color = 255,0,0
        # self.surf.fill(self.color)
        self.loc = np.array([x, y])
        # self.xloc = self.loc[0]
        # self.yloc = self.loc[1]
        self.rect = pygame.Rect(self.loc[0], self.loc[1], self.xsize, self.ysize)
        self.rect.width = 0

    def draw_player(self):
        self.drawing = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)

    def move_player(self, event, n):
        if event.type == KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w]:
                self.loc[1] -= n
            elif pressed[pygame.K_s]:
                self.loc[1] += n
            elif pressed[pygame.K_a]:
                self.loc[0] -= n
            elif pressed[pygame.K_d]:
                self.loc[0] += n

class Zombie():
    """This is the zombie class that will chase the player around on the screen"""
    def __init__(self,xloc,yloc):
        pygame.sprite.Sprite.__init__(self)
        self.xsize = 40
        self.ysize = 40
        self.surf = pygame.Surface((self.xsize,self.ysize))
        # self.color = 0,255,0
        # self.surf.fill(self.color)
        self.surf = pygame.image.load("zombie3.png")
        self.surf = pygame.transform.scale(self.surf,(40,40))
        self.rect = self.surf.get_rect()
        self.loc = np.array([xloc,yloc])

        self.rect = pygame.Rect(self.loc[0], self.loc[1], self.xsize, self.ysize)
        self.rect.width = 0

    def draw_zombie(self):
        self.drawing = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)

    def move_zombie(self,player,r):
        """This moves the zombie towards the player specified by r pixels"""

        m = player.loc - self.loc

        # if type(m[0]) != np.float64:
        #     m[0] = 0
        # if type(m[1]) != np.float64:
        #     m[1] = 0

        if m[0] != np.float64(0) or m[1] != np.float64(0):
            #print(m)
            m_unit = m/np.linalg.norm(m)
        else:
            m_unit = np.array([0,0])

        m_now = r*m_unit


        move_x = m_now[0]
        move_y = m_now[1]
        self.loc[0] += int(m_now[0])
        self.loc[1] += int(m_now[1])

class SafeZone():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.xsize = 40
        self.ysize = 40
        self.surf = pygame.Surface((50,50))
        self.color = 100,250,100
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect()
        self.loc = np.array([200, 580])

        self.rect = pygame.Rect(self.loc[0], self.loc[1], self.xsize, self.ysize)
        self.rect.width = 0

if __name__ == "__main__":
#This is the part of the code that where I"m just trying to display a rectangle and I'm not getting anything
    zombies = Game()
    pygame.mixer.init()
    pygame.mixer.music.load('raze_music.ogg')
    pygame.mixer.music.play()
    zombies.MainLoop()
