from pico2d import *
import game_world

class Star:
    image = None

    def __init__(self, x= 100 , y = 684//2, x_velocity = 1):
        if Star.image == None:
            Star.image = load_image('star.png')
        self.x, self.y, self.velocity = x, y, x_velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity
        if self.x <20 or self.x >800-20:
            game_world.remove_object(self)