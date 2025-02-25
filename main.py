from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FRAMERATE
import pygame as pg

from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pg.init()

    clock = pg.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.fill("black")
        player.draw(screen)

        pg.display.flip()
        dt = clock.tick(FRAMERATE) / 1000


if __name__ == "__main__":
    main()
