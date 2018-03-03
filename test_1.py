import os,sys
import pygame
from pygame.locals import*

RED = (255,0,0)

class Game:
    """This is the class that handles the main initialization and creation of the game."""
    def __init__(self,width = 640,height = 480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))

    def MainLoop(self):
        """This is the main loop of the game"""
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


class Player:
    """This is the player class that the player will move around with"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def LoadSprites(self):
        """Load the sprites we need"""
        self.player = Player()
        self.player_sprite = pygame.sprite.RenderPlain((self.player))

if __name__ == "__main__":
    MainWindow = Game()
    MainWindow.MainLoop()
