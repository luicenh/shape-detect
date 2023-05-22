import cv2
import numpy as np

from src import approx, points_analysis, rotate
from src import generator


# 主方法
def detect(e0):
    extra = {}
    # generator.show(e0)
    rotate_angle = 0
    # 归一化e8
    ratio, width, height, center_point = generator.format1(e0)
    r2 = height / 100
    # print("ratio is %.2f " % ratio)

    # 获取标准图形
    circle = generator.generate_circle()
    sq = generator.generate_sq()
    # pall = generator.generate_pall()
    # tria = generator.generate_triangle()

    # np.array
    points = np.array(e0, np.float32)
    sq_points = np.array(sq, np.float32)
    # pall_points = np.array(pall, np.float32)
    circle_points = np.array(circle, np.float32)
    # tria_points = np.array(tria, np.float32)

    # 标准平行四边形
    # res = cv2.matchShapes(points, pall_points, 1, 0)
    # print("parall", res)
    # if res < 0.01:
    #     return "parall", width, height, rotate_angle, extra
    # 标准三角形
    # res = cv2.matchShapes(points, tria_points, 1, 0)
    # print("tria", res)
    # if res < 0.01:
    #     return "tria", width, height, rotate_angle, extra

    # 标准圆
    like_circle = False
    res = cv2.matchShapes(points, circle_points, 1, 0)
    # print("circle", res)
    if res < 0.01:
        return "circle", width, height, rotate_angle, extra, center_point
    if res < 0.02:
        like_circle = True

    res_points = approx.approx(points, like_circle)
    generator.show(res_points)
    if len(res_points) > 8:
        return "circle", width, height, rotate_angle, extra, center_point

    for point in res_points:
        point[0] = point[0] * ratio * r2
        point[1] = point[1] * r2

    # 标准正方形
    res = cv2.matchShapes(points, sq_points, 1, 0)
    # print("sq", res)
    if res < 0.01:
        shape, is_rotate, extra = points_analysis.detect_quadrangle(res_points, ratio, r2, True)
        if (shape != "none") & (is_rotate):
            width, height, rotate_angle, extra = rotate.rotate_quadrangle(shape, res_points)
        return shape, width, height, rotate_angle, extra, center_point

    # 以上命中都不需要考虑旋转的情况，但下面的命中需要处理旋转Rotate
    print("length is %.2f " % len(res_points))

    if len(res_points) == 3:
        # width, height, rotate_angle
        # generator.show(res_points)
        width, height, rotate_angle = points_analysis.detect_triangle(res_points)
        return "tria", width, height, rotate_angle, extra, center_point

    if len(res_points) == 4:
        shape, is_rotate, extra = points_analysis.detect_quadrangle(res_points, ratio, r2, False)

        if (shape != "none") & (is_rotate):
            width, height, rotate_angle, extra = rotate.rotate_quadrangle(shape, res_points)
        return shape, width, height, rotate_angle, extra, center_point

    return "none", width, height, rotate_angle, extra, center_point


def detect_circle(e0):
    rotate_angle = 0
    # 归一化e8
    ratio, width, height, center_point = generator.format1(e0)
    # print("ratio is %.2f " % ratio)

    # 获取标准图形
    circle = generator.generate_circle()

    # np.array
    points = np.array(e0, np.float32)
    circle_points = np.array(circle, np.float32)

    # 标准圆
    like_circle = False
    res = cv2.matchShapes(points, circle_points, 1, 0)
    # print("circle", res)
    if res < 0.01:
        return "circle", width, height, rotate_angle
    if res < 0.02:
        like_circle = True

    res_points = approx.approx(points, like_circle)

    if len(res_points) > 8:
        return "circle", width, height, rotate_angle

    return "none", width, height, rotate_angle
