from pico2d import *
import game_world
import end_state
import game_framework

class Flag:
    image = None
    def __init__(self):
        if Flag.image == None:
            self.image = load_image('flag.png')
        self.x, self.y = 940, 700
        self.Flag_end = 0

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.Flag_end==1:
            game_framework.change_state(end_state)
        pass
    def get_bb(self):
        return self.x -30 , self.y - 30, self.x + 30, self.y + 30

    def handle_event(self, event):
        pass

    def handle_collision(self, other, group):
        if group == 'character:flag':
            print("cl")
            self.Flag_end = 1