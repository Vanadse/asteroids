# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init() # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Initialize pygame.display and pass screen settings
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #player.update(dt) 
        updatable.update(dt) 

        screen.fill("black")

        #player.draw(screen)
        for thing in drawable:
             thing.draw(screen)
        for asteroid in asteroids:
             if asteroid.is_colliding_with(player):
                  print("Game Over!")
                  return
             for shot in shots:
                  if shot.is_colliding_with(asteroid):
                       shot.kill()
                       asteroid.split()

        pygame.display.flip()

        dt = clock.tick(60) / 1000










# Dont edit below here-------------------

if __name__ == "__main__":
        main()