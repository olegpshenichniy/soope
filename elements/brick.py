# -*- coding: utf-8 -*-
import pygame as pg
from soope.conf import MEDIA_PATH


class Brick(pg.sprite.Sprite):
    WIDTH = 30
    HEIGHT = 30

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("{0}/elements/brick.png".format(MEDIA_PATH))
        self.rect = pg.Rect(x, y, self.WIDTH, self.HEIGHT)