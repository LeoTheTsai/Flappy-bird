import pygame

class pipe():
    def __init__(self, image, position, direction, grow):
        self.image = image
        self.position = position
        self.direction = direction
        self.grow = grow

