import cv2
import numpy as np

from src import approx, points_analysis, rotate
from src import generator

#主方法
def detect(e0) :
    rotate_angle = 0
    # 归一化e8
    ratio, width, height = generator.format(e0)
    print("ratio is %.2f " % ratio)

    # 获取标准图形
    circle = generator.generateCircle()
    sq = generator.generateSq()
    pall = generator.generatePall()
    tria = generator.generateTriangle()

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
        return "parall", width, height, rotate_angle
    # 标准三角形
    res = cv2.matchShapes(points, tria_points, 1, 0)
    print("tria", res)
    if res < 0.01:
        return "tria", width, height, rotate_angle

    # 标准圆
    likeCircle = False
    res = cv2.matchShapes(points, circle_points, 1, 0)
    print("circle", res)
    if res < 0.01:
        return "circle", width, height, rotate_angle
    if res < 0.02:
        likeCircle = True

    res_points = approx.approx(points, likeCircle)

    for point in res_points:
        point[0] = point[0] * ratio

    if len(res_points) > 8:
        return "circle", width, height, rotate_angle

    # 标准正方形
    res = cv2.matchShapes(points, sq_points, 1, 0)
    print("sq", res)
    if res < 0.01 :
        shape, _ = points_analysis.detect_quadrangle(res_points, ratio, True)
        return shape, width, height, rotate_angle

    #以上命中都不需要考虑旋转的情况，但下面的命中需要处理旋转Rotate
    print("length is %.2f " % len(res_points))

    if len(res_points) == 3:
        # width, height, rotate_angle
        print("====")
        print(res_points)
        generator.show(res_points)
        width, height, rotate_angle = points_analysis.detect_triangle(res_points)
        return "tria", width, height, rotate_angle

    if len(res_points) == 4:
        shape, is_rotate = points_analysis.detect_quadrangle(res_points, ratio, False)

        if (shape != "none") & (is_rotate) :
            width, height, rotate_angle = rotate.rotate_quadrangle(shape, res_points)
        return shape, width, height, rotate_angle

    return "none", width, height, rotate_angle


def detect_circle(e0) :
    rotate_angle = 0
    # 归一化e8
    ratio, width, height = generator.format(e0)
    print("ratio is %.2f " % ratio)

    # 获取标准图形
    circle = generator.generateCircle()

    # np.array
    points = np.array(e0, np.float32)
    circle_points = np.array(circle, np.float32)

    # 标准圆
    likeCircle = False
    res = cv2.matchShapes(points, circle_points, 1, 0)
    print("circle", res)
    if res < 0.01:
        return "circle", width, height, rotate_angle
    if res < 0.02:
        likeCircle = True

    res_points = approx.approx(points, likeCircle)

    if len(res_points) > 8:
        return "circle", width, height, rotate_angle

    return "none", width, height, rotate_angle