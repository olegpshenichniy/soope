import pygame as pg

from soope.events.constants import *


class EventPlayer(object):
    """
    Class for Base player class. Add events listening.
    """

    AVAILABLE_EVENTS = (LEFT, RIGHT, UP, RUN, DOWN)

    def __init__(self):
        self.events = {e: None for e in self.AVAILABLE_EVENTS}

    def listen_event(self, event, joystick=None):
        # JOYSTICK
        if joystick:

            if event.type == pg.locals.JOYHATMOTION:
                if event.value[0] == 0:
                    self.events[RIGHT] = False
                    self.events[LEFT] = False
                elif event.value[0] == 1:
                    self.events[RIGHT] = True
                elif event.value[0] == -1:
                    self.events[LEFT] = True

                if event.value[1] == 1:
                    self.events[UP] = True
                elif event.value[1] == 0:
                    self.events[UP] = False

            elif event.type == pg.locals.JOYBUTTONDOWN:
                if event.button == 3:
                    self.events[UP] = True
                elif event.button == 1:
                    self.events[RUN] = True

            elif event.type == pg.locals.JOYBUTTONUP:
                if event.button == 3:
                    self.events[UP] = False
                elif event.button == 1:
                    self.events[RUN] = False

        # KEYBOARD
        else:

            if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                self.events[LEFT] = True
            elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                self.events[RIGHT] = True

            if event.type == pg.KEYUP and event.key == pg.K_RIGHT:
                self.events[RIGHT] = False
            elif event.type == pg.KEYUP and event.key == pg.K_LEFT:
                self.events[LEFT] = False

            if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                self.events[UP] = True
            elif event.type == pg.KEYUP and event.key == pg.K_UP:
                self.events[UP] = False

            if event.type == pg.KEYDOWN and event.key == pg.K_LSHIFT:
                self.events[RUN] = True
            elif event.type == pg.KEYUP and event.key == pg.K_LSHIFT:
                self.events[RUN] = False