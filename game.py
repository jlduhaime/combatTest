import sys
import pygame as pg
from pygame.locals import *
from player import Player
from mob import Mob
import constants as c

class Game:

    def __init__(self):
        pg.init()
        self.is_running = False
        self.clock = pg.time.Clock()
        self.display = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        self.player = Player("Hector")
        self.mobs = [Mob() for i in range(5)]
        pg.display.set_caption('Combat Sample')

    def on_event(self, event):
        """ handles incoming events """
        if event.type == QUIT:
            self.is_running = False
        if event.type == KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.is_running = False
        return

    def on_loop(self):
        """ handles game loop """
        return

    def on_render(self):
        """ handles changes to screen object """
        self.display.fill(c.BLACK)
        pg.display.flip()
        return

    def on_cleanup(self):
        """ handles resource cleanup """
        return

    def run(self):
        """ handels game looping method """
        self.is_running = True

        while self.is_running:
            for event in pg.event.get():
                self.on_event(event)

            self.on_loop()

            self.on_render()

            self.clock.tick(c.FPS)

        self.on_cleanup()
