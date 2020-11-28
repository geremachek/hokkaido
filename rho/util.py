from textwrap import wrap
from glob import glob
from os.path import basename
from time import sleep

# convert between types of colors

def rgb_to_hex(rgb: tuple) -> str:
    return '%02x%02x%02x' % rgb

def hex_to_rgb(hexa: str) -> tuple:
    return tuple(int(hexa.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

# ansi stuff

def ansi_hex(rgb: tuple) -> str:
    return "\033]11;#{}\007".format(rgb_to_hex(rgb))

def send_to_ttys(rgb: tuple):
    for tty in glob("/dev/pts/*"):
        if basename(tty).isdigit():
            f = open(tty, 'a')

            f.write(ansi_hex(rgb))

            f.close()

# increment/decrement rgb values without exceeding limits

def increment(n: int, inc: int) -> int:
    if n+inc <= 255 and n+inc >= 0:
        return n+inc
    else:
        return n

# breathe colors

def breathe_colors(rgb: list, og: list, cycles: int, inc: int, delay: int) -> list:
    orgb = rgb
    returning = rgb != og

    for i in range(cycles):
        if (inc > 0 and orgb != [255, 255, 255]) or (inc < 0 and orgb != [0,0,0]) or (returning and orgb == og): # break out of loop if max or minimum color value has been reached
            send_to_ttys(tuple(orgb))

            for i, v in enumerate(orgb):
                increased = increment(v, inc)

                if returning: # if the breath is returning to the original color, make sure that it doesn't go beyond it
                    if increased != og[i]:
                        orgb[i] = increased
                else:
                    orgb[i] = increased
            
            sleep(delay)
        else:
            break

    return orgb

def start(hexa: str, bright: bool, dark: bool, delay: int, cycles: int):
    rgb = list(hex_to_rgb(hexa))
    og = rgb
    inc = 1

    if dark : inc = -1

    while True:
        rgb = breathe_colors(rgb, og, cycles, inc, delay/1000)
        rgb = breathe_colors(rgb, og, cycles, -inc, delay/1000)
