import pygame
from . import global_value as g

def set_value():
    g.window_X = 1000
    g.window_Y = 500
    g.Cell_Size = 10
    g.Cell_State = [[0] * g.window_X for i in range(g.window_Y)]

    g.alpha_code = 1
    g.beta_code = 2

    g.alpha_posx = 150
    g.alpha_posy = 150
    g.alpha_range = 200

    g.beta_posx = 650
    g.beta_posy = 150
    g.beta_range = 200