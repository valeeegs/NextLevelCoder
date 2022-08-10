import pygame
from dino_runner.utils.constants import RUNNING, JUMPING
from pygame.sprite import Sprite


class Dinosaour(Sprite):
    X_POS = 80
    Y_POS = 310
    JUM_VEL = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0 #para mostrar que patita se levanta 
        self.dino_run = True
        self.dino_jump = False
        self.jum_vel = self.JUM_VEL

    def update(self, user_input):#
        if self.dino_run:
            self.run() #creo que depsues se le borra xd
        elif self.dino_jump:
            self.jump()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False

        elif not self.dino_jump: 
            self.dino_jump = False
            self.dino_run = True

        if self.step_index >= 10:
            self.step_index = 0
        

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jum_vel * 4
            self.jum_vel -= 0.8

        #sin esto cae al vacio xd
        if self.jum_vel < -self.JUM_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jum_vel = self.JUM_VEL


    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
