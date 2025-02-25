from pygame.transform import rotate
from circleshape import CircleShape
import pygame as pg
import random

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position = self.position + self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        rotation = random.uniform(20, 50)
        v1 = self.velocity.rotate(rotation)
        v2 = self.velocity.rotate(-rotation)
        new_rad = self.radius - ASTEROID_MIN_RADIUS

        Asteroid(self.position[0], self.position[1], new_rad).velocity = v1 * 1.2
        Asteroid(self.position[0], self.position[1], new_rad).velocity = v2 * 1.2
