from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_DELAY
import pygame as pg

from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_delay = 0

    def draw(self, screen):
        pg.draw.polygon(screen, "white", self.__triangle(), 2)

    def __rotate(self, dt):
        self.rotation = self.rotation + PLAYER_TURN_SPEED * dt

    def __move(self, dt):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def __shoot(self):
        if self.shot_delay > 0:
            return
        Shot(self.position[0], self.position[1], self.rotation)
        self.shot_delay = SHOT_DELAY

    def update(self, dt):
        keys = pg.key.get_pressed()
        if self.shot_delay > 0:
            self.shot_delay -= dt

        if keys[pg.K_a]:
            self.__rotate(-dt)
        if keys[pg.K_d]:
            self.__rotate(dt)
        if keys[pg.K_w]:
            self.__move(dt)
        if keys[pg.K_s]:
            self.__move(-dt)
        if keys[pg.K_SPACE]:
            self.__shoot()

    def __triangle(self):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        right = pg.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
