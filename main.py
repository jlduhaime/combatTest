import sys
import pygame as pg
import game


if __name__ == '__main__':
    game = game.Game()
    game.run()
    pg.quit()
    sys.exit()
