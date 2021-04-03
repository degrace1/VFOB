import cv2
import numpy as np
import utlis

def getLaneCurve(img):

    imgThres = utlis.thresholding(img)

    cv2.imshow('Thres',imgThres)
    return None


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        img = cv2.resize(img,(480,240))
        curve = getLaneCurve(img)
        print(curve)
        cv2.imshow('Vid',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break