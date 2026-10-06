#my coursework
import pygame
from pygame.examples.midi import BACKGROUNDCOLOR
import menuitems
from constants import *


#main function
class Main():
    def __init__(self):
        pygame.init()
        #main screen function game loop
        self.menuscreen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.running = True
        self.clock = pygame.time.Clock()
        #set up objects
        self.buttons = [menuitems.Button(10,10,"start"), menuitems.Button(10,70,"quit")]

    def mainloop(self):
        while self.running:
            # inputs
            self.handle_input()
            # updates
            self.updates()
            # render
            self.render()
            self.clock.tick(TARGET_FRAME_RATE)
        pygame.quit()


    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def updates(self):
        pass

    def render(self):
        self.menuscreen.fill(BACKGROUNDCOLOR)
        for button in self.buttons:
            button.draw(self.menuscreen)
        pygame.display.flip()

main = Main()
main.mainloop()
