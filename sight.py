from pico2d import *
import game_world

class Sight:
    image = None

    def __init__(self, x= 1024//2, y = 684//2):
        if Sight.image == None:
            Sight.image == load_image('sight.png')
        self.screen_delay = 0
        self.x, self.y = x, y
        self.blind = True
        if not self.blind:
            self.screen_delay = (self.screen_delay +1) % 15
            if(self.screen_delay == 0):
                self.blind = False

    def draw(self):
        self.draw(self.x, self.y-90)

    def update(self):
        pass