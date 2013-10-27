# -*- coding: utf-8 -*-
import pygame as pg

from soope.conf import MEDIA_PATH
from element import ElementBase


class Pipe(pg.sprite.Sprite, ElementBase):
    WIDTH = 64
    HEIGHT = 64
    REACT_WITH_OTHER = True

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("{0}/elements/pipe.gif".format(MEDIA_PATH))
        self.rect = pg.Rect(x, y, self.WIDTH, self.HEIGHT)