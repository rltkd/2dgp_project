from pico2d import *
import game_framework
import play_state

image = None
logo_time= 0.0
running = True
def enter():
    global image
    image = load_image('logo.png')

def exit():
    global image
    del image
    pass

def update():
    pass


def draw():
    # fill here
    clear_canvas()
    image.draw(play_state.width//2,play_state.height//2)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_SPACE:
                game_framework.change_state(play_state)



