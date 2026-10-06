from constants import *
import pygame

class Button:
    def __init__(self,x,y,text):
        self.x = x
        self.y = y
        self.text = text
        font = pygame.font.Font("freesansbold.ttf",20)
        self.text_image = font.render(self.text,True,"black")
        self.w = BUTTON_WIDTH
        self.h = BUTTON_HEIGHT
        self.colour = BUTTON_COLOUR

    def draw(self, screen):
        pygame.draw.rect(screen,self.colour,(self.x,self.y,self.w,self.h))
        screen.blit(self.text_image, (self.x, self.y))

    def click(self):
        pass

    def hover(self):
        pass

if __name__ == "__main__":
    #tests
    b = Button(20,20,"hello")