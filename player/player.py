# -*- coding: utf-8 -*-
import pygame as pg

from soope.conf import MEDIA_PATH

from soope.events.constants import *
from soope.events.player import EventPlayer
from soope.animation.player import PlayerAnimation

#from blocks import Platform, DeathBlock, BlockTeleport
#from monsters import Monster


class Player(pg.sprite.Sprite, EventPlayer, PlayerAnimation):

    WIDTH = 22
    HEIGHT = 32
    COLOR = "#888888"

    MOVE_SPEED = 2.5
    MOVE_EXTRA_SPEED = 4
    JUMP_POWER = 10
    JUMP_EXTRA_POWER = 4
    GRAVITY = 0.35

    def __init__(self, x, y, surface, camera):
        EventPlayer.__init__(self)
        PlayerAnimation.__init__(self)

        self._surface = surface
        self._camera = camera

        pg.sprite.Sprite.__init__(self)

        self.xvel = 0
        self.yvel = 0
        self.on_ground = False

        # start position
        self.startX = x
        self.startY = y

        self.image = pg.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill(pg.Color(self.COLOR))

        # stay by default
        self.boltAnimStay.blit(self.image, (0, 0))

        # make image transparent
        self.image.set_colorkey(pg.Color(self.COLOR))

        # object rectangle
        self.rect = pg.Rect(x, y, self.WIDTH, self.HEIGHT)

    def render(self):
        # render
        self._surface.blit(self.image, self._camera.apply(self))

    def collide(self, xvel, yvel, level_elements):
        for elem in level_elements:

            # if user collide with collideable elem
            if elem.REACT_WITH_OTHER and pg.sprite.collide_rect(self, elem):

                # if move right
                if xvel > 0:
                    # not move right
                    self.rect.right = elem.rect.left

                # if move left
                if xvel < 0:
                    # not move left
                    self.rect.left = elem.rect.right

                # if fall down
                if yvel > 0:
                    # stop fall down
                    self.rect.bottom = elem.rect.top

                    # stay on ground
                    self.on_ground = True

                    # fall energy disappear
                    self.yvel = 0

                # if move up
                if yvel < 0:
                    # stop move up
                    self.rect.top = elem.rect.bottom

                    # jump energy disappear
                    self.yvel = 0

                ## bad block
                #if isinstance(p, self.DeathBlock) or isinstance(p, self.Monster):
                #    self.die()
                #
                ## move logik into block class
                #if hasattr(p, 'player_action'):
                #    p.player_action(self)

    def update(self, platforms):
        self.__apply_movement()

        # move rect object
        if not self.on_ground:
            self.yvel += self.GRAVITY
        self.on_ground = False

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

    #def die(self):
    #    pg.time.wait(500)
    #    self.teleporting(self.startX, self.startY)
    #
    #def teleporting(self, goX, goY):
    #    self.rect.x = goX
    #    self.rect.y = goY

    def __apply_movement(self):
        """
        Change player coordinate using move events.
        """
        if self.events[UP]:
            if self.on_ground:
                self.yvel = -self.JUMP_POWER
                # if running and move -> jump higher
                if self.events[RUN] and (self.events[LEFT] or self.events[RIGHT]):
                    self.yvel -= self.JUMP_EXTRA_POWER
            self.image.fill(pg.Color(self.COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))

        if self.events[LEFT]:
            self.xvel = -self.MOVE_SPEED
            self.image.fill(pg.Color(self.COLOR))
            if self.events[RUN]:
                self.xvel -= self.MOVE_EXTRA_SPEED
                if not self.events[UP]:
                    self.boltAnimLeftSuperSpeed.blit(self.image, (0, 0))
            else:
                if not self.events[UP]:
                    self.boltAnimLeft.blit(self.image, (0, 0))

            if self.events[UP]:
                self.boltAnimJumpLeft.blit(self.image, (0, 0))

        if self.events[RIGHT]:
            self.xvel = self.MOVE_SPEED
            self.image.fill(pg.Color(self.COLOR))
            if self.events[RUN]:
                self.xvel += self.MOVE_EXTRA_SPEED
                if not self.events[UP]:
                    self.boltAnimRightSuperSpeed.blit(self.image, (0, 0))
            else:
                if not self.events[UP]:
                    self.boltAnimRight.blit(self.image, (0, 0))

            if self.events[UP]:
                self.boltAnimJumpRight.blit(self.image, (0, 0))

        if not (self.events[LEFT] or self.events[RIGHT]):
            self.xvel = 0
            if not self.events[UP]:
                self.image.fill(pg.Color(self.COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))
