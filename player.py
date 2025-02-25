from circleshape import CircleShape
from constants import PLAYER_RADIUS
import pygame as pg


class Player(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pg.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        right = pg.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
