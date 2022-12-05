from pico2d import *
import game_world
import game_framework

import server

width , height = 1024, 684

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class Sight:
    def __init__(self):
        Sight.image = load_image('sight.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.draw_sight = True
        self.timer = 0.6
    def draw(self):
        # fill here
        if not self.draw_sight:
            self.image.draw(server.character.x, server.character.y-90)
        else:
            pass


    def update(self):
        if not self.draw_sight:
            self.timer -= game_framework.frame_time
            if self.timer <= 0:
                self.timer = 0.6
                self.draw_sight = True
        pass

    def handle_event(self):
        pass