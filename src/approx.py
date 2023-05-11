import cv2
import numpy as np

from src import generate

#基于approxPolyDP的拟合，并处理边际点
def approx(points):
    approx5 = cv2.approxPolyDP(points, 0.009 * cv2.arcLength(points, True), True)
    approx6 = cv2.approxPolyDP(points, 0.01 * cv2.arcLength(points, True), True)
    approx7 = cv2.approxPolyDP(points, 0.02 * cv2.arcLength(points, True), True)
    approx8 = cv2.approxPolyDP(points, 0.03 * cv2.arcLength(points, True), True)
    approx9 = cv2.approxPolyDP(points, 0.04 * cv2.arcLength(points, True), True)

    nums = [len(approx5), len(approx6), len(approx7), len(approx8), len(approx9)]

    result = '\n'.join(str(num) for num in nums)

    generate.show1(points, result)
    # 使用切片和join方法，在每5个数字之后添加一个换行符

    list2 = [len(process(approx5)), len(process(approx6)), len(process(approx7)), len(process(approx8)), len(process(approx9))]

    result = '\n'.join(str(num) for num in list2)
    generate.show1(points, result)

    p = process(approx8).tolist()

    res = []
    for i in p:
        res.append(i[0])

    return res

#暴力处理一笔画的初始点与结束点
def process(points):
    i = 1
    while i < len(points):
        dist = np.linalg.norm(points[i] - points[i - 1])
        if dist < 20:
            points = np.delete(points, i, axis=0)
        else:
            i += 1

    dist = np.linalg.norm(points[0] - points[-1])
    if dist < 20:
        points = np.delete(points, -1, axis=0)

    return points
