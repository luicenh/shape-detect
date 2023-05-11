import cv2
import numpy as np

from src import approx, sq_detect
from src import generate

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

    # 标准平行四边形
    res = cv2.matchShapes(points, pall_points, 1, 0)
    print("parall", res)
    if res < 0.01:
        return "parall", ratio
    # 标准三角形
    res = cv2.matchShapes(points, tria_points, 1, 0)
    print("tria", res)
    if res < 0.01:
        return "tria", ratio

    # 标准圆
    likeCircle = False
    res = cv2.matchShapes(points, circle_points, 1, 0)
    print("circle", res)
    if res < 0.01:
        return "circle", ratio
    if res < 0.02:
        likeCircle = True

    res_points = approx.approx(points, likeCircle)

    if len(res_points) > 8:
        return "circle", ratio

    # 标准正方形
    res = cv2.matchShapes(points, sq_points, 1, 0)
    print("sq", res)
    if res < 0.01 :
        return sq_detect.detect_sq(res_points, ratio, True), ratio


    print("length is %.2f " % len(res_points))

    if len(res_points) == 3:
        return "tria", ratio

    if len(res_points) == 4:
        return sq_detect.detect_sq(res_points, ratio, False), ratio

    return "none", ratio