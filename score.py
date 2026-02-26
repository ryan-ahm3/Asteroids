import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Display_Score():
    def __init__(self, score, font):
        self.score = score
        self.font = pygame.font.Font(None, 32)


    def increase(self, amount):
        self.score += amount
    
    def draw(self, screen,):
        score_surface = self.font.render(f"{self.score}", True, (255, 255, 255))
        score_rect = score_surface.get_rect()
        score_rect.midtop = (SCREEN_WIDTH / 2, 20)
        screen.blit(score_surface, score_rect)