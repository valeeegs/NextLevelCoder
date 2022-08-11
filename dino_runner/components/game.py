import pygame
from dino_runner.components.dinosaour import Dinosaour
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
FONT_STYLE = 'freesansbold.ttf'

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = Dinosaour()
        self.obstacle_manager =  ObstacleManager()
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = True
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.death_count = 0

    def execute(self):  
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self) #la instancia de la clase

    def update_score(self):
        #incrementar putnso y velocidad cada 100 puntos
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed +=1


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Points: {self.points}", True, (0,0,0)) #change color
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                self.playing = False
                self.running = False
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                self.run()


    def show_menu(self):
        self.screen.fill((255,255,255)) #Change color
        half_screen_height = SCREEN_HEIGHT//2
        half_screen_width = SCREEN_WIDTH//2
        
        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render("Press any Key to start", True, (0,0,0)) #change color
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)
        elif self.death_count > 0:
            #tarea
            #mostrar mensaje para reiniciar, puntos actuales, conteo de muertes
            pass

        self.screen.blit(RUNNING[0], (half_screen_width -20, half_screen_height - 140))
        pygame.display.update()
        self.handle_key_events_on_menu()
