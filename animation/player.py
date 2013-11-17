# -*- coding: utf-8 -*-
import pygame as pg

from soope.conf import MEDIA_PATH
from soope import pyganim


class PlayerAnimation(object):
    ANIMATION_DELAY = 0.1
    ANIMATION_SUPER_SPEED_DELAY = 0.05

    ANIMATION_RIGHT = [('{0}/player/mario/r1.png'.format(MEDIA_PATH)),
                       ('{0}/player/mario/r2.png'.format(MEDIA_PATH)),
                       ('{0}/player/mario/r3.png'.format(MEDIA_PATH)),
                       ('{0}/player/mario/r4.png'.format(MEDIA_PATH)),
                       ('{0}/player/mario/r5.png'.format(MEDIA_PATH))]
    ANIMATION_LEFT = [('{0}/player/mario/l1.png'.format(MEDIA_PATH)),
                      ('{0}/player/mario/l2.png'.format(MEDIA_PATH)),
                      ('{0}/player/mario/l3.png'.format(MEDIA_PATH)),
                      ('{0}/player/mario/l4.png'.format(MEDIA_PATH)),
                      ('{0}/player/mario/l5.png'.format(MEDIA_PATH))]
    ANIMATION_JUMP_LEFT = [('{0}/player/mario/jl.png'.format(MEDIA_PATH), 0.1)]
    ANIMATION_JUMP_RIGHT = [('{0}/player/mario/jr.png'.format(MEDIA_PATH), 0.1)]
    ANIMATION_JUMP = [('{0}/player/mario/j.png'.format(MEDIA_PATH), 0.1)]
    ANIMATION_STAY = [('{0}/player/mario/0.png'.format(MEDIA_PATH), 0.1)]

    def __init__(self):
        self.boltAnimStay = pyganim.PygAnimation(self.ANIMATION_STAY)
        self.boltAnimStay.play()

        # move right anim
        boltAnim = []
        for anim in self.ANIMATION_RIGHT:
            boltAnim.append((anim, self.ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()

        # move left anim
        boltAnim = []
        for anim in self.ANIMATION_LEFT:
            boltAnim.append((anim, self.ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimJumpLeft = pyganim.PygAnimation(self.ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(self.ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(self.ANIMATION_JUMP)
        self.boltAnimJump.play()

        # fast move right anim
        boltAnim = []
        boltAnimSuperSpeed = []
        for anim in self.ANIMATION_RIGHT:
            boltAnim.append((anim, self.ANIMATION_DELAY))
            boltAnimSuperSpeed.append((anim, self.ANIMATION_SUPER_SPEED_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        self.boltAnimRightSuperSpeed = pyganim.PygAnimation(boltAnimSuperSpeed)
        self.boltAnimRightSuperSpeed.play()

        # fast move left anim
        boltAnim = []
        boltAnimSuperSpeed = []
        for anim in self.ANIMATION_LEFT:
            boltAnim.append((anim, self.ANIMATION_DELAY))
            boltAnimSuperSpeed.append((anim, self.ANIMATION_SUPER_SPEED_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        self.boltAnimLeftSuperSpeed = pyganim.PygAnimation(boltAnimSuperSpeed)
        self.boltAnimLeftSuperSpeed.play()


