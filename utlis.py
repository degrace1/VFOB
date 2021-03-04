import cv2
import numpy as np

def thresholding(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerBlue = np.array([90, 44, 245])
    upperBlue = np.array([107, 255, 255])
    maskedBlue= cv2.inRange(hsv,lowerBlue,upperBlue)
    return maskedBlue
