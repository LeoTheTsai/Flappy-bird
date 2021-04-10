import pygame
from bird import bird
from pipeManager import pipeManager
import time


pygame.init()
width = 1440
height = 800
black = (0,0,0)

bird_x = 300
bird_y = 400


clock = pygame.time.Clock()

#make the pygame window
display_surface = pygame.display.set_mode((width, height))
birdy = bird(bird_x, bird_y)
pipeManager = pipeManager(width, height)


# def collision(bird, pipe):
#     for p in pipe.pipeList:
#         if bird.bird_x == (p.position[0] - pipe.pipew):
#             if p.direction == "bottom" and bird.bird_y >= p.position[1]:
#                 if p.direction == "top" and bird.bird_y <= p.grow:
#                     return True
#     return False



while (True):
    display_surface.fill(black)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    if birdy.bird_y <= 0 or birdy.bird_y >= height:
        print("You Lose!!!")
        break
    elif pipeManager.collision(birdy):
        print("Collision!!!")
        break
    birdy.draw(display_surface)
    birdy.update()
    pipeManager.draw(display_surface)
    pipeManager.manage()
    pygame.display.update()
    clock.tick(30)

pygame.quit()

