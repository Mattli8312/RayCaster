# Function for rendering map for ray tracing purposes;
from src import Assets;
import pygame as py;

def Generate_Map( map_file , tile_width = 25):
    fin = open(map_file)
    off_x = off_y = tile_width;
    i = j = 0;
    for line in fin:
        j = 0;
        for char in line:
            py.draw.line(Assets.screen, (255,255,255), ( off_x + j * tile_width, off_y ), ( off_x + j * tile_width, off_y + i * tile_width));
            if(char == '#'): py.draw.rect(Assets.screen, (255,255,255), ( off_x + j * tile_width, off_y + i * tile_width, tile_width, tile_width));
            j += 1;
        j -= 1;
        py.draw.line(Assets.screen, (255,255,255), ( off_x , off_y + i * tile_width), ( off_x + j * tile_width, off_y + i * tile_width));
        i += 1;