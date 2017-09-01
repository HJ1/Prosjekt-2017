import pygame
from pygame.locals import *
from color_palette import *
pygame.init()

#Screen Variables With Values
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

def main():
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    screen.fill(GRAY2)
    pygame.mouse.set_visible(0)
    pygame.display.set_caption("Prosjekt 2017")
    pygame.display.flip()
    
if __name__=="__main__":
    main()
    
    




