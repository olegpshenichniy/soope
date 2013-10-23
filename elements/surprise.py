# -*- coding: utf-8 -*-
import pygame as pg
from soope.conf import MEDIA_PATH


class Surprise(pg.sprite.Sprite):
    WIDTH = 30
    HEIGHT = 30

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("{0}/elements/surprise.gif".format(MEDIA_PATH)).convert()
        self.rect = pg.Rect(x, y, self.WIDTH, self.HEIGHT)