import sys
import pygame

# Configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Game loop.
while  True:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('UP Pressed')
            elif event.key == pygame.K_DOWN:
                print('DOWN Pressed')
            elif event.key == pygame.K_LEFT:
                print('LEFT Pressed')
            elif event.key == pygame.K_RIGHT:
                print('RIGHT Pressed')

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        print('W Pressed')

    pygame.display.flip()
    fpsClock.tick(fps)