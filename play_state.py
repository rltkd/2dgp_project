from pico2d import *
import game_framework
class Map:
    def __init__(self):
        self.image = load_image('stage.png')

    def draw(self):
        width, height = 1024, 684
        self.image.draw(width//2, height//2)

class Character:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('spritesheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x += self.dir * 1
        if self.x > 800:
            self.dir = -1
            self.x = 800
        elif self.x < 0:
            self.dir = 1
            self.x = 0

    def draw(self):
        # if self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

character = None
map = None
running = True

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

def enter():
    global character, map, running
    character = Character()
    map = Map()
    running = True

#게임 종료 - 객체 소멸
def exit():
    global character, map
    del character
    del map

#게임 월드 객체를 업데이트 - 게임 로직
def update():
    character.update()
def draw_world():
    map.draw()
    character.draw()


def draw():
    # 게임 월드 렌더링
    clear_canvas()
    draw_world()
    update_canvas()


def pause():
    pass

def resume():
    pass

# def test_self():
#     import sys
#     this_module = sys.modules['__main__']
#     pico2d.open_canvas()
#     game_framework.run(this_module)
#     pico2d.close_canvas()
#
#
# if __name__ == '__main__':#만약 단독 실행 상태이면,
#     test_self()
