from pico2d import *
import game_world

class Star:
    image = None

    def __init__(self, x= 100 , y = 684//2, velocity = 4):
        if Star.image == None:
            Star.image = load_image('star.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.velocity == 4:
            self.x += self.velocity
        elif self.velocity ==5:
            self.x -= self.velocity
        elif self.velocity ==6:
            self.y += self.velocity
        elif self.velocity ==7:
            self.y -= self.velocity

        if self.x <30 or self.x >1020-30:
            game_world.remove_object(self)