from pico2d import *
import game_world
import game_framework

width , height = 1024, 684

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

player = None

class Sight:
    image = None
    def __init__(self, x=  width//2 , y = height//2,x_velocity=0,y_velocity=0):
        if Sight.image == None:
            Sight.image = load_image('sight.png')
        self.x, self.y,self.x_velocity, self.y_velocity = x, y,x_velocity,y_velocity

    def draw(self):
        self.image.draw(self.x, self.y-90)

    def update(self):
        self.x += self.x_velocity
        # self.y += self.y_velocity
