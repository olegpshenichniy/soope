# -*- coding: utf-8 -*-
import pygame as pg

from soope.conf import MEDIA_PATH
from soope import pyganim

#from blocks import Platform, DeathBlock, BlockTeleport
#from monsters import Monster


class Mario(pg.sprite.Sprite):

    WIDTH = 22
    HEIGHT = 32
    COLOR = "#888888"

    MOVE_SPEED = 2.5
    MOVE_EXTRA_SPEED = 4
    JUMP_POWER = 10
    JUMP_EXTRA_POWER = 20
    GRAVITY = 0.35

    # EVENTS
    AVAILABLE_EVENTS = ('left', 'right', 'up', 'running')

    # ANIMATION #

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

    def __init__(self, x, y, surface, camera):
        self._surface = surface
        self._camera = camera

        pg.sprite.Sprite.__init__(self)

        self.xvel = 0
        self.yvel = 0
        self.on_ground = False

        # create events dict
        self.events = {e: None for e in self.AVAILABLE_EVENTS}

        # start position
        self.startX = x
        self.startY = y

        self.image = pg.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill(pg.Color(self.COLOR))

        # make image transparent
        self.image.set_colorkey(pg.Color(self.COLOR))

        # object rectangle
        self.rect = pg.Rect(x, y, self.WIDTH, self.HEIGHT)

        # ANIMATION #
        self.boltAnimStay = pyganim.PygAnimation(self.ANIMATION_STAY)
        self.boltAnimStay.play()

        # stay by default
        self.boltAnimStay.blit(self.image, (0, 0))

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

    def listent_event(self, event, joystick=None):

        print 'event : ' + str(event.type)

        if joystick:
            if event.type == pg.locals.JOYAXISMOTION:
                x, y = joystick.get_axis(0), joystick.get_axis(1)
                print 'x and y : ' + str(x) + ' , ' + str(y)
            elif event.type == pg.locals.JOYBALLMOTION:
                print 'ball motion'
            elif event.type == pg.locals.JOYHATMOTION:
                print 'hat motion'
            elif event.type == pg.locals.JOYBUTTONDOWN:
                print 'button down'
            elif event.type == pg.locals.JOYBUTTONUP:
                print 'button up'

        if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
            self.events['left'] = True
        if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            self.events['right'] = True

        if event.type == pg.KEYUP and event.key == pg.K_RIGHT:
            self.events['right'] = False
        if event.type == pg.KEYUP and event.key == pg.K_LEFT:
            self.events['left'] = False

        if event.type == pg.KEYDOWN and event.key == pg.K_UP:
            self.events['up'] = True
        if event.type == pg.KEYUP and event.key == pg.K_UP:
            self.events['up'] = False

        if event.type == pg.KEYDOWN and event.key == pg.K_LSHIFT:
            self.events['running'] = True
        if event.type == pg.KEYUP and event.key == pg.K_LSHIFT:
            self.events['running'] = False

    def update(self, platforms):

        if self.events['up']:
            if self.on_ground:
                self.yvel = -self.JUMP_POWER
                # if running and move -> jump higher
                if self.events['running'] and (self.events['left'] or self.events['right']):
                    self.yvel -= self.JUMP_EXTRA_POWER
            self.image.fill(pg.Color(self.COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))

        if self.events['left']:
            self.xvel = -self.MOVE_SPEED
            self.image.fill(pg.Color(self.COLOR))
            if self.events['running']:
                self.xvel -= self.MOVE_EXTRA_SPEED
                if not self.events['up']:
                    self.boltAnimLeftSuperSpeed.blit(self.image, (0, 0))
            else:
                if not self.events['up']:
                    self.boltAnimLeft.blit(self.image, (0, 0))

            if self.events['up']:
                self.boltAnimJumpLeft.blit(self.image, (0, 0))

        if self.events['right']:
            self.xvel = self.MOVE_SPEED
            self.image.fill(pg.Color(self.COLOR))
            if self.events['running']:
                self.xvel += self.MOVE_EXTRA_SPEED
                if not self.events['up']:
                    self.boltAnimRightSuperSpeed.blit(self.image, (0, 0))
            else:
                if not self.events['up']:
                    self.boltAnimRight.blit(self.image, (0, 0))

            if self.events['up']:
                self.boltAnimJumpRight.blit(self.image, (0, 0))

        if not (self.events['left'] or self.events['right']):
            self.xvel = 0
            if not self.events['up']:
                self.image.fill(pg.Color(self.COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))

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