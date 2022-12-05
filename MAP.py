from pico2d import *
width, height = 960,780
tilesize = 60
rows= 16
cols =13
#60,60
map_data = [

            [1, 2, 1, 0, 0, 5, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [4, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
            [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 5, 0, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 5, 0, 1, 1, 1],
            [0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 3],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],

            ]
class Wall:
    image = None
    def __init__(self,y,x):
        if Wall.image == None:
            Wall.image = load_image('block1.png')
        self.x, self.y = (x * 60)+ 30 , (y * 60) + 30

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
    def update(self):
        pass
    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30
    def handle_collision(self,other,massage):
        #점프에 대한 충돌 처리
        pass
class Empty:

    def __init__(self,y,x):
        self.x, self.y = (x * 60) + 30 , (y * 60) + 30
    def get_pos(self):
        return self.x, self.y
    def draw(self):
        pass
    def update(self):
        pass
    def get_bb(self,x,y):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30
    def handle_collision(self,other,massage):
        #점프에 대한 충돌 처리
        pass
# class Background:
#     def __init__(self):
#         self.block_image = load_image('block1.png')
#         self.road_image = load_image('block2.png')
#         for cols in range(len(map_data)):
#             for rows in range(len(map_data[cols])):
#                 pass
#                 if map_data[cols][rows] == 1:
#                     self.x, self.y = cols*16, rows*13
#                     # self.tile = 1
#         #
#         #         if map_data[cols][rows] ==0:
#         #             self.x, self. y = cols, rows
#         #             self.tile = 0
#     def draw(self):
#         self.block_image.draw(self.x, self.y)
#         # for y in range(0,rows):
#         #     for x in range(0,cols):
#         #         if(map_data[cols][rows] == 1 ):
#         #             self.block_image.draw(x,y)
#         #             # draw_rectangle(*self.get_bb(x,y) )
#         #         elif (map_data[cols][rows] == 0 ):
#         #             self.road_image.draw(x,y)
#         #             # draw_rectangle(*self.get_bb(x, y))
#
#
#     def update(self):
#         pass
#     def get_bb(self,x,y):
#         return self.x - 30, self.y - 30, self.x + 30, self.y + 30
#     def handle_collision(self,other,massage):
#         #점프에 대한 충돌 처리
#         pass

