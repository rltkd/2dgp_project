from pico2d import *

import play_state
from Star import Star
import game_framework
import game_world
import server
width, height = 960,780
blind = True

#
# PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
# RUN_SPEED_KMPH = 20.0  # Km / Hour
# RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
# RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
# RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
#
# TIME_PER_ACTION = 0.5
# ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
# FRAMES_PER_ACTION = 8
#
# RIGHTKEY_DOWN, LEFTKEY_DOWN, UPKEY_DOWN, DOWNKEY_DOWN, RIGHTKEY_UP, LEFTKEY_UP, UPKEY_UP, DOWNKEY_UP, SPACE, A = range(10)
#
# key_event_table = {
#     (SDL_KEYDOWN, SDLK_RIGHT): RIGHTKEY_DOWN,
#     (SDL_KEYDOWN, SDLK_LEFT): LEFTKEY_DOWN,
#     (SDL_KEYDOWN, SDLK_UP): UPKEY_DOWN,
#     (SDL_KEYDOWN, SDLK_DOWN): DOWNKEY_DOWN,
#     (SDL_KEYUP, SDLK_RIGHT): RIGHTKEY_UP,
#     (SDL_KEYUP, SDLK_LEFT): LEFTKEY_UP,
#     (SDL_KEYUP, SDLK_UP): UPKEY_UP,
#     (SDL_KEYUP, SDLK_DOWN): DOWNKEY_UP,
#     (SDL_KEYDOWN, SDLK_SPACE): SPACE,
#     (SDL_KEYDOWN,SDLK_a):A
# }
# class WalkingState:
#     @staticmethod
#     def enter(character, event):
#         if event == RIGHTKEY_DOWN:
#             character.x_dir = 1
#
#
#         elif event == LEFTKEY_DOWN:
#             character.x_dir = -1
#
#         elif event == RIGHTKEY_UP:
#             character.x_dir = -1
#
#         elif event == LEFTKEY_UP:
#             character.x_dir = 1
#
#
#         if event == UPKEY_DOWN:
#
#             character.y_dir = 1
#
#         elif event == UPKEY_UP:
#
#             character.y_dir = -1
#
#         elif event == DOWNKEY_DOWN:
#             character.y_dir = -1
#
#
#         elif event == DOWNKEY_UP:
#             character.y_dir = 1
#
#
#
#
#     @staticmethod
#     def exit(character, event):
#         character.face_dir = character.dir
#         if event == SPACE:
#             character.star()
#
#     @staticmethod
#     def do(character):
#         character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
#         character.x += character.x_dir * RUN_SPEED_PPS * game_framework.frame_time
#         character.y += character.y_dir * RUN_SPEED_PPS * game_framework.frame_time
#         character.x = clamp(25, character.x, get_canvas_width() - 25)
#         character.y = clamp(25, character.y, get_canvas_height() - 25)
#
#     @staticmethod
#     def draw(character):
#         if character.x_dir > 0:
#             character.image.clip_draw(int(character.frame) * 100, 0, 100, 100, character.x, character.y)
#             character.dir = 4
#         elif character.x_dir < 0:
#             character.image.clip_draw(int(character.frame) * 100, 100, 100, 100, character.x, character.y)
#             character.dir = 5
#         elif character.x_dir == 0 and character.y_dir >0:
#             character.image.clip_draw(int(character.frame) * 100, 200, 100, 100, character.x, character.y)
#             character.dir = 6
#         elif character.x_dir == 0 and character.y_dir <0:
#             character.image.clip_draw(int(character.frame) * 100, 300, 100, 100, character.x, character.y)
#             character.dir = 7
#         elif character.x_dir == 0 and character.y_dir ==0:
#             character.image.clip_draw(int(character.frame) * 100, abs((character.face_dir))*100, 100, 100, character.x, character.y)
# class IDLE:
#     @staticmethod
#     def enter(character, event):
#         pass
#
#     @staticmethod
#     def exit(character,event):
#         pass
#
#     @staticmethod
#     def draw(character):
#         if character.x_dir > 0:
#             character.image.clip_draw(int(character.frame) * 100, 0, 100, 100, character.x, character.y)
#             character.dir = 4
#         elif character.x_dir < 0:
#             character.image.clip_draw(int(character.frame) * 100, 100, 100, 100, character.x, character.y)
#             character.dir = 5
#         elif character.x_dir == 0 and character.y_dir > 0:
#             character.image.clip_draw(int(character.frame) * 100, 200, 100, 100, character.x, character.y)
#             character.dir = 6
#         elif character.x_dir == 0 and character.y_dir < 0:
#             character.image.clip_draw(int(character.frame) * 100, 300, 100, 100, character.x, character.y)
#             character.dir = 7
#         elif character.x_dir == 0 and character.y_dir == 0:
#             character.image.clip_draw(int(character.frame) * 100, abs((character.face_dir)) * 100, 100, 100, character.x, character.y)
#
#     @staticmethod
#     def do(character):
#         pass
#
# next_state_table = {
#     WalkingState: {RIGHTKEY_UP: WalkingState, LEFTKEY_UP: IDLE, RIGHTKEY_DOWN: IDLE, LEFTKEY_DOWN: IDLE,
#                 UPKEY_UP: IDLE, UPKEY_DOWN: IDLE, DOWNKEY_UP: IDLE, DOWNKEY_DOWN: IDLE,
#                 SPACE: WalkingState, A:WalkingState},
#     IDLE: {RIGHTKEY_UP: WalkingState, LEFTKEY_UP: WalkingState, RIGHTKEY_DOWN: WalkingState, LEFTKEY_DOWN: WalkingState, UPKEY_UP: WalkingState, UPKEY_DOWN:WalkingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState, SPACE: IDLE, A: IDLE}
# }
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
RIGHTKEY_DOWN, LEFTKEY_DOWN, UPKEY_DOWN, DOWNKEY_DOWN, RIGHTKEY_UP, LEFTKEY_UP, UPKEY_UP, DOWNKEY_UP, SPACE, A = range(10)
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UPKEY_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWNKEY_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHTKEY_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFTKEY_UP,
    (SDL_KEYUP, SDLK_UP): UPKEY_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWNKEY_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN,SDLK_a):A
}
class WalkingState:
    @staticmethod
    def enter(character, event):
        if event == RIGHTKEY_DOWN:
            character.x_velocity += RUN_SPEED_PPS
            character.x_dir += 1
        elif event == RIGHTKEY_UP:
            character.x_velocity -= RUN_SPEED_PPS
            character.x_dir -= 1
        if event == LEFTKEY_DOWN:
            character.x_velocity -= RUN_SPEED_PPS
            character.x_dir -= 1
        elif event == LEFTKEY_UP:
            character.x_velocity += RUN_SPEED_PPS
            character.x_dir += 1
        if event == UPKEY_DOWN:
            character.y_velocity += RUN_SPEED_PPS
            character.y_dir += 1
        elif event == UPKEY_UP:
            character.y_velocity -= RUN_SPEED_PPS
            character.y_dir -= 1
        if event == DOWNKEY_DOWN:
            character.y_velocity -= RUN_SPEED_PPS
            character.y_dir -= 1
        elif event == DOWNKEY_UP:
            character.y_velocity += RUN_SPEED_PPS
            character.y_dir += 1
    @staticmethod
    def exit(character, event):
        character.face_dir = character.dir
        if character.star_count < 3:
            if event == SPACE:
                character.star()
                character.star_count += 1
        if character.sight_count == 1 and event == A:
            server.sight.draw_sight= False
            character.sight_count = 0
    @staticmethod
    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        character.x += character.x_velocity * game_framework.frame_time
        character.y += character.y_velocity * game_framework.frame_time
        character.x = clamp(25, character.x, get_canvas_width() - 25)
        character.y = clamp(25, character.y, get_canvas_height() - 25)
    @staticmethod
    def draw(character):
        if character.x_dir>0:
            character.image.clip_draw(int(character.frame) * 100, 0, 100, 100, character.x, character.y)
            character.dir = 4
        elif character.x_dir <0:
            character.image.clip_draw(int(character.frame) * 100, 100, 100, 100, character.x, character.y)
            character.dir = 5
        elif character.x_dir ==0 and character.y_dir >0:
            character.image.clip_draw(int(character.frame) * 100, 200, 100, 100, character.x, character.y)
            character.dir = 6
        elif character.x_dir ==0 and character.y_dir <0:
            character.image.clip_draw(int(character.frame) * 100, 300, 100, 100, character.x, character.y)
            character.dir = 7
        elif character.x_dir ==0 and character.y_dir ==0:
            character.image.clip_draw(int(character.frame) * 100, abs((character.face_dir))*100, 100, 100, character.x, character.y)

