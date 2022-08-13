import random
import pygame
from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.hammer import Hammer


class PowerUpMAnager:
    def __init__(self):
        self.power_ups = []
        self.when_appears  = 0

    def generate_power_up(self, points):
        if len(self.power_ups) == 0:
            if self.when_appears == points:
                #para que no se genere en el mismo punto
                self.when_appears = random.randint(self.when_appears +200, self.when_appears + 300)
                power_up_type = Shield() if random.randint(0,1) == 0 else Hammer() #añade un powerup random
                self.power_ups.append(power_up_type)

    def update(self, points, game_speed, player):
        self.generate_power_up(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                if power_up == Shield:
                    player.shield = True
                    player.show_text = True
                else:
                    player.hammer = True
                    player.show_text = True
                player.type = power_up.type
                time_random = random.randint(5, 8)
                player.power_up_time_up = power_up.start_time + (time_random * 1000) ###
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200,300)
