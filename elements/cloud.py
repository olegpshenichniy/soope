# -*- coding: utf-8 -*-
import pygame as pg

from soope.conf import MEDIA_PATH
from element import ElementBase


class Cloud(pg.sprite.Sprite, ElementBase):
    WIDTH = 128
    HEIGHT = 48

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("{0}/elements/cloud.gif".format(MEDIA_PATH))
        self.rect = pg.Rect(x, y, self.WIDTH, self.HEIGHT)