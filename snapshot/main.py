# -*- coding: utf-8 -*-


import cv2
import time
import subprocess as sp
import sys
import argparse

h = False # show_help
o = False # open_file
delay_time = 1
path = "photo.jpg"  # image_path
help_text = '''
USAGE: snapshot [options]
  -h          This help message
  -o          open image(mac only)
  -d int      Delay a time
  -p string   File path
'''


def opt(args):
    global h, o, delay_time, path
    if ("-h" in args):
        h = True
    if ("-d" in args):
        delay_time = int(args[args.index("-d") + 1])
    if ("-p" in args):
        path = args[args.index("-p") + 1]
    if ("-o" in args):
        o = True


def take():
    global delay_time, path
    cap = cv2.VideoCapture(0)
    time.sleep(delay_time)
    ret, frame = cap.read()
    cv2.imwrite(path, frame)
    cap.release()
    cv2.destroyAllWindows()
    print("took a picture at " + path)


def main(args=sys.argv[1:]):
    global h, o, path, help_text
    opt(args)

    if h:
        print(help_text)
    else:
        take()

    if o:
        sp.call(["open", path])


if __name__ == '__main__':
    main()
