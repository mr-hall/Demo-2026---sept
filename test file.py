#my coursework
import pygame
from constants import *
running = True

#main function
def main():
    global running
    #main screen function game loop
    menuscreen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while running:
        # inputs
        input()
        # updates
        updates()
        # render
        render()
        pass

def input():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



def updates():
    pass

def render():
    pass

main()
