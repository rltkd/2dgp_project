from pico2d import *
import game_framework
width, height = 1024, 684

character = None
map = None
sight = True
running = True

class Map:
    def __init__(self):
        self.image = load_image('stage.png')

    def draw(self):
        self.image.draw(width//2, height//2)


# class Sight:
#     def __init__(self):
#         self.back_x = width//5
#         self.back_y = height//5
#         self.image = load_image('back.png')
#
#     def update(self):
#         pass
#     def draw(self):
#         self.image.draw(self.back_x, self.back_y)
class Character:
    def __init__(self):
        self.x, self.y, self.z = 50, 120, 4
        self.frame = 0
        self.dir_x, self.dir_y = 0, 0
        self.image = load_image('character_animation.png')
        self.sight_image = load_image('sight.png')
        self.screen_delay=0
    def update(self):
        global sight
        self.frame = (self.frame + 1) % 8
        self.x += self.dir_x*5
        self.y += self.dir_y*5
        if self.x > width:
            self.x = width
        elif self.x < 0:
            self.x = 0
        elif self.y > height:
            self.y = height
        elif self.y < 0:
            self.y =0

        # if not sight:
        #     self.screen_delay = (self.screen_delay+1) % 15
        #     if(self.screen_delay == 0):
        #         sight = True
    def draw(self):
        if sight:
            self.sight_image.draw(self.x, self.y-90)

        self.image.clip_draw(self.frame*100, 100*self.z, 100, 100, self.x, self.y)





def handle_events():
    global running, sight
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            if event.key == SDLK_RIGHT:
                character.z=0
                character.dir_x += 1

            elif event.key == SDLK_LEFT:
                character.z = 1
                character.dir_x -= 1

            elif event.key == SDLK_UP:
                character.z = 2
                character.dir_y += 1

            elif event.key == SDLK_DOWN:
                character.z = 3
                character.dir_y -= 1

            elif event. key == SDLK_1:
                sight = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                character.z = 4
                character.dir_x -= 1
            elif event.key == SDLK_LEFT:
                character.z = 5
                character.dir_x += 1
            elif event.key == SDLK_UP:
                character.z = 6
                character.dir_y -= 1
            elif event.key == SDLK_DOWN:
                character.z = 7
                character.dir_y += 1

def enter():
    global character, map,  running
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
