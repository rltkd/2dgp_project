import pico2d
import play_state
import logo_state
import game_framework
# state = logo_state #모듈을 변수로 취급

width, height = 1000, 800
pico2d.open_canvas(width, height)


game_framework.run(play_state)
   # finalization code
pico2d.close_canvas()