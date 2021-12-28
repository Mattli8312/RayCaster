# Function for rendering map for ray tracing purposes;
from src import Assets;
import pygame as py;

def Generate_Map( map_file , tile_width = 25):
    fin = open(map_file)
    Assets.off_x = Assets.off_y = tile_width;
    i = j = 0;
    for line in fin:
        j = 0;
        new_grid_line = [];
        for char in line:
            if(char == '#'): 
                py.draw.rect(Assets.screen, (255,255,255), ( Assets.off_x + j * tile_width, Assets.off_y + i * tile_width, tile_width, tile_width));
                new_grid_line.append(1);
            else: new_grid_line.append(0);
            j += 1;
        Assets.grid.append(new_grid_line);
        j -= 1;
        i += 1;