import pygame
from constants import SCREEN_WIDTH

class LifeDisplay:
    def __init__(self):
        self.spacing = 30
        self.size = 15
        self.margin = 25

    def draw(self, screen, current_lives):
        for i in range(current_lives):
            x = SCREEN_WIDTH - self.margin - (i * self.spacing)
            y = self.margin
            
            # small triangle pointing up
            points = [
                (x, y - self.size),
                (x - self.size/2, y + self.size/2),
                (x + self.size/2, y + self.size/2)
            ]
            
            pygame.draw.polygon(screen, "white", points, 2)
