# -*- coding: utf-8 -*-


import cv2
import time
import subprocess as sp
import sys

h = False  # show_help
delay_time = 1
path = "photo.jpg"  # image_path


def opt(args):
    global h, delay_time, path
    if ("-h" in args):
        h = True
    if ("-d" in args):
        delay_time = int(args[args.index("-d") + 1])
    if ("-p" in args):
        path = args[args.index("-p") + 1]


def take():
    global h, delay_time, path
    cap = cv2.VideoCapture(0)
    time.sleep(delay_time)
    ret, frame = cap.read()
    cv2.imwrite(path, frame)
    cap.release()
    cv2.destroyAllWindows()
    print("took a picture at " + path)


def main(args=sys.argv[1:]):
    global h, delay_time, path
    opt(args)

    if h:
        print("help")
    else:
        take()


if __name__ == '__main__':
    main()
