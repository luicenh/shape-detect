import math

from src import points_analysis


def get_center(e0):
    max_x = None
    min_x = None
    max_y = None
    min_y = None

    for point in e0:
        x, y = point
        if max_x is None or x > max_x:
            max_x = x
        if min_x is None or x < min_x:
            min_x = x
        if max_y is None or y > max_y:
            max_y = y
        if min_y is None or y < min_y:
            min_y = y

    return ((max_x + min_x) / 2, (max_y + min_y) / 2)


def get_side(e0):
    max_x = None
    min_x = None
    max_y = None
    min_y = None

    for point in e0:
        x, y = point
        if max_x is None or x > max_x:
            max_x = x
        if min_x is None or x < min_x:
            min_x = x
        if max_y is None or y > max_y:
            max_y = y
        if min_y is None or y < min_y:
            min_y = y

    return max_x - min_x, max_y - min_y


def rotate15(M):
    p = get_center(M)
    theta = math.radians(15)  # 逆时针旋转角度（15度对应的弧度）
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    M_prime = [[x - p[0], y - p[1]] for x, y in M]  # 得到新矩阵M'
    M_doubleprime = [[cos_theta * x - sin_theta * y, sin_theta * x + cos_theta * y] for x, y in M_prime]  # 得到旋转后的新矩阵M''
    M_rotated = [[x + p[0], y + p[1]] for x, y in M_doubleprime]  # 得到旋转后的矩阵M

    return M_rotated


def check_rotate(points):
    x1, y1 = points[0][0], points[0][1]
    x2, y2 = points[1][0], points[1][1]
    x3, y3 = points[2][0], points[2][1]
    x4, y4 = points[3][0], points[3][1]

    return (is_parallel(y2 - y1, x2 - x1) & is_parallel(y4 - y3, x4 - x3)) or (
                is_parallel(y3 - y2, x3 - x2) & is_parallel(y1 - y4, x1 - x4))


def is_parallel(y, x):
    if x == 0:
        return False

    return -0.26795 < y / x < 0.26795

# 检测是否为标准形状，梯形上边比下边短，平行四边形左下角为锐角（可不判断）
def check_shape(shape, points):
    if shape == "ladder":
        sorted_points = sorted(points, key=lambda x: x[1])

        # 取出前两个坐标和后两个坐标
        low_points = sorted_points[:2]
        high_points = sorted_points[-2:]

        # 计算y值更高的两个点的y值之差以及y值更低的两个点的y值之差
        diff_high = high_points[1][0] - high_points[0][0]
        diff_low = low_points[1][0] - low_points[0][0]

        return abs(diff_low) > abs(diff_high)

    if shape == "parall":
        return True
        # sorted_points = sorted(points, key=lambda x: x[1])
        #
        # # 取出前两个坐标和后两个坐标
        # low_points = sorted_points[:2]
        # high_points = sorted_points[-2:]
        #
        # # 计算y值更高的两个点的y值之差以及y值更低的两个点的y值之差
        # diff_high = high_points[1][0] + high_points[0][0]
        # diff_low = low_points[1][0] + low_points[0][0]
        #
        # return diff_low < diff_high

    return True


def rotate_quadrangle(shape, points):
    extra = {}
    angle = 0
    for i in range(24):
        angle += 15
        points = rotate15(points)
        # generator.show(points)
        if check_rotate(points) & check_shape(shape, points):
            if shape == "parall":
                extra["bl_angle"] = points_analysis.cal_left_bottom_angle(points)
            width, height = get_side(points)
            return width, height, angle, extra
    return 0, 0, 0, extra
