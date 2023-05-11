import cv2

def match(q0, q1, str):
    res = cv2.matchShapes(q0, q1, 1, 0)
    return res