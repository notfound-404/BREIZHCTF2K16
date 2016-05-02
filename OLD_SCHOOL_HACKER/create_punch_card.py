#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import convert
from PIL import Image


START_X = 25
START_Y = 26
DELTA_X = 34-25
DELTA_Y = 127-101
LEN = 80
WID = 12

# x 150   y 160
# fx 2965 fy 12*160
# dx 45   dy 160


def _usage():
    print("Usage:\n \
./%s -r <punched_card.jpg>\nor\n \
./%s -w <nude_card.png> <msg> [max:80 / A-Z0-9"
          % (sys.argv[0], sys.argv[0]))
    exit(1)


def _write(nude_card, msg):
    NAME = "ALL_CARD/IMG_"
    NAME += os.urandom(9).encode('base64').strip().replace('/', '')
    NAME += ".png"
    img = Image.open(nude_card)
    l, h = img.size
    pix = img.load()
    x = START_X
    for C in msg:
        if C == " ":
            x += DELTA_X
        else:
            y = START_Y
            for BIT in convert._convert_to_bin(C):
                if BIT == "0":
                    for h in range(y, y+11):
                        for l in range(x, x+5):
                            pix[l, h] = (0, 0, 0)
                if BIT == "1":
                    True
                y += DELTA_Y
            x += DELTA_X
    img.save(NAME)
    print('[+] Image successfully saved as %s' % NAME)


def _read(card_to_read):
    img = Image.open(card_to_read)
    l, h = img.size
    pix = img.load()
    RESULT = []
    x = START_X
    for i in range(LEN):
        y = START_Y
        DATA = ""
        for j in range(WID):
            if pix[x, y][0] == 0:
                DATA += "0"
            else:
                DATA += "1"
            y += DELTA_Y
        x += DELTA_X
        RESULT.append(convert._convert_to_ascii(DATA))
    try:
        print("[+] Output: %s" % ''.join(RESULT))
    except:
        print RESULT
        print("[!] Error. Some lines havent been decoded / value are None")
        exit(1)


if __name__ == '__main__':
    try:
        OTP = sys.argv[1]
        CARD = sys.argv[2]
        MSG = sys.argv[3]
    except:
        _usage()

    if len(MSG) > 80:
        _usage()

    if OTP == "-w":
        _write(CARD, MSG)
    if OTP == "-r":
        _read(CARD)
