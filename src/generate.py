import math
import matplotlib.pyplot as plt
import numpy as np

#用于生成标准图形，格式化输入，输出图片等

def generateSq():
    x_coords = np.linspace(0, 100, 25)
    y_coords = np.linspace(0, 0, 25)

    sq = np.column_stack((x_coords, y_coords)).tolist()

    x_coords = np.linspace(100, 100, 25)
    y_coords = np.linspace(0, 100, 25)

    sq = sq + np.column_stack((x_coords, y_coords)).tolist()

    x_coords = np.linspace(100, 0, 25)
    y_coords = np.linspace(100, 100, 25)

    sq = sq + np.column_stack((x_coords, y_coords)).tolist()

    x_coords = np.linspace(0, 0, 25)
    y_coords = np.linspace(100, 0, 25)

    sq = sq + np.column_stack((x_coords, y_coords)).tolist()
    return sq

def generatePall():
    x_coords = np.linspace(0, 50, 25)
    y_coords = np.linspace(100, 0, 25)

    pall = np.column_stack((x_coords, y_coords)).tolist()

    x_coords = np.linspace(50, 100, 25)
    y_coords = np.linspace(0, 0, 25)

    pall = pall + np.column_stack((x_coords, y_coords)).tolist()

    x_coords = np.linspace(100, 50, 25)
    y_coords = np.linspace(0, 100, 25)

    pall = pall + np.column_stack((x_coords, y_coords)).tolist()

    x_coords = np.linspace(50, 0, 25)
    y_coords = np.linspace(100, 100, 25)

    pall = pall + np.column_stack((x_coords, y_coords)).tolist()
    return pall


def generateCircle() :
    center = (50, 50)
    radius = 50

    # 生成100个均匀分布在标准圆上的点
    circle = []
    for i in range(101):
        angle = 2 * math.pi * i / 100
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        circle.append((x, y))

    return circle

def generateTriangle():
    x_coords = np.linspace(0, 100, 25)
    y_coords = np.linspace(0, 0, 25)

    tria = np.column_stack((x_coords, y_coords)).tolist()

    x_coords = np.linspace(100, 50, 25)
    y_coords = np.linspace(0, 100, 25)

    tria = tria + np.column_stack((x_coords, y_coords)).tolist()

    x_coords = np.linspace(50, 0, 25)
    y_coords = np.linspace(100, 0, 25)

    tria = tria + np.column_stack((x_coords, y_coords)).tolist()
    return tria


def format(e0):
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

    for i in range(len(e0)):
        x = e0[i][0]
        y = e0[i][1]

        e0[i][0] = (x - min_x) * 100 / (max_x - min_x)
        e0[i][1] = (y - min_y) * 100 / (max_y - min_y)

    return (max_x - min_x) / (max_y - min_y)


def show(e0):
    x = [point[0] for point in e0]
    y = [point[1] for point in e0]

    plt.plot(x, y, '-o')
    plt.axis('equal')
    plt.show()

def show1(e0, str):
    x = [point[0] for point in e0]
    y = [point[1] for point in e0]

    plt.plot(x, y, '-o')
    plt.axis('equal')
    plt.text(max(x) + 4, max(y) / 4 , str)
    plt.show()