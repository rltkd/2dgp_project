from pico2d import *
import game_framework
import game_world

width, height = 1024, 684

from MAP import Map
from player import Character
from sight import Sight

import server
# z 스프라이트 0 4 right 1 5 left 2 6 up 3 7 down

def enter():
    server.character = Character()
    server.map = Map()
    game_world.add_object(server.map,0)
    game_world.add_object(server.character,1)
    server.sight = Sight()
    game_world.add_object(server.sight,2)

#게임 종료 - 객체 소멸
def exit():
    game_world.clear()
#게임 월드 객체를 업데이트 - 게임 로직
def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    # 게임 월드 렌더링
    clear_canvas()
    draw_world()
    update_canvas()
    delay(0.001)


def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
            game_framework.quit()
        else:
            server.character.handle_event(event) #소년한테 이벤트 처리하도록 넘겨준다.

def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
