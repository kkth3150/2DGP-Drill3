from pico2d import *
import math

open_canvas(800, 600)

def PlayerMove():
    while True:
        Circle_Move()
        Square_Move()
        Triangle_Move()


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

def Square_Move():
    points = [(400, 80), (750, 80), (750, 550), (50, 550), (50, 80), (400, 80)]
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        move = 100
        dx = (x2 - x1) / move
        dy = (y2 - y1) / move
        for step in range(move):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x1 + dx * step, y1 + dy * step)
            delay(0.01)

def Triangle_Move():
    points = [(400, 80), (700, 80), (400, 550), (100, 80), (400, 80)]
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        move = 80
        dx = (x2 - x1) / move
        dy = (y2 - y1) / move
        for step in range(move):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x1 + dx * step, y1 + dy * step)
            delay(0.01)

grass = load_image('grass.png')
character = load_image('character.png')


PlayerMove()
close_canvas()