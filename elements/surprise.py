# -*- coding: utf-8 -*-
import pygame as pg

from soope.conf import MEDIA_PATH
from element import ElementBase


class Surprise(pg.sprite.Sprite, ElementBase):
    WIDTH = 30
    HEIGHT = 30
    REACT_WITH_OTHER = True

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("{0}/elements/surprise.gif".format(MEDIA_PATH)).convert()
        self.rect = pg.Rect(x, y, self.WIDTH, self.HEIGHT)