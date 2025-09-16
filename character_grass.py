from pico2d import *
import math

open_canvas(800, 600)

def PlayerMove():
    while True:
        Circle_Move()


def Circle_Move():
    cx, cy = 400, 300
    r = 220

    for degree in range(-90, -450, -2):
        rad = math.radians(degree)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)




grass = load_image('grass.png')
character = load_image('character.png')


PlayerMove()
close_canvas()