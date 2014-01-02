# -*- coding: utf-8 -*-
import pygame as pg
from pygame.locals import *

import conf
from camera import Camera
from level import Level
from player.player import Player


class App(object):
    WIN_SIZE = conf.WIN_SIZE

    def __init__(self):
        pg.init()

        # joy stick
        pg.joystick.init()
        try:
            self.joystick = pg.joystick.Joystick(0)
            self.joystick.init()
            print 'Enabled joystick: ' + self.joystick.get_name()
        except pg.error:
            print 'no joystick found.'
            self.joystick = None

        self._running = True
        self.display_surf = None

        self.level = None
        self.player = None
        self.timer = None

    def on_init(self):
        pg.display.set_caption("PyMario")

        self.display_surf = pg.display.set_mode(
            self.WIN_SIZE,
            pg.HWSURFACE | pg.DOUBLEBUF
        )
        self._running = True

        # timer fps
        self.timer = pg.time.Clock()

        # camera
        self.camera = Camera(level_width=len(Level.MAP[0]) * 30,
                             level_height=len(Level.MAP) * 30)

        # create level
        self.level = Level(surface=self.display_surf, camera=self.camera)

        # create player
        self.player = Player(60, 60, surface=self.display_surf, camera=self.camera)

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            self.timer.tick(conf.FPS)
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self._on_cleanup()

    def on_event(self, event):
        self._listen_event(event)
        self.player.listen_event(event, joystick=self.joystick)

    def on_loop(self):
        # center camera on player
        self.camera.update(self.player)

        # update mario
        self.player.update(self.level.get_elements())

    def on_render(self):
        # render level
        self.level.render()
        self.player.render()

        pg.display.update()

    def _on_cleanup(self):
        pg.quit()

    def _listen_event(self, event):
        if event.type == pg.QUIT:
            self._running = False


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()