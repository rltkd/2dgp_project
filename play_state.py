import random
import json
import os

from pico2d import *
import game_framework
import game_world
import item
from player import Character
import solider
import server
import MAP
import sight
import load_state
def gen_map():
    for cols in range(13):
        for rows in range(16):
            if MAP.map_data[cols][rows] == 1:
                server.map.append(MAP.Wall(cols, rows))

            if MAP.map_data[cols][rows] == 2:
                server.character = Character()
            if MAP.map_data[cols][rows] == 4:
                empty = MAP.Empty(cols, rows)
                server.item.append(item.Star_Item(*empty.get_pos()))
            if MAP.map_data[cols][rows] ==5:
                empty = MAP.Empty(cols, rows)
                server.soldier.append(solider.Solider(*empty.get_pos()))
            if MAP.map_data[cols][rows] == 6:
                empty = MAP.Empty(cols, rows)
                server.item.append(item.Sight_Item(*empty.get_pos()))
def enter():
    gen_map()
    background = MAP.Background()
    server.sight = sight.Sight()
    # server.character = Character()
    game_world.add_object(background, 0)
    game_world.add_objects(server.map, 1)
    game_world.add_objects(server.soldier, 1)
    game_world.add_object(server.character, 1)
    game_world.add_objects(server.item,1)
    game_world.add_object(server.sight,2)

    game_world.add_collision_pairs(server.character, server.item, 'character:star_item')
    game_world.add_collision_pairs(server.character, server.item, 'character:sight_item')
    game_world.add_collision_pairs(server.character, server.soldier, 'character:solider')
    game_world.add_collision_pairs(server.character, server.map, 'character:block')
    game_world.add_collision_pairs(server.soldier, server.map, 'solider:block')
    game_world.add_collision_pairs(None, server.map, 'star:block')

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
            # game_framework.change_state(load_state)
        else:
            server.character.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            # print('COLLISION ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()



def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


