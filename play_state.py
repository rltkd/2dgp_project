from pico2d import *
import game_framework
import game_world

width, height = 960,780

from MAP import Block
from player import Character
from sight import Sight
from solider import Solider

soldier_xy= []
import server
# z 스프라이트 0 4 right 1 5 left 2 6 up 3 7 down

def enter():
    server.character = Character()
    server.map = Block(server.character.x,server.character.y)
    game_world.add_object(server.map,0)
    game_world.add_object(server.character,1)
    # server.soldier = Solider(200,500)
    # server.soldier1 = Soldier(400, 600)
    game_world.add_object(server.soldier,1)
    server.sight = Sight()
    if server.sight == True:
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


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
