from pico2d import *
import game_framework
width, height = 1024, 684
sight = True

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

RIGHTKEY_DOWN, LEFTKEY_DOWN, UPKEY_DOWN, DOWNKEY_DOWN, RIGHTKEY_UP, LEFTKEY_UP, UPKEY_UP, DOWNKEY_UP, SPACE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UPKEY_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWNKEY_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHTKEY_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFTKEY_UP,
    (SDL_KEYUP, SDLK_UP): UPKEY_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWNKEY_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

# class STAR:
#     def __init__(self):
#         self.star_image = load_image('star.png')
#         self.state=['up', 'down', 'right', 'left']
#         self.star_x, self.star_y = character.x + 10, character.y
#         self.state = 'right'
#         self.star = False
#
#     def update(self):
#         if self.star:
#             if self.state == 'right':
#                 self.star_x += 10
#                 if self.star_x > width:
#                     self.star = False
#             elif self.state == 'left':
#                 self.star_x -= 10
#                 if self.star_x < 0:
#                     self.star = False
#             elif self.state == 'up':
#                 self.star_y += 10
#                 if self.star_y > height:
#                     self.star = False
#             elif self.state == 'down':
#                 self.star_y -= 10
#                 if self.star_y < 0:
#                     self.star = False
#
#     def draw(self):
#         if self.star:
#             self.star_image.draw(self.star_x, self.star_y)
#
#     def Ab(self, state):
#         self.state = state
# class IDLE:
#     @staticmethod
#     def enter(self, event):
#         print('enter IDLE')
#         self.z=0
#         pass
#
#     @staticmethod
#     def exit(self):
#         print('enter exit')
#         pass
#
#     @staticmethod
#     def do(self):
#         self.frame = (self.frame +1) % 8
#         pass
#
#
#     @staticmethod
#     def draw(self):
#         self.image.clip_draw(self.frame * 100, (self.idle_z+4)*100, 100, 100, self.x, self.y)
#         pass


# class RUN:
#     def enter(self, event):
#         print('enter run')
#         #self.dir 값을 결정해야 함.
#         if event == RD:
#             self.dir_x += 1
#             self.face = 'right'
#             self.z= 0
#         elif event == LD:
#             self.dir_x -= 1
#             self.face = 'left'
#             self.z = 1
#         elif event == UD:
#             self.dir_y += 1
#             self.face = 'up'
#             self.z = 2
#         elif event == DD:
#             self.dir_y -= 1
#             self.face = 'down'
#             self.z = 3
#         elif event == RU:
#             self.dir_x -= 1
#             if self.dir_y < 0:
#                 self.z = 3
#             elif self.dir_y > 0:
#                 self.z = 2
#         elif event == LU:
#             self.dir_x += 1
#             if self.dir_y < 0:
#                 self.z = 3
#             elif self.dir_y > 0:
#                 self.z = 2
#         elif event == UU:
#             self.dir_y -=1
#             if self.dir_x < 0:
#                 self.z = 1
#             elif self.dir_x > 0:
#                 self.z = 0
#         elif event == DU:
#             self.dir_y +=1
#             if self.dir_x < 0:
#                 self.z = 1
#             elif self.dir_x > 0:
#                 self.z = 0
#         pass
#
#     def exit(self):
#         print('exit.run')
#         #run을 나가서 idle로 갈 때, run의 방향을 알려줄 필요가 있다.
#         self.idle_z = self.z
#         pass
#
#     def do(self):
#         self.frame=(self.frame + 1) % 8
#         if self.face == 'right' or self.face =='left':
#             self.x += self.dir_x
#         elif self.face == 'up' or self.face =='down':
#             self.y += self.dir_y
#         self.x = clamp(0,self.x, width)
#         self.y = clamp(0,self.y, height)
#         pass
#
#     def draw(self):
#         self.image.clip_draw(self.frame * 100, self.z*100, 100, 100, self.x, self.y)
#         pass

class WalkingState:
    @staticmethod
    def enter(character, event):
        if event == RIGHTKEY_DOWN:
            character.x_velocity += RUN_SPEED_PPS
        elif event == RIGHTKEY_UP:
            character.x_velocity -= RUN_SPEED_PPS
        if event == LEFTKEY_DOWN:
            character.x_velocity -= RUN_SPEED_PPS
        elif event == LEFTKEY_UP:
            character.x_velocity += RUN_SPEED_PPS

        if event == UPKEY_DOWN:
            character.y_velocity += RUN_SPEED_PPS
        elif event == UPKEY_UP:
            character.y_velocity -= RUN_SPEED_PPS
        if event == DOWNKEY_DOWN:
            character.y_velocity -= RUN_SPEED_PPS
        elif event == DOWNKEY_UP:
            character.y_velocity += RUN_SPEED_PPS



    @staticmethod
    def exit(character, event):
        if event == SPACE:
            character.star()

    @staticmethod
    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        character.x += character.x_velocity * game_framework.frame_time
        character.y += character.y_velocity * game_framework.frame_time
        character.x = clamp(25, character.x, get_canvas_width() - 25)
        character.y = clamp(25, character.y, get_canvas_height() - 25)

    @staticmethod
    def draw(character):
        if character.x_velocity > 0:
            character.image.clip_draw(int(character.frame) * 100, 0, 100, 100, character.x, character.y)
            character.dir = 1
        elif character.x_velocity < 0:
            character.image.clip_draw(int(character.frame) * 100, 100, 100, 100, character.x, character.y)
            character.dir = -1
        else:
            # if character x_velocity == 0
            if character.y_velocity > 0 or character.y_velocity < 0:
                if character.dir == 1:
                    character.image.clip_draw(int(character.frame) * 100, 200, 100, 100, character.x, character.y)
                else:
                    character.image.clip_draw(int(character.frame) * 100, 300, 100, 100, character.x, character.y)
            else:
                # character is idle
                if character.dir == 1:
                    character.image.clip_draw(int(character.frame) * 100, 300, 100, 100, character.x, character.y)
                else:
                    character.image.clip_draw(int(character.frame) * 100, 200, 100, 100, character.x, character.y)


next_state_table = {
    WalkingState: {RIGHTKEY_UP: WalkingState, LEFTKEY_UP: WalkingState, RIGHTKEY_DOWN: WalkingState, LEFTKEY_DOWN: WalkingState,
                UPKEY_UP: WalkingState, UPKEY_DOWN: WalkingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState,
                SPACE: WalkingState}
}


class Character:
    image = None
    def __init__(self):
        self.x, self.y = 50, 90
        # self.face = ['up', 'down', 'right', 'left']
        if Character.image is None:
            Character.image =load_image('character_animation.png')
        self.frame = 0
        self.dir = 1
        self.x_velocity, self.y_velocity = 0 ,0
        self.q = []
        self.cur_state = WalkingState
        self.cur_state.enter(self, None)

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y, 'dir': self.dir, 'cur_state': self.cur_state}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)
    def update(self):

        self.cur_state.do(self)
        if len(self.q) > 0: # q에 뭔가 있다면
            event = self.q.pop()#이벤트를 가져오고
            self.cur_state.exit(self,event)  #현재 상태를 나가고,
            self.cur_state = next_state_table[self.cur_state][event] #다음 상태를 계산하기
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self,event):
        self.q.insert(0, event)

    def handle_event(self,event): # 소년이 스스로 이벤트를 처리할수 있게
        # event 는 키이벤트, 이것을 내부 rd 등으로 변환
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type), event.key]
            self.add_event(key_event) #변환된 내부 이벤트를 큐에 추가

