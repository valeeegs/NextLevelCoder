import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_COLOR = (0,0,0)
FONT_STYLE = 'freesansbold.ttf'
FONT_SIZE = 30

def get_text(
    message, screen,
    font_size = FONT_SIZE, 
    width = SCREEN_WIDTH//2, 
    height = SCREEN_HEIGHT//2,
    font_color = FONT_COLOR
    ):

    font = pygame.font.Font(FONT_STYLE, font_size)
    text = font.render(message, True, font_color) #change color
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    screen.blit(text, text_rect) #no funciona si no le pongo esto más en la función :c