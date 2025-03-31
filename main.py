# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    loop = True
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while loop == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        pygame.Surface.fill(screen, (0,0,0))
        player.draw(screen)
        pygame.display.update()
        clock.tick(60)
        dt = clock.tick(60)/1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()