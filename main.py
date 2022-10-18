import pico2d
import play_state
import logo_state
import game_framework
# state = logo_state #모듈을 변수로 취급

width, height = 1024, 684
pico2d.open_canvas(width, height)

# states = [ play_state]
# #
# for state in states:
#     state.enter()
#     # game main loop code
#     while state.running:
#         state.handle_events()
#         state.update()
#         state.draw()
#     state.exit()

game_framework.run(play_state)
   # finalization code
pico2d.close_canvas()