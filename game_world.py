#layer 0: Background Objects
#layer 1: foreground objects
import pickle
objects = [[],[],[]]
collision_group = dict()

def add_object(o,depth):
    objects[depth].append(o)

def add_objects(ol,depth):
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            remove_collision_object(o)
            layer.remove(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')

def all_objects():
    for layer in objects:
        for o in layer:
            yield o

def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()
    collision_group.clear()


def add_collision_pairs(a, b, group):

    if group not in collision_group:
        # print('Add new group ', group)
        collision_group[group] = [ [], [] ] # list of list : list pair

    if a:
        if type(a) is list:
            collision_group[group][1] += a
        else:
            collision_group[group][1].append(a)

    if b:
        if type(b) is list:
            collision_group[group][0] += b
        else:
            collision_group[group][0].append(b)

    # print(collision_group)


def all_collision_pairs():
    for group, pairs in collision_group.items():
        for a in pairs[0]:
            for b in pairs[1]:
                yield a, b, group


def remove_collision_object(o):
    for pairs in collision_group.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)







def save():
    # fill here
    game = [objects,collision_group]
    with open('game.sav','wb') as f:
        pickle.dump(game, f)
    pass

def load():
    # fill here
    global objects,collision_group
    with open('game.sav','rb') as f:
        game = pickle.load(f)
        objects,collision_group =game[0],game[1]
    pass