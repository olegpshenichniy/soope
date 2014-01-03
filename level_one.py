import pygame as pg
from PIL import Image

import conf
from elements.brick import Brick
from elements.cloud import Cloud
from elements.pipe import Pipe
from elements.surprise import Surprise

from level.transformer import Transformer
from level import colors


class Level(object):

    BACKGROUND_COLOR = "#339DD3"
    MAP = []

    def __init__(self, surface, camera):

        # surface (main screen)
        self._surface = surface
        self._camera = camera

        self._bg = None
        self._elements = pg.sprite.Group()

        # load sprite sheet
        #self._sprite_sheet = pg.image.load(conf.MEDIA_PATH + 'sheets/mario.gif').convert()

        # set background
        self._set_background()

        # create map
        self._create_map()

    def _set_background(self):
        self._bg = pg.Surface(conf.WIN_SIZE)
        self._bg.fill(pg.Color(self.BACKGROUND_COLOR))

    def _create_map(self):

        transformer = Transformer("{0}/level/1.png".format(conf.MEDIA_PATH),
                                  BOLE=Brick,
                                  AZURE_MIST_WEB=Cloud,
                                  BANANA_YELLOW=Surprise,
                                  ANDROID_GREEN=Pipe)

        converted_map = transformer.convert()
        self._elements.add(converted_map)


    def render(self):
        # render background
        self._surface.blit(self._bg, (0, 0))

        # draw entities
        for e in self._elements:
            self._surface.blit(e.image, self._camera.apply(e))

    def get_elements(self):
        return self._elements



