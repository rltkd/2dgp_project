from pico2d import *
width, height = 1024, 684

class Map:
    def __init__(self):
        self.image = load_image('stage.png')

    def draw(self):
        self.image.draw(width//2, height//2)