next_state_table = {
    WalkingState: {RIGHTKEY_UP: WalkingState, LEFTKEY_UP: WalkingState, RIGHTKEY_DOWN: WalkingState, LEFTKEY_DOWN: WalkingState,
                UPKEY_UP: WalkingState, UPKEY_DOWN: WalkingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState,
                SPACE: WalkingState, A:WalkingState}
}


class Character:
    image = None
    sound = None
    def __init__(self):
        self.x, self.y = 100, 30
        if Character.image is None:
            Character.image =load_image('character_animation.png')
        if Character.sound is None:
            Character.sound =load_wav('sound.wav')
            Character.sound.set_volume(250)
        self.frame = 0
        self.dir = 1
        self.star_count = 3
        self.sight_count = 0
        self.face_dir = 4
        self.x_dir, self.y_dir = 0, 0
        self.go = 1
        self.x_velocity, self.y_velocity =0, 0
        self.q = []
        self.cur_state = WalkingState
        self.cur_state.enter(self, None)

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y, 'dir': self.dir, 'cur_state': self.cur_state}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def star(self):
        # star = Star.star_diretion(self.dir)
        star = Star(self.x, self.y, self.dir * 0.5,self.face_dir)
        game_world.add_collision_pairs(star, None, 'star:block')
        game_world.add_object(star, 1)

    # def sight(self):
    #     sight = Sight(self)
    #     game_world.add_object(sight, 2)
    def update(self):

        self.cur_state.do(self)
        if len(self.q) > 0: # q??? ?????? ?????????
            event = self.q.pop()#???????????? ????????????
            self.cur_state.exit(self,event)  #?????? ????????? ?????????,
            self.cur_state = next_state_table[self.cur_state][event] #?????? ????????? ????????????
            self.cur_state.enter(self, event)


    def draw(self):
        self.cur_state.draw(self)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
    def add_event(self,event):
        self.q.insert(0, event)

    def handle_event(self,event): # ????????? ????????? ???????????? ???????????? ??????
        # event ??? ????????????, ????????? ?????? rd ????????? ??????
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type), event.key]
            self.add_event(key_event) #????????? ?????? ???????????? ?????? ??????
    def handle_collision(self, other, group):
        if group == 'character:block':
            # if self.x_dir>=0 and self.y_dir>0:
            #     self.x -=1
            #     self.y -=1
            # elif self.x_dir<0 and self.y_dir>0:
            #     self.x +=1
            #     self.y -=1
            # elif self.x_dir>0 and self.y_dir<0:
            #     self.x -=1
            #     self.y +=1
            # elif self.x_dir < 0 and self.y_dir < 0:
            #     self.x += 1
            #     self.y += 1
            self.x, self.y = 100, 30
            server.sight.draw_sight=False
        if group == 'character:star_item':
            self.star_count= 0

        if group == 'character:sight_item':
            self.sight_count = 1

        if group == 'character:solider':
            self.sound.play()
            self.x, self.y =100, 30
