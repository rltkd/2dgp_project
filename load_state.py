import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import server

import play_state

from player import Character
from solider import Solider


menu = None

def enter():
    global menu
    menu = load_image('menu.png')
    hide_cursor()
    hide_lattice()

def exit():
    global menu
    del menu

def pause():
    pass

def resume():
    pass


def create_new_world():
    server.character = Character()
    game_world.add_object(server.character, 1)
    game_world.add_collision_pairs(server.character, None, 'character:solider')

    # fill here
    with open('soldier_data.json', 'r') as f:
        zombie_data_list = json.load(f)
        for data in zombie_data_list:
            solider = Solider(data['x'],data['y'])
            game_world.add_object(solider,1)
            game_world.add_collision_pairs(None,solider,'character:solider')



# def load_saved_world():
#     # fill here
#     game_world.load()
#     for o in game_world.all_objects():
#         if isinstance(o,Boy):
#             server.boy = o
#     pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            create_new_world()
            game_framework.change_state(play_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            # load_saved_world()
            game_framework.change_state(play_state)

def update():
    pass

def draw():
    clear_canvas()
    menu.draw(get_canvas_width()//2, get_canvas_height()//2)
    update_canvas()






