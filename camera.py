# -*- coding: utf-8 -*-
import pygame as pg

from soope import conf


class Camera(object):
    def __init__(self, level_width, level_height):
        self.camera_func = Camera.camera_configure
        self.state = pg.Rect(0, 0, level_width, level_height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

    # CONFIGURE CAMERA
    @staticmethod
    def camera_configure(camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t = -l + conf.WIN_WIDTH / 2, -t + conf.WIN_HEIGHT / 2

        # Не движемся дальше левой границы
        l = min(0, l)

        # Не движемся дальше правой границы
        l = max(-(camera.width - conf.WIN_WIDTH), l)

        # Не движемся дальше нижней границы
        t = max(-(camera.height - conf.WIN_HEIGHT), t)

        # Не движемся дальше верхней границы
        t = min(0, t)

        return pg.Rect(l, t, w, h)