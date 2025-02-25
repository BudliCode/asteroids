from circleshape import CircleShape
from constants import SHOT_RADIUS, SHOT_SPEED
import pygame as pg


class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pg.Vector2(0, 1).rotate(rotation) * SHOT_SPEED

    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position = self.position + self.velocity * dt
