"""
# Author: Li Ang <psw.liang@link.cuhk.edu.hk>
# Assignment2 for ELEG4701

This script will show you how OOP works.

A simple bullet emitter

* class MainWindow is to control the clock and canvas
* class BaseBullet has basic elements.
* class BulletA, BulletB is different bullet
* class Emitter will add a bullet into game logic
* class Logic shows what game will do in every frame

(I always think that intuitive visual effects
will make students more interested in coding.)

*[You have to finish all the TODOs in this assignments]*
@ 10 pts for reading this script
@ 10 pts for TODO 0
@ 40 pts for TODO 1
@ 40 pts for TODO 2

Submitting bugs and issues are welcomed; 
it will make this homework project better.
You can email me or submit an issue directly on GitHub.
I will give you extra points.
"""

from numpy.random.mtrand import random
import cv2
import numpy as np
import itertools


class MainWindow:
    """
    The canvas and the frame controller
    """
    def __init__(self, title='Game') -> None:
        self.runFrames = 999   # total frame number of this game
        self.currentFrame = 0  # to count the frame
        self.miliSecPerFrames = 10 # duration of each frame, try to change it
        self.canvas = np.zeros(shape=(300, 300, 3)).astype(np.uint8)  # the canvas, ndarray
        self.title = title      #the title name
        self.logic = GameLogic(self.canvas)

    def start(self):
        self.currentFrame = 0
        while self.currentFrame < self.runFrames:
            self.logic.render()
            # cv2.imshow(self.title,
            #            np.random.randint(0,255,size=(300,300,3)).astype(np.uint8))
            cv2.imshow(self.title, self.canvas)
            cv2.waitKey(self.miliSecPerFrames)
            self.currentFrame = self.currentFrame + 1
            print(self.currentFrame, 'f')
        print('Game Finished!')


class BaseBullet:
    """
    2D object
    pos = (x,y)
    speed = (x,y)
    acc = (x,y)
    """
    def __init__(self, pos, spd, acc) -> None:
        # you can try what will happen if you use shallow copy for pos
        # when you call astype, it will create new array for you, so it is deepcopy
        self.pos = pos.astype(np.float64)
        self.speed = spd.astype(np.float64)
        self.acc = acc.astype(np.float64)
        self.radius = 3
        self.color = np.array([128, 128, 128])
        self.linewidth = 0
        self.danmakuType = 'c'


class BulletA(BaseBullet):
    def __init__(self, pos, direction: np.ndarray) -> None:
        super().__init__(pos, 5 * direction, np.array([0, 0]))
        self.color = np.random.randint(0,255, 3).tolist() #[128, 128, 0]
        self.linewidth=-1 # filled


class BulletB(BaseBullet):
    def __init__(self, pos, direction: np.ndarray) -> None:
        super().__init__(pos, np.array([0, 0]), 5 * direction)
        self.radius = 10
        self.color = [128, 0, 128]


class BulletC(BaseBullet):
    def __init__(self, pos, direction: np.ndarray) -> None:
        super().__init__(pos, 20*np.array([direction[1], direction[0]]), direction)
        self.danmakuType = 'f'
        self.radius = 10
        self.color = [0, 128, 0]

# TODO 1: made a class BulletC, and add something you like in it (40 pts)


class Emitter:
    def __init__(self, area, pos) -> None:
        print('emitter pos', pos)
        self.area = area
        self.pos = np.array(pos, dtype=np.float)

    def emit(self, t):
        # TODO 1: do not forget to add bullet type in here
        if t == 0:
            self.area.append(BulletA(self.pos, np.random.rand(2) - 0.5))
        if t == 1:
            self.area.append(BulletB(self.pos, np.random.rand(2) - 0.5))

class Emitter2(Emitter):
    def emit(self, t):
            self.area.append(BulletC(self.pos, np.random.rand(2) - 0.5))

s = cv2.imread('star.png')

class GameLogic:
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.w = self.canvas.shape[0]
        self.h = self.canvas.shape[1]
        self.bulletList = []

        self.emitterList = [#Emitter(self.bulletList, [self.w // 2, self.h // 2]),
                            Emitter(self.bulletList, [self.w // 3, self.h // 3]),
                            Emitter2(self.bulletList, [self.w//4, self.h // 3])]

    def render(self):
        self.canvas[:] = 0
        for emitter in self.emitterList:
            # 0,3 is for skip emit if random number is 2
            emitter.emit(np.random.randint(0, 3, size=1))
        deleteList = []
        for idx, b in enumerate(self.bulletList):
            b.pos += b.speed
            b.speed += b.acc

            # here is a simple logic, if the bullet click the wall, kill it
            # TODO 2: Try to add collision detection for wall in North and South (40pts)
            # see what will happens

            if (b.pos[0] > self.w) or (b.pos[0] < 0):
                deleteList.append(idx)
                continue
            if (b.pos[1] > self.h) or (b.pos[1] < 0):
                #b.speed = -b.speed
                deleteList.append(idx)
                continue
            # print(b.pos, b.radius, b.color, len(self.bulletList))
            if b.danmakuType == 'c':
                cv2.circle(self.canvas, b.pos.astype(int), b.radius, b.color, b.linewidth)
            if b.danmakuType == 'f':
                phi = 4 * np.pi / 5
                rotations = [[[np.cos(i * phi), -np.sin(i * phi)],
                              [i * np.sin(phi), np.cos(i * phi)]] for i in range(1, 5)]
                pentagram = np.array([[[[0, -1]] + [np.dot(m, (0, -1)) for m in rotations]]], dtype=np.float)

                pentagram = np.round(pentagram * 14 + b.pos).astype(np.int)

                # 将5个顶点作为多边形顶点连线，得到五角星
                cv2.polylines(self.canvas, pentagram, True, b.color, b.linewidth)

        # You can think about the use of following codes
        # and use #(ctrl+/) to comment them, run the script and see what will happen
        idx = list(set(list(range(len(self.bulletList)))) - set(deleteList))
        self.bulletList = [self.bulletList[i] for i in idx]
        for e in self.emitterList:
            e.area = self.bulletList



if __name__ == '__main__':
    # TODO 0: run this script, and change the title to your SID, 10pts
    w = MainWindow()
    w.start()
