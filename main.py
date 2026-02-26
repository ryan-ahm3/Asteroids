import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Display_Score
from lifedisplay import LifeDisplay

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score_keeper = Display_Score(0, None)
    life_display = LifeDisplay()
    lives = 3

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while(1):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for obj in asteroids:
            if obj.collides_with(player) and player.invulnerable_timer <= 0:
                lives -= 1
                if lives > 0:
                    player.respawn()
                else:
                    print("Game over!")
                    sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid) == True:
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    score_keeper.increase(100) 

            
        # Draw
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
            score_keeper.draw(screen)
            life_display.draw(screen, lives)

        pygame.display.flip()

        # Locked to 60 fps
        dt = clock.tick(60) / 1000 

        

if __name__ == "__main__":
    main()
