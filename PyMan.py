import pygame
import os, sys
from pygame.locals import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

class PyManMain:
    '''The Main PyMan Class - This class handles the main
    initialization and creating of the game'''

    def __init__(self, width=640, height=480):
        '''Initialize'''
        '''Initialize PyGame'''
        pygame.init()
        '''Set the window size'''
        self.width = width
        self.height = height
        '''Create the screen'''
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):
        '''This is the main loop of the game'''
        '''Load all of our sprites'''
        self.LoadSprites()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.snake_sprites.draw(self.screen)
            pygame.display.flip()

            if __name__ == '__main__':
                MainWindow = PyManMain()
                MainWindow.MainLoop()

# class Snake(pygame.sprite.Sprite):
#     '''This is our sname that will move around the screen'''
#     def __init__ (self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image, self.rect = pygame.image.load('snake.png')
#         self.pellets = 0
#
#     def LoadSprites(self):
#         '''Load the sprites that we need'''
#         self.snake = Snake()
#         self.snake_sprites = pygame.sprite.RenderPlain((self.snake))
#
# class Pellet(pygame.sprite.Sprite):
#     def __init__(self, rect=None):
#         pygame.sprite.Sprite.__init__(self)
#         self.image, self.rect = load('pellet.png, -1')
#         if rect != None:
#             self.rect = rect

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = Rect(255, 0, 40, 40)

    def LoadSprites(self):
        '''Load the sprites that we need'''
        self.rect = Player()
        self.rect_sprites = pygame.sprite.RenderPlain((self.rect))


if __name__ == "__main__":
     MyGame = PyManMain()
     MyGame.MainLoop()
     MyRect = Player()



'''CURRENT STATUS: got the window to open, wrote code
for snake but snake doesn't show up yet'''
