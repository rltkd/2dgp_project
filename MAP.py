from pico2d import *
width, height = 960,780

#60,60
map_data = [[1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
            [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
            ]

class Block:
    def __init__(self, x, y):
        # self.image = load_image('stage.png')
        rows = 16
        cols = 13
        self.x, self.y = x, y

        for cols in range(len(map_data)):
            for rows in range(len(map_data[cols])):
                pass

                if map_data[cols][rows] == 1:
                    self.image = load_image('block1.png')
                    self.x = 30
                    self.y = 30
                if map_data[cols][rows] ==0:
                    pass



    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        pass

