'''
# Author: Li Ang

This script will show you how OOP works.

'''
from numpy.core.fromnumeric import shape, size
from numpy.lib.shape_base import tile
import cv2
import numpy as np

img = np.random.randint(100,200, size=(100,100, 3)).astype(np.uint8)

out = 9999


"""
The canvas and the core runner
"""
class MainWindow():
    def __init__(self, title='Game') -> None:
        self.runFrames = 999
        self.currentFrame = 0
        self.miliSecPerFrames = 10
        self.canvas = np.zeros(shape=(300,300,3)).astype(np.uint16) #
        self.title = title
        self.logic = GameLogic(self.canvas)

    def start(self):
        self.currentFrame = 0
        while self.currentFrame < self.runFrames:
            self.logic.render()
            cv2.imshow(self.title, self.canvas)
            cv2.waitKey(self.miliSecPerFrames)
            self.currentFrame = self.currentFrame + 1
            print(self.currentFrame)
        print('Game Finished!')


"""
2D object
pos = (x,y)   
speed = (x,y)
acc = (x,y)
"""
class BaseBullet():
    def __init__(self, pos, spd, acc) -> None:
        self.pos = pos
        self.speed = spd
        self.acc = acc
        self.radius = 3
        self.color = np.array([128, 128, 128])

class BulletA(BaseBullet):
    def __init__(self, pos, direction: np.ndarray) -> None:
        super().__init__(pos, 5*direction, np.array([0, 0]))
        self.color = np.array([128, 128, 0])

class BulletB(BaseBullet):
    def __init__(self, pos, direction: np.ndarray) -> None:
        super().__init__(pos, np.array([0, 0]), 5*direction)
        self.radius=5
        self.color = np.array([128, 0, 128])

class Emitter():
    def __init__(self, area, pos) -> None:
        self.area = area
        self.pos = pos
    def emit(self, t):
        if t == 0:
            self.area.append(BulletA(self.pos, np.random.rand(1,2)))
        if t == 1:
            self.area.append(BulletB(self.pos, np.random.random(1,2)))




class GameLogic():
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.w = self.canvas.shape[0]
        self.h = self.canvas.shape[1]
        self.bulletList = []
        self.emitter = Emitter(self.bulletList, [self.w//2, self.h//2])

    def render(self):
        self.emitter.emit(0)
        for b in self.bulletList:
            b.pos += b.speed
            b.speed += b.acc
            print(b.pos, b.radius, b.color)
            cv2.circle(self.canvas, b.pos, b.radius, b.color, 0) 



if __name__ == '__main__':
    w = MainWindow()
    w.start()

