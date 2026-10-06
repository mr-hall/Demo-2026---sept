#my coursework
import pygame
from pygame.examples.midi import BACKGROUNDCOLOR
import menuitems
from constants import *


#main function
def main():
    pygame.init()
    #main screen function game loop
    menuscreen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    #set up objects
    buttons = [menuitems.Button(10,10,"start"), menuitems.Button(10,70,"quit")]

    while running:
        # inputs
        running = input()
        # updates
        updates()
        # render
        render(menuscreen, buttons)
        clock.tick(TARGET_FRAME_RATE)
    pygame.quit()


def input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def updates():
    pass

def render(screen, buttons ):
    screen.fill(BACKGROUNDCOLOR)
    for button in buttons:
        button.draw(screen)
    pygame.display.flip()

main()
