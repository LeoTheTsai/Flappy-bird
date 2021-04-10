import pygame
from random import randint
from pipe import pipe

class pipeManager():
    def __init__(self, surfaceW, surfaceH):
        self.surfaceW = surfaceW
        self.surfaceH = surfaceH
        self.pipew = 100
        self.pipeh = 400
        self.pipeList = []
        self.spawntime = 50
        self.spawnmaxtime = 50


    def add_pipe(self):
        height = randint(100, 200)
        gap = randint(100, 250)
        top_pipe = pygame.Surface((self.pipew, height))
        top_pipe.fill((0, 255, 0))
        bottom_pipe = pygame.Surface((self.pipew, self.surfaceH - (height + gap)))
        bottom_pipe.fill((0,255,0))

        top = pipe(top_pipe, [self.surfaceW - 100, 0], "top", height)
        bottom = pipe(bottom_pipe, [self.surfaceW - 100, self.surfaceH - (height + gap)], "bottom", height)

        self.pipeList.append(top)
        self.pipeList.append(bottom)

    def manage(self):
        if self.spawntime >= self.spawnmaxtime:
            self.add_pipe()
            self.spawntime = 0
        else:
            self.spawntime += 1
        self.move_pipe()
        self.delete_pipe()



    def delete_pipe(self):
        for p in self.pipeList:
            if p.position[0] <= 0:
                self.pipeList.remove(p)


    def move_pipe(self):
        for p in self.pipeList:
            p.position[0] -= 10


    def draw(self, display_surface):
        for p in self.pipeList:
            display_surface.blit(p.image, p.position)

    def collision(self, bird):
        for p in self.pipeList:
            # if (bird.bird_x >= (p.position[0] - self.pipew)) and (bird.bird_x <= p.position[0]):
            if bird.bird_x in range(p.position[0] - self.pipew, p.position[0]):
                if p.direction == "top" and bird.bird_y <= p.grow:
                    return True
                elif p.direction == "bottom" and bird.bird_y >= (p.position[1]):
                    return True
        return False



