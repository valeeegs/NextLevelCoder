from unittest.mock import DEFAULT
import pygame
from dino_runner.utils.constants import DUCKING, DUCKING_HAMMER, HAMMER_TYPE, JUMPING_HAMMER, RUNNING, JUMPING, RUNNING_HAMMER, RUNNING_SHIELD, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD
from pygame.sprite import Sprite
from dino_runner.components.get_text import get_text

RUN_IMG = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
JUMP_IMG = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
DUCK_IMG = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}

class Dinosaour(Sprite):
    X_POS = 80
    Y_POS = 310
    JUM_VEL = 8.5
    Y_POS_DUCKING = 340

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0 #para mostrar que patita se levanta 
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.jum_vel = self.JUM_VEL
        self.setup_state()
       
    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.power_up_time_up = 0
        self.hammer = False

    def update(self, user_input):#
        if self.dino_run:
            self.run() #creo que depsues se le borra xd
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif not self.dino_jump and not self.dino_duck: 
            #no menciono los tres antes ya que no cambian de estado y no es necesario volver a colocar lo mismo
            #pero ambos llegana quí cuando dejan de presionar alguna tecla, entonces es necesario
            self.dino_jump = False
            self.dino_duck = False
            self.dino_run = True

        if self.step_index >= 9:
            self.step_index = 0

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type] 
        if self.dino_jump:
            self.dino_rect.y -= self.jum_vel * 4
            self.jum_vel -= 0.8

        #sin esto cae al vacio xd
        if self.jum_vel < -self.JUM_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jum_vel = self.JUM_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCKING #si lo dejo con self.Y_POS vuela xd
        self.step_index += 1

    def check_invicibility(self, screen):
        if self.shield:
            time_to_show = round((self.power_up_time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show >= 0 and self.show_text:
                get_text(f"Shield enabled for {time_to_show}", screen, 18, 500, 40)
            else:
                self.shield = False
                self.type = DEFAULT_TYPE

        if self.hammer:
            time_to_show = round((self.power_up_time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show >= 0 and self.show_text:
                get_text(f"Hammer enabled for {time_to_show}", screen, 18, 500, 40)
            else:
                self.hammer = False
                self.type = DEFAULT_TYPE


    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
