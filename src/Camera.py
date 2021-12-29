from pygame.version import ver
from src import Assets;
import pygame as py;
import math;
import numpy as np;

# https://stackoverflow.com/questions/36510795/rotating-a-rectangle-not-image-in-pygame/51381391#51381391


class Camera:
    def __init__ (self, x, y, w):
        self.x = x;
        self.y = y;
        self.w = w;
        self.rays = [];
        #Thanks to link above
        self.image_orig = py.Surface((self.w,self.w));
        self.image_orig.set_colorkey((0,0,0));
        self.image_orig.fill((255,0,0));
        self.rect = self.image_orig.get_rect();
        self.rect.center = (self.x, self.y);
        self.speed = 5;
        self.new_image = self.image_orig.copy();
        #Thanks to link above
        self.ray_count = 14;
        self.angle = 90;
        self.angle_speed = 4;
    def Render_Camera(self):
        old_center = self.rect.center;
        rect = self.new_image.get_rect();
        rect.center = old_center;
        Assets.screen.blit(self.new_image, rect);
        py.display.flip();
        #Render Rays
        for r in self.rays: py.draw.line(Assets.screen, (255,0,0), (self.x, self.y), (r[0], r[1]));
    def Rotate(self, direction = 1):
        self.angle = (self.angle + self.angle_speed * direction) % 360;
        new_image = py.transform.rotate(self.image_orig, self.angle);
        self.new_image = new_image;
    def Move(self, direction = 1):
        curr_tuple = self.rect.center;
        self.x = curr_tuple[0] + direction * (int)(self.speed * (math.sin(math.pi * self.angle / 180)));
        self.y = curr_tuple[1] + direction * (int)(self.speed * (math.cos(math.pi * self.angle / 180)));
        new_tuple = (self.x, self.y);
        self.rect.center = new_tuple;
    def Cast_Rays(self, ray_count = 20):
        self.rays = [];
        for i in range(-ray_count // 2, ray_count // 2 + 1, 1): 
            self.Cast_Ray(self.angle + i * 4);

    def Cast_Ray(self, angle):
        """
        x, y = self.rect.center[0], self.rect.center[1];
        while True:
            i = (x - Assets.off_x) // Assets.tile_width;
            j = (y - Assets.off_y) // Assets.tile_width;
            if( x < 0 or y < 0 or x >= Assets.width or y >= Assets.height):
                break;
            elif( i > -1 and j > -1 and i < len(Assets.grid[0]) and j < len(Assets.grid) and Assets.grid[j][i]):
                py.draw.line(Assets.screen, (255,0,0), (self.rect.center[0], self.rect.center[1]), (x,y));
                break;
            else: 
                y -= (int)(math.cos(angle * math.pi / 180) * Assets.tile_magnitude);
                x -= (int)(math.sin(angle * math.pi / 180) * Assets.tile_magnitude);
        """ 
        # + Optimization + #
        delta = np.sign([math.cos(angle * math.pi / 180), math.sin((angle * math.pi) / 180)]);
        tan_angle = math.tan((angle - 90) * math.pi / 180);
        y_o = self.y;
        x_o = self.x;
        # Check the horizontal distance first 
        while(delta[1] and (x_o - Assets.off_x) % Assets.tile_width): x_o -= delta[1];
        y_o -= (x_o - self.x) * tan_angle;
        i, j = self.Position_To_Index(x_o, y_o);
        while(self.Valid_Index(i,j) and x_o > 0 and y_o > 0 and not Assets.grid[i][j]):
            x_o -= delta[1] * Assets.tile_width;
            y_o += delta[1] * Assets.tile_width * tan_angle;
            i, j = self.Position_To_Index(x_o  - delta[1] * 5 , y_o);
        # #Check the vertical distance second
        y_i = self.y;
        x_i = self.x;
        while(delta[0] and (y_i - Assets.off_y) % Assets.tile_width): y_i -= delta[0];
        y_i -= delta[0] * Assets.tile_width;
        if(tan_angle): x_i -= (y_i - self.y) / tan_angle;
        else: x_i += delta[0] * 1000; # Auto Correction for infinity
        i, j = self.Position_To_Index(x_i, y_i);
        while(self.Valid_Index(i,j) and not Assets.grid[i][j]):
            y_i -= delta[0] * Assets.tile_width;
            if(tan_angle):x_i += delta[0] *(Assets.tile_width) / tan_angle;
            else: x_i += delta[0] * 1000;
            i, j = self.Position_To_Index(x_i , y_i - delta[0] * 5);
        # Compare Horizontal and Veritcal Distances
        horiz_dist = (self.x - x_o)**2 + (self.y - y_o)**2;
        vert_dist = (self.x - x_i)**2 + (self.y - y_i)**2;
        if(horiz_dist < vert_dist): self.rays.append([x_o,y_o]);
        else: self.rays.append([x_i,y_i]);

    def Position_To_Index(self, x, y):
        j = (int)((x - Assets.off_x) // Assets.tile_width);
        i = (int)((y - Assets.off_y) // Assets.tile_width);
        return i, j;

    def Valid_Index(self, i, j):
        return i > -1 and j > -1 and i < len(Assets.grid) and j < len(Assets.grid[0]) - 1;