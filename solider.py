import random
import math
import game_framework


from pico2d import *
import game_world

# Solider Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 15.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Solider Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3



class Solider:
    image = None

    def __init__(self, x, y):
        if self.image == None:
              self.image = load_image('solider.png')
        self.x, self.y = x, y
        self.x_int = self.x
        self.x_dir = 1
        self.speed = 0
        self.timer = 1.0 # change direction every 1 sec when wandering
        self.frame = 0
        self.x_velocity = 1


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        # if self.x_dir == 1:
        #     self.x += RUN_SPEED_PPS * game_framework.frame_time
        #     if self.x >= self.x_int + 200:
        #         self.x_dir = -1
        # elif self.x_dir == -1:
        #     self.x -= RUN_SPEED_PPS * game_framework.frame_time
        #     if self.x <= self.x_int - 100:
        #         self.x_dir = 1
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
    def draw(self):
        if self.x_dir == 1:
            self.image.clip_draw(int(self.frame) * 50, 50, 50, 50, self.x, self.y)
        elif self.x_dir == -1:
            self.image.clip_draw(int(self.frame) * 50, 100, 50, 50, self.x, self.y)
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x -15 , self.y - 15, self.x + 15, self.y + 15

    def handle_event(self, event):
        pass

    def handle_collision(self, other, group):
        if group == 'solider:block':
            if self.x < other.x:  # 오
                self.x_dir = -1
            elif self.x > other.x:  # 왼
                self.x_dir = 1
