import pygame as pg
from pygame.locals import *

import conf
from level import Level
from player.mario import Mario


class App:
    WIN_SIZE = conf.WIN_SIZE

    def __init__(self):
        self._running = True
        self._display_surf = None

        self.level = None
        self.player = None

    def on_init(self):
        pg.init()
        pg.display.set_caption("PyMario")

        self._display_surf = pg.display.set_mode(
            self.WIN_SIZE,
            pg.HWSURFACE | pg.DOUBLEBUF
        )
        self._running = True
        
        # create level
        self.level = Level(self._display_surf)

        # create player
        self.player = Mario(self._display_surf, 100, 100)

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        # main loop
        while self._running:
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()

    def on_event(self, event):
        if event.type == pg.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        # render level
        self.level.render()
        self.player.render()

        pg.display.update()

    def on_cleanup(self):
        pg.quit()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()