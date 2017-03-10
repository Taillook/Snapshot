# -*- coding: utf-8 -*-


import cv2
import time
import subprocess as sp
import sys

def main(args=sys.argv[1:]):
    delay_time = 1

    cap = cv2.VideoCapture(0)
    time.sleep(delay_time)
    ret, frame = cap.read()
    path = "photo.jpg"
    cv2.imwrite(path,frame)

    cap.release()
    cv2.destroyAllWindows()