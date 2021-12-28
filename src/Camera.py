from src import Assets;
import pygame as py;
import math;

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
        self.angle = 0;
        self.angle_speed = 4;
    def Render_Camera(self):
        old_center = self.rect.center;
        rect = self.new_image.get_rect();
        rect.center = old_center;
        Assets.screen.blit(self.new_image, rect);
        py.display.flip();
    def Rotate(self, direction = 1):
        self.angle = (self.angle + self.angle_speed * direction) % 360;
        new_image = py.transform.rotate(self.image_orig, self.angle);
        self.new_image = new_image;
    def Move(self, direction = 1):
        curr_tuple = self.rect.center;
        x_final = curr_tuple[0] + direction * (int)(self.speed * (math.sin(math.pi * self.angle / 180)));
        y_final = curr_tuple[1] + direction * (int)(self.speed * (math.cos(math.pi * self.angle / 180)));
        new_tuple = (x_final, y_final);
        self.rect.center = new_tuple;
    def Cast_Rays(self):
        # Cast the center Rays;
        pass;