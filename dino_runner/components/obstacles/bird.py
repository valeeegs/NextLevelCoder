
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self, type):
        self.type = type
        self.image = BIRD
        super().__init__(self.image, self.type)
        self.rect.y = 265
        self.fly_index = 0
    
    def draw(self, screen):
        if self.fly_index >= 9:
            self.fly_index = 0
        
        screen.blit(self.image[self.fly_index//5], self.rect)
        self.fly_index += 1

        