from pico2d import *
import game_world
width, height = 960,780
tilesize = 60
rows= 16
cols =13
#60,60
map_data = [

            [1, 2, 1, 0, 0, 5, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [4, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
            [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 5, 0, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 5, 0, 1, 1, 1],
            [0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 3],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],

            ]
class Wall:
    image = None
    def __init__(self,y,x):
        if Wall.image == None:
            Wall.image = load_image('block1.png')
        self.x, self.y = (x * 60)+ 30 , (y * 60) + 30
        self.bc = 2

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
    def update(self):
        if self.bc <= 0:
            try:
                game_world.remove_object(self)
            except:
                pass
        pass
    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30
    def handle_collision(self,other,group):
         if group == 'star:block':
             self.bc -= 1

class Empty:

    def __init__(self,y,x):
        self.x, self.y = (x * 60) + 30 , (y * 60) + 30
    def get_pos(self):
        return self.x, self.y
    def draw(self):
        pass
    def update(self):
        pass
    def get_bb(self,x,y):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30
    def handle_collision(self,other,group):
        pass