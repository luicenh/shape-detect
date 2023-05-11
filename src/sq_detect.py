import math


def detect_sq(points, f):
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

    if -15 < x1 - x3 < 15 or -15 < y1 - y3 < 15:
        return "diamond"

    if f:
        return "sq"

    if sum180(a1, a2) & sum180(a2, a3):
        if is90(a1):
            return "sq"
        else:
            return "parall"

    if (sum180(a1, a2) & sum180(a3, a4)) | (sum180(a1, a4) & sum180(a2, a3)):
        return "ladder"

    return "none"

def sum180(a1, a2) :
    return 160 <= a1 + a2 <= 200

def is90(a1) :
    return 80 < a1 < 100