
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self):
        self.image = BIRD[0]
        self.fly_index = 0
        self.type = 1
        super().__init__(self.fly(), self.type)
        self.rect.y = 100

    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.fly_index += 1

        if self.fly_index >= 10:
            self.fly_index = 0

