import cv2


def match(q0, q1, str):
    ka1 = cv2.matchShapes(q0, q1, 1, 0)
    ka2 = cv2.matchShapes(q0, q1, 2, 0)
    ka3 = cv2.matchShapes(q0, q1, 3, 0)
    print("======" + str)
    print(ka1)
    print(ka2)
    print(ka3)