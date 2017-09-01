import pygame
from pygame.locals import *

def main():
    pygame.init()
    pygame.joystick.init()
    pygame.mouse.set_visible(0)
    pygame.display.set_caption("Prosjekt 2017")
    
def run():
    import game

if __name__ == "__main__":
    run()
