import pygame as pg
from pygame.locals import *

import conf
from level import Level


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1024, 800

        self.level = None

    def on_init(self):
        pg.init()
        self._display_surf = pg.display.set_mode(
            self.size,
            pg.HWSURFACE | pg.DOUBLEBUF
        )
        self._running = True
        
        # initialize level
        self.level = Level(self._display_surf)

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

        self.level.render()

        pass

    def on_cleanup(self):
        pg.quit()



if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()