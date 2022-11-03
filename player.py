from pico2d import *
width, height = 1024, 684
sight = True
RD, LD, RU, LU,UD,UU,DD,DU,SD, SU = range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU,
    (SDL_KEYDOWN,SDLK_SPACE) :SD,
    (SDL_KEYUP,SDLK_SPACE) : SU
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
class IDLE:
    @staticmethod
    def enter(self, event):
        print('enter IDLE')
        self.dir_x = 1
        self.dir_y = 0
        pass

    @staticmethod
    def exit(self):
        print('enter exit')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame +1) % 8
        pass


    @staticmethod
    def draw(self):
        if self.dir_x == 1:#오른쪽을 바라보는 IDLE
            self.image.clip_draw(self.frame * 100, 4*100, 100, 100, self.x, self.y)
        elif self.dir_x == -1:
            self.image.clip_draw(self.frame * 100, 5*100, 100, 100, self.x, self.y)
        elif self.dir_y == 1:
            self.image.clip_draw(self.frame * 100, 6*100, 100, 100, self.x, self.y)
        elif self.dir_y == -1:
            self.image.clip_draw(self.frame * 100, 7*100, 100, 100, self.x, self.y)
        pass


class RUN:
    def enter(self, event):
        print('enter run')
        #self.dir 값을 결정해야 함.
        if event == RD: self.dir_x = 1
        elif event == LD:self.dir_x = -1
        elif event == RU: self.dir_x = -1
        elif event == LU: self.dir_x = 1
        elif event == UU: self.dir_y = -1
        elif event == UD: self.dir_y = 1
        elif event == DD: self.dir_y = -1
        elif event == DU: self.dir_y = +1

        pass

    def exit(self):
        print('enter.run')
        #run을 나가서 idle로 갈 때, run의 방향을 알려줄 필요가 있다.
        pass

    def do(self):
        self.frame=(self.frame + 1) % 8
        self.x += self.dir_x
        self.x = clamp(0,self.x, width)
        self.y = clamp(0,self.x, height)
        pass

    def draw(self):
        if self.dir_x == 1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir_x == -1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        elif self.dir_y == 1:
            self.image.clip_draw(self.frame * 100, 2*100, 100, 100, self.x, self.y)
        elif self.dir_y == -1:
            self.image.clip_draw(self.frame * 100, 3*100, 100, 100, self.x, self.y)
        pass

next_state = {
    IDLE: {RU: RUN, LU:RUN, RD:RUN, LD:RUN,UD:RUN,DD:RUN,UU:RUN,DU:RUN},
    RUN: {RU: IDLE, LU:IDLE, RD:IDLE, LD:IDLE,UD:IDLE, UU:IDLE,DD:IDLE, DU:IDLE},
}

class Character:
    def __init__(self):
        self.x, self.y = 50, 90
        self.state=['up', 'down', 'right', 'left']
        self.frame=0
        self.dir_x,self.dir_y= 1, 0
        self.image= load_image('character_animation.png')
        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):

        self.cur_state.do(self)

        if self.q: # q에 뭔가 있다면
            event = self.q.pop()#이벤트를 가져오고
            self.cur_state.exit(self) #현재 상태를 나가고,
            self.cur_state = next_state[self.cur_state][event] #다음 상태를 계산하기
            self.cur_state.enter(self, event)

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)


    def draw(self):
        self.cur_state.draw(self)

    def add_event(self,event):
        self.q.insert(0, event)

    def handle_event(self,event): # 소년이 스스로 이벤트를 처리할수 있게
        # event 는 키이벤트, 이것을 내부 rd 등으로 변환
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type), event.key]
            self.add_event(key_event) #변환된 내부 이벤트를 큐에 추가

