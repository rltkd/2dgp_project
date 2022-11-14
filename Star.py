from pico2d import *
import game_world

class Star:
    image = None

    def __init__(self, x= 100 , y = 684//2, face_dir = 4):
        if Star.image == None:
            Star.image = load_image('star.png')
        self.x, self.y, self.face_dir = x, y, face_dir

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.x_velocity
        if self.x <20 or self.x >1020-20:
            game_world.remove_object(self)