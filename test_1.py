import os,sys
import pygame
import math
from pygame.locals import*

class Game():
    """This is the class that handles the main initialization and creation of the game."""
    def __init__(self,width = 800,height = 800):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.background_surf = pygame.Surface((self.width, self.height))
        self.color = (145, 168, 168)
        self.background_surf.fill(self.color)
        # self.rect = pygame.Rect(0, 0, self.width, self.height)
        #self.background = pygame.draw.rect(self.background_surf,self.color,self.rect, 0) #not actually sure what this does...
        self.player1 = Player()
        self.zombie1 = Zombie()
        #self.event_list = [] #may implement later

    def MainLoop(self):
        """This is the main loop of the game"""

        while 1:
            self.refresh()

            for event in pygame.event.get():
                self.player1.move_player(event)
                self.zombie1.move_zombie(self.player1,3)
                if event.type == pygame.QUIT:
                    sys.exit()

    def refresh(self):
        self.screen.blit(self.background_surf,(0,0))
        self.screen.blit(self.player1.surf,(self.player1.xloc,self.player1.yloc))
        self.screen.blit(self.zombie1.surf,(self.zombie1.xloc,self.zombie1.yloc))
        pygame.display.flip()

    #def update(self):
        #possibly implement later to control movement of player and zombies




class Player():
    """This is the player class that the player will move around as"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.xsize = 40
        self.ysize = 40
        self.surf = pygame.Surface((self.xsize,self.ysize))
        self.color = 255,0,0
        self.surf.fill(self.color)
        self.xloc = 300
        self.yloc = 300
        self.rect = pygame.Rect(self.xloc, self.yloc, self.xsize, self.ysize)
        self.rect.width = 0

    def draw_player(self):
        self.drawing = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)

    def move_player(self, event):
        if event.type == KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w]:
                self.yloc -= 3
            elif pressed[pygame.K_s]:
                self.yloc += 3
            elif pressed[pygame.K_a]:
                self.xloc -= 3
            elif pressed[pygame.K_d]:
                self.xloc += 3
class Zombie():
    """This is the zombie class that will chase the player around on the screen"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.xsize = 40
        self.ysize = 40
        self.surf = pygame.Surface((self.xsize,self.ysize))
        self.color = 0,255,0
        self.surf.fill(self.color)
        self.xloc = 100
        self.yloc = 100
        self.rect = pygame.Rect(self.xloc, self.yloc, self.xsize, self.ysize)
        self.rect.width = 0

    def draw_zombie(self):
        self.drawing = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)

    def move_zombie(self,player,r):
        """This moves the zombie towards the player specified by r pixels"""
        p_x = player.xloc
        p_y = player.yloc
        z_x = self.xloc
        z_y = self.yloc

        m = (p_y - z_y)/(p_x - z_x)
        print("y",p_y - z_y)
        print("x",p_x - z_x)
        print("slope",m)

        move_x = r/math.sqrt(1+m**2)
        print("move_x",move_x)
        move_y = m * move_x
        print("move_y",move_y)
        self.xloc += move_x
        self.yloc += move_y

    #def LoadSprites(self):
    #    """Load the sprites we need"""
    #    self.player = Player()
    #    self.player_sprite = pygame.sprite.RenderPlain((self.player))

if __name__ == "__main__":
#This is the part of the code that where I"m just trying to display a rectangle and I'm not getting anything
    zombies = Game()
    zombies.MainLoop()

# pygame.display.set_caption("hello")
# RED = 255,0,0
# screen.fill(RED)
# #
# background = pygame.Surface(screen.get_size())
# background = background.convert()
# background.fill((250,250,250))
# screen.blit(background,(0,0))
# pygame.display.flip()
# #
# mysurf = pygame.Surface((40,40))
# myrect = pygame.Rect(100,100, 100, 100)
# mysurf.fill(RED)
# width = 0
# drawing = pygame.draw.rect(mysurf,RED,myrect,width)
# screen.blit(mysurf,(100,100))
# pygame.display.flip()
#
#     while 1:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
