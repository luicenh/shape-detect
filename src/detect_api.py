import copy

import cv2
import numpy as np

from src import generator, approx, rotate, detect


def detect1(e0):
    e1 = copy.deepcopy(e0)
    shape, width, height, angle = detect.detect(e1)

    if shape != "none":
        return shape, width, height, angle

    #目前需求的图形只有旋转椭圆无法在第一步检测出来，所以只在循环中识别圆
    for i in range(6):
        angle += 15

        e0 = rotate.rotate15(e0)

        et = copy.deepcopy(e0)

        shape, width, height, angle_res = detect.detect_circle(et)

        if shape != "none":
            return shape, width, height, angle + angle_res

    return "none", 0, 0, 0
