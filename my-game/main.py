import pygame
import sys
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot




def main():

    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)


    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable, )
    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)

    


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0

    while True:
        dt = clock.tick(60) / 1000 
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
          for shot in shots:
            if asteroid.collides_with(shot):
                log_event("asteroid_shot")
                asteroid.split()
                shot.kill()

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for draw in drawable:
             draw.draw(screen)
        pygame.display.flip()

       

       

        

        

if __name__ == "__main__":
    main()

