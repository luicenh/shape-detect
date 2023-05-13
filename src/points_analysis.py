import math
from src import rotate

def detect_quadrangle(points, ratio, f):
    print(points)

    x1, y1 = points[0][0], points[0][1]
    x2, y2 = points[1][0], points[1][1]
    x3, y3 = points[2][0], points[2][1]
    x4, y4 = points[3][0], points[3][1]

    v1 = (x2 - x1, y2 - y1)
    v2 = (x3 - x2, y3 - y2)
    v3 = (x4 - x3, y4 - y3)
    v4 = (x1 - x4, y1 - y4)

    # 计算夹角
    a1 = math.acos(
        (v1[0] * v2[0] + v1[1] * v2[1]) / (math.sqrt(v1[0] ** 2 + v1[1] ** 2) * math.sqrt(v2[0] ** 2 + v2[1] ** 2)))
    a2 = math.acos(
        (v2[0] * v3[0] + v2[1] * v3[1]) / (math.sqrt(v2[0] ** 2 + v2[1] ** 2) * math.sqrt(v3[0] ** 2 + v3[1] ** 2)))
    a3 = math.acos(
        (v3[0] * v4[0] + v3[1] * v4[1]) / (math.sqrt(v3[0] ** 2 + v3[1] ** 2) * math.sqrt(v4[0] ** 2 + v4[1] ** 2)))
    a4 = math.acos(
        (v4[0] * v1[0] + v4[1] * v1[1]) / (math.sqrt(v4[0] ** 2 + v4[1] ** 2) * math.sqrt(v1[0] ** 2 + v1[1] ** 2)))

    # 将弧度转换为角度制，并确保结果在 0 到 360 度之间
    a1 = math.degrees(a1) % 360
    a2 = math.degrees(a2) % 360
    a3 = math.degrees(a3) % 360
    a4 = math.degrees(a4) % 360
    print(a1, a2, a3, a4)

    if (-15 * ratio < x1 - x3 < 15 * ratio or -15 < y1 - y3 < 15) & (
            -15 * ratio < x2 - x4 < 15 * ratio or -15 < y2 - y4 < 15) & sum180(a1, a2) & sum180(a2, a3):
        return "diamond", False

    if f:
        return "sq", False

    is_rotate = not rotate.checkRotate(points)

    if sum180(a1, a2) & sum180(a2, a3):
        if is90(a1):
            return "sq", is_rotate
        else:
            return "parall", is_rotate

    if (sum180(a1, a2) & sum180(a3, a4)) | (sum180(a1, a4) & sum180(a2, a3)):
        return "ladder", is_rotate

    return "none", is_rotate


def sum180(a1, a2):
    return 160 <= a1 + a2 <= 200


def is90(a1):
    return 80 < a1 < 100

def detect_triangle(points):
    print(points)

    x1, y1 = points[0][0], points[0][1]
    x2, y2 = points[1][0], points[1][1]
    x3, y3 = points[2][0], points[2][1]

    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    # 计算三个角的度数
    cos_theta1 = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    cos_theta2 = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
    cos_theta3 = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    a1 = math.degrees(math.acos(cos_theta1))
    a2 = math.degrees(math.acos(cos_theta2))
    a3 = math.degrees(math.acos(cos_theta3))
    #依次p3, p1, p2
    print(a1, a2, a3)

    diff1 = abs(a1 - a2)
    diff2 = abs(a1 - a3)
    diff3 = abs(a2 - a3)

    # 找到两个差值中的最小值
    #依次p2, p1, p3
    min_diff = min(diff1, diff2, diff3)

    width, height, angle = 0, 0, 0
    # 点1 点3
    if min_diff == diff1:
        width, height, angle = cal_triangle(points[0], points[2], points[1])

    # 点2 点3
    if min_diff == diff2:
        width, height, angle = cal_triangle(points[2], points[1], points[0])

    # 点1 点2
    if min_diff == diff3:
        width, height, angle = cal_triangle(points[0], points[1], points[2])

    return width, height, angle

def cal_triangle(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # 计算前两个点之间的距离
    width = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # 计算第三个点到(x1, y1)和(x2, y2)所对应的直线距离
    A, B, C = y2 - y1, x1 - x2, x2 * y1 - x1 * y2
    height = abs(A * x3 + B * y3 + C) / math.sqrt(A ** 2 + B ** 2)

    #中点坐标
    x4 = (x1 + x2 ) / 2
    y4 = (y1 + y2 ) / 2

    # 计算连线斜率
    k = (y3 - y4) / (x3 - x4)

    # 计算连线与水平方向夹角（单位为弧度）
    theta = math.atan(k)

    # 将夹角转换为极坐标系下的角度值
    theta_degrees = (math.pi / 2 - theta) * 180 / math.pi

    # 如果角度值小于0，则加上360度
    if theta_degrees < 0:
        theta_degrees += 360

    #夹角大于180度
    if x4 > x3:
        theta_degrees += 180

    return width, height, theta_degrees
