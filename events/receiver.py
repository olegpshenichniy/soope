import pygame as pg

from .constants import *


class Receiver(object):
    """
    Recive pygame event and return game readable event.
    """

    def __init__(self, pygame_event, joystick=None):
        self.pygame_event = pygame_event
        self.joystick = joystick
        self.game_events = set()

    def convert(self):

        # JOYSTICK
        if self.pygame_event.type == pg.locals.JOYHATMOTION:
            if self.pygame_event.value[0] == 1:
                self.game_events.add(RIGHT)
            elif self.pygame_event.value[0] == -1:
                self.game_events.add(LEFT)

            if self.pygame_event.value[1] == 1:
                self.game_events.add(UP)
            elif self.pygame_event.value[1] == -1:
                self.game_events.add(DOWN)

        elif self.pygame_event.type == pg.locals.JOYBUTTONDOWN:
            if self.pygame_event.button == 1:
                self.game_events.add(RUN)

        # KEYBOARD
        if self.pygame_event.type == pg.KEYDOWN and self.pygame_event.key == pg.K_LEFT:
            self.game_events.add(LEFT)
        elif self.pygame_event.type == pg.KEYDOWN and self.pygame_event.key == pg.K_RIGHT:
            self.game_events.add(RIGHT)

        if self.pygame_event.type == pg.KEYDOWN and self.pygame_event.key == pg.K_UP:
            self.game_events.add(UP)
        elif self.pygame_event.type == pg.KEYDOWN and self.pygame_event.key == pg.K_DOWN:
            self.game_events.add(DOWN)

        if self.pygame_event.type == pg.KEYDOWN and self.pygame_event.key == pg.K_LSHIFT:
            self.game_events.add(RUN)

        return self.game_events