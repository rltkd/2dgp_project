from pico2d import *
import game_framework
width, height = 1024, 684

character = None
map = None
sight = True
running = True
att = None
state = None

from MAP import Map
from player import PLAYER
from player import STAR
# class Map:
#     def __init__(self):
#         self.image = load_image('stage.png')
#
#     def draw(self):
#         self.image.draw(width//2, height//2)
#

# class Star:
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
#
#
#
# class Character:
#     def __init__(self):
#         self.x, self.y, self.z = 50, 120, 4
#         self.frame = 0
#         self.dir_x, self.dir_y = 0, 0
#         self.image = load_image('character_animation.png')
#         self.sight_image = load_image('sight.png')
#         self.screen_delay = 0
#
#     def update(self):
#         global sight
#         self.frame = (self.frame + 1) % 8
#         self.x += self.dir_x*5
#         self.y += self.dir_y*5
#         if self.x > width:
#             self.x = width
#         elif self.x < 0:
#             self.x = 0
#         elif self.y > height:
#             self.y = height
#         elif self.y < 0:
#             self.y =0
#
#         if not sight:
#             self.screen_delay = (self.screen_delay+1) % 15
#             if(self.screen_delay == 0):
#                 sight = False
#
#
#
#     def draw(self):
#         if sight:
#             self.sight_image.draw(self.x, self.y-90)
#
#         self.image.clip_draw(self.frame*100, 100*self.z, 100, 100, self.x, self.y)

# z 스프라이트 0 r 4 i right 1r 5i left 2r 6i up 3r 7i down
def handle_events():
    global sight, state
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_RIGHT:
                character.z = 0
                state = 'right'
                character.dir_x += 1
            elif event.key == SDLK_LEFT:
                character.z = 1
                state = 'left'
                character.dir_x -= 1

            elif event.key == SDLK_UP:
                character.z = 2
                state = 'up'
                character.dir_y += 1
            elif event.key == SDLK_DOWN:
                character.z = 3
                state = 'down'
                character.dir_y -= 1

            elif event.key == SDLK_1:
                sight = False
            elif event.key == SDLK_SPACE:
                att.append(Star())
                att[len(att)-1].Ab(state)
                att[len(att)-1].star = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                character.z = 4
                character.dir_x -= 1
                if character.dir_y < 0:
                    character.z = 3
                elif character.dir_y > 0:
                    character.z = 2
            elif event.key == SDLK_LEFT:
                character.z = 5
                character.dir_x += 1
                if character.dir_y < 0:
                    character.z = 3
                elif character.dir_y > 0:
                    character.z = 2
            elif event.key == SDLK_UP:
                character.z = 6
                character.dir_y -= 1
                if character.dir_x < 0:
                    character.z = 1
                elif character.dir_x > 0:
                    character.z = 0
            elif event.key == SDLK_DOWN:
                character.z = 7
                character.dir_y += 1
                if character.dir_x < 0:
                    character.z = 1
                elif character.dir_x > 0:
                    character.z = 0

def enter():
    global character, map, att,  running
    character = Character()
    map = Map()
    att = []
    running = True

#게임 종료 - 객체 소멸
def exit():
    global character, map, att
    del character
    del map
    del att

#게임 월드 객체를 업데이트 - 게임 로직
def update():
    character.update()
    for i in att:
        i.update()
def draw_world():
    map.draw()
    character.draw()
    for i in att:
        i.draw()


def draw():
    # 게임 월드 렌더링
    clear_canvas()
    draw_world()
    update_canvas()
    delay(0.05)


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
