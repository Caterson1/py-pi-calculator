import math

import pygame as p
import sys
import random

p.font.init()

widow_bounds = WIDTH, HEIGHT = 600, 600
origin = x0, y0 = WIDTH/2, HEIGHT - HEIGHT/2
font = p.font.SysFont('Monocraft', 12)
circle_radius = 200
#
# screen = p.display.set_mode((WIDTH, HEIGHT))
#
# def pygame_init():
#     # Screen or whatever you want to call it is your best friend - it's a canvas
#     # or surface where you can draw - generally you'll have one large canvas and
#     # additional surfaces on top - effectively breaking things up and giving
#     # you the ability to have multiples scenes in one window
#     p.init()
#     screen.fill((180, 210, 255))
#     p.display.set_caption('pi-calculator')

class Ball:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.in_circle = circle_radius > math.sqrt(self.position_x**2 + self.position_y**2)


running = True
ball_list = []
temp_ball_list = []
count_in = 0
count_out = 0

while True:
    # for event in p.event.get():
    #     if event.type == p.QUIT:  # this refers to clicking on the "x"-close
    #         p.quit()
    #         sys.exit()
    #     elif event.type == p.KEYDOWN:  # there's a separate system built in
    #         if event.key == p.K_SPACE:
    #             if running is False:
    #                 running = True
    #                 print("START")
    #             elif running is True:
    #                 running = False
    #                 print("PAUSE")

    if running:
        for x in range(2000):
            ball_list.append(
                Ball(random.uniform(-circle_radius, circle_radius),
                     random.uniform(-circle_radius, circle_radius)))
            # temp_ball_list.append(ball_list[-1])
            if ball_list[-1].in_circle:
                count_in += 1
            else:
                count_out += 1
        # for i in temp_ball_list:
        #     if i.in_circle:
        #         color = (0, 255, 0)
        #     else:
        #         color = (255, 0, 0)
        #     p.draw.circle(screen, color, (x0 + i.position_x, y0 - i.position_y), 1)
        # p.draw.circle(screen, (255, 255, 255), (x0, y0), circle_radius, 1)
        # p.draw.rect(screen, (255, 255, 255),
        #             (x0 - circle_radius, y0 - circle_radius,
        #              circle_radius * 2, circle_radius * 2), 1, 1)
        print(4*count_in/len(ball_list))
        # temp_ball_list = []

    # p.display.flip()