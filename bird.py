import pygame

class bird():
    def __init__(self, bird_x, bird_y):
        self.y_change = 0
        self.scale_x = 100
        self.scale_y = 100
        self.bird_x = bird_x
        self.bird_y = bird_y
        self.image = pygame.image.load("bird.png")
        self.image = pygame.transform.scale(self.image, (self.scale_x, self.scale_y))

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.y_change += 2
        else:
            self.y_change -= 3
        self.bird_y -= self.y_change

    def draw(self, surface):
        surface.blit(self.image, (self.bird_x, self.bird_y))

    def on_hit(self):
        self.bird_y -= 3
