import game_world

import play_state
import load_state
import game_framework
from pico2d import *

image = None
class Item:
    def __init__(self):
        if self.image ==None:
            self.image = load_image('item.png')
            self.x, y = 0 , 0

    def __draw__(self):
        self.image.draw(x,y)
