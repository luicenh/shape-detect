import os

import matplotlib
import numpy as np
import cv2
from matplotlib import pyplot as plt

import approx
import generate
import match

#主方法
def detect(e0) :
    # 归一化e8
    ratio = generate.format(e0)
    print("ratio is %.2f " % ratio)

    # 获取标准图形
    circle = generate.generateCircle()
    sq = generate.generateSq()
    pall = generate.generatePall()
    tria = generate.generateTriangle()

    # np.array
    points = np.array(e0, np.float32)
    sq_points = np.array(sq, np.float32)
    pall_points = np.array(pall, np.float32)
    circle_points = np.array(circle, np.float32)
    tria_points = np.array(tria, np.float32)

    # 分别比较
    res = match.match(points, sq_points, "sq")
    if res < 0.01 :
        return "sq", ratio
    res = match.match(points, pall_points, "parall")
    if res < 0.01 :
        return "parall", ratio
    res = match.match(points, circle_points, "circle")
    if res < 0.01 :
        return "circle", ratio
    res = match.match(points, tria_points, "tria")
    if res < 0.01 :
        return "tria", ratio

    res_points = approx.approx(points)

    if len(res_points) == 3:
        return "tria", ratio

    if len(res_points) == 4:
        return shape, ratio

    return "none", ratio