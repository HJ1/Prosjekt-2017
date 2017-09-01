import pygame, sys
from pygame.locals import *
from color_palette import *

import main
main.main()

#Controller
try:
    j = pygame.joystick.Joystick(0)
    j.init()
    print 'Enabled joystick: ' + j.get_name()
except:
    pass

#Values and variables
screen = pygame.display.set_mode((800, 800))
screen.fill(GRAY2)
clock = pygame.time.Clock()

#Make a loop
running = True

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Keyboard
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False, sys.exit()
                
        #Controller
        if event.type == pygame.JOYBUTTONDOWN:
                print event
        elif event.type == pygame.JOYBUTTONUP:
                print event
        if event.type == pygame.JOYBUTTONDOWN and event.button == 7:
                print "A BUTTON"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 6:
                print "B BUTTON"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 4:
                print "START BUTTON"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 13:
                print "L BUTTON"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 12:
                print "R BUTTON"
                running = False
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 5:
                print "Z BUTTON"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 11:
                print "C BUTTON UP"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 10:
                print "C BUTTON DOWN"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 9:
                print "C BUTTON LEFT"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 8:
                print "C BUTTON RIGHT"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 3:
                print "DPAD UP"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 2:
                print "DPAD DOWN"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 1:
                print "DPAD LEFT"
        elif event.type == pygame.JOYBUTTONDOWN and event.button == 0:
                print "DPAD RIGHT"

    pygame.display.update()
