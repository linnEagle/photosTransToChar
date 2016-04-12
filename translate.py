#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Lin on 2016/4/9

from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}.]?-_+~<>i!lI;:,\"^`'. ")

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int)
parser.add_argument('--height', type=int)
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 +1)/length
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':
    im = Image.open(IMG)
    print im.size
    if WIDTH is None:
        WIDTH = im.size[0]
    if HEIGHT is None:
        HEIGHT = im.size[1]
    im = im.resize(im.size, Image.NEAREST)
    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print txt

    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        filename = IMG[:-3]+'txt'
        with open(filename, 'w') as f:
            f.write(txt)
