import game_world

import play_state
import game_framework
from pico2d import *

class Star_Item:
    image = None
    def __init__(self,x, y):
        if Star_Item.image == None:
            self.image = load_image('item.png')
            self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass
    def get_bb(self):
        return self.x -25 , self.y - 25, self.x + 25, self.y + 25

    def handle_event(self, event):
        pass

    def handle_collision(self, other, group):
        if group == 'character:star_item':
            try:
                game_world.remove_object(self)
            except:
                pass


import game_world

import play_state
import game_framework
from pico2d import *

class Sight_Item:
    image = None
    def __init__(self,x, y):
        if Sight_Item.image == None:
            self.image = load_image('sight_item.png')
            self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass
    def get_bb(self):
        return self.x -25 , self.y - 25, self.x + 25, self.y + 25

    def handle_event(self, event):
        pass

    def handle_collision(self, other, group):
        if group == 'character:sight_item':
            try:
                game_world.remove_object(self)
            except:
                pass

