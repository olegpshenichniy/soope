import pygame as pg

import conf
from elements.brick import Brick
from elements.cloud import Cloud
from elements.pipe import Pipe
from elements.surprise import Surprise


class Level(object):

    BACKGROUND_COLOR = "#339DD3"
    MAP = [
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "             c            c           c              c       ",
       "                                                             ",
       "    c                                                        ",
       "                                          c                  ",
       "     c       c      c                                        ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                                                             ",
       "                    s                                        ",
       "                                                             ",
       "     s                                                       ",
       "             s                                               ",
       "                                                             ",
       "                                bbbbbbb                      ",
       "                       bb           bbb                      ",
       "      p   p        bbbbbbb  p   bbbbbbb                      ",
       "                                                             ",
       "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb  bbbbbbbbbbbbb",
       "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb  bbbbbbbbbbbbb",
       "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb  bbbbbbbbbbbbb",
       "bbbbbbbbbbbbbbsssssbbb                          bbbbbbbbbbbbb",
       "b                                                  bbbbbbb   ",
       "b      bbbbbbbbbbbbbbbbb  bbbbbbbbbbbbbbbbb      p    bb     ",
       "b                                                     bb bb  ",
       "b                         bbbbbbbbbbbbbbbbbbbbbbbbbbbbb   b  ",
       "b    ss   sbsbsbsb bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb ",
       "b                                                            ",
       "b                     p                   p                  ",
       "b                        sbsbsb                              ",
       "b    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb        ",
       "b                                                            ",
       "b                                                            ",
       "                                                             ",
       "                                                             ",
       "      s d                                                    ",
       "                    s                                        ",
       "                                                             ",
       "     s   f    f                                              ",
       "             s                                               ",
       "                                                             ",
       "                                bbbbbbb                      ",
       "                       bb           bbb                      ",
       "      p   p        bbbbbbb  p   bbbbbbb                      ",
       "                                                             ",
       "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
       "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
       "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
       "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    ]

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
        # level platforms
        x = y = 0
        for row in self.MAP:
            for col in row:
                if col == "b":
                    pf = Brick(x, y)
                    self._elements.add(pf)
                elif col == "c":
                    pf = Cloud(x, y)
                    self._elements.add(pf)
                elif col == "p":
                    pf = Pipe(x, y)
                    self._elements.add(pf)
                elif col == "s":
                    pf = Surprise(x, y)
                    self._elements.add(pf)

                x += Brick.WIDTH
            y += Brick.HEIGHT
            x = 0

    def render(self):
        # render background
        self._surface.blit(self._bg, (0, 0))

        # draw entities
        for e in self._elements:
            self._surface.blit(e.image, self._camera.apply(e))

    def get_elements(self):
        return self._elements
