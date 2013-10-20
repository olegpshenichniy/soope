import pygame as pg

import conf


class Level(object):

    MAP = [
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             "
    ]


    def __init__(self, surface):
        self.surface = surface

        self._sprite_sheet = pg.image.load(
            conf.MEDIA_PATH + 'sheets/mario/mario.gif').convert()

        self._create_map()

    def _create_map(self):
        pass

    def render(self):
        self.surface.blit(self._sprite_sheet, (0, 0), (0, 0, 100, 100))
        pg.display.flip()