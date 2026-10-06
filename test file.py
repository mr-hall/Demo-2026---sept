#my coursework
import pygame
from pygame.examples.midi import BACKGROUNDCOLOR

from constants import *


#main function
def main():
    pygame.init()
    #main screen function game loop
    menuscreen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    while running:
        # inputs
        running = input()
        # updates
        updates()
        # render
        render(menuscreen)
        clock.tick(TARGET_FRAME_RATE)
    pygame.quit()


def input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def updates():
    pass

def render(screen):
    screen.fill(BACKGROUNDCOLOR)
    pygame.display.flip()

main()
