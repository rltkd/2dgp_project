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

    def draw(self):
        # fill here
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom,
                                       self.canvas_width, self.canvas_height,
                                       0, 0)
        pass

    def update(self):
        # fill heres
        self.window_left = clamp(0,
                                 int(server.character.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0,
                                   int(server.character.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height - 1)
        pass

    def handle_event(self):
        events = get_events()
        for event in events:
            if event.type == SDLK_a:
                return True