# Function for rendering map for ray tracing purposes;
from src import Assets;
import pygame as py;

def Initialize_Map( map_file ):
    fin = open(map_file)
    i = j = 0;
    for line in fin:
        j = 0;
        new_grid_line = [];
        for char in line:
            if(char == '#'): 
                new_grid_line.append(1);
            else: new_grid_line.append(0);
            j += 1;
        Assets.grid.append(new_grid_line);
        j -= 1;
        i += 1;

def Generate_Map( tile_width = 25):
    Assets.off_x = Assets.off_y = tile_width;
    i = j = 0;
    for g in Assets.grid:
        j = 0;
        for char in g:
            if(char == 1): 
                py.draw.rect(Assets.screen, (255,255,255), ( Assets.off_x + j * tile_width, Assets.off_y + i * tile_width, tile_width, tile_width));
            j += 1;
        j -= 1;
        i += 1;