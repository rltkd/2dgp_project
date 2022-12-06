import pico2d
import play_state
import menu_state
import game_framework

width, height = 960, 780
pico2d.open_canvas(width, height)


game_framework.run(menu_state)
   # finalization code
pico2d.close_canvas()