from pico2d import *
import game_framework
class Map:
    def __init__(self):
        self.image = load_image('state.png')

    def draw(self):
        self.image.draw(400,300)


map = None
running = True

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

def enter():
    global map, running
    # boy = Boy()
    map = Map()
    running = True

#게임 종료 - 객체 소멸
def exit():
    global map
    del map

#게임 월드 객체를 업데이트 - 게임 로직
def update():
    pass

def draw_world():
    map.draw()

def draw():
    # 게임 월드 렌더링
    clear_canvas()
    draw_world()
    update_canvas()


def pause():
    pass

def resume():
    pass
