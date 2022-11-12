from pico2d import *
from Star import Star
from sight import Sight
import game_framework
import game_world
width, height = 1024, 684
blind = True

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
            print('star')
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
                    character.image.clip_draw(int(character.frame) * 100, 400, 100, 100, character.x, character.y)
                else:
                    character.image.clip_draw(int(character.frame) * 100, 500, 100, 100, character.x, character.y)


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
        self.x_velocity, self.y_velocity = 0, 0
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
        print('star')
        star = Star(self.x, self.y, self.dir * RUN_SPEED_PPS * 10)
        game_world.add_object(star, 1)
    def sight(self):
        sight = Sight(self.x, self.y)
        game_world.add_object(sight, 2)
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

