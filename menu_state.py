import pico2d
import play_state
import game_framework

width, height = 960, 780

from pico2d import *

image = None

def enter():
    global image
    image = load_image('title.png')

def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(play_state)

def draw():
    clear_canvas()
    image.draw(width//2,height//2)
    update_canvas()

def update():
    pass