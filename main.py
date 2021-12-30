# Importing Modules #
import pygame as py;
import sys; sys.path.append("./src");
from src import Assets;
from src import Map;
from src import Camera;
py.init();

camera_x = 150;
camera_y = 300;
camera = Camera.Camera(camera_x,camera_y,20);
running = True;
Map.Initialize_Map("./src/Map1.txt");

while(running):
    Assets.screen.fill((0,0,0));
    # Map.Generate_Map(Assets.tile_width); # 2-D view
    # camera.Render_Camera(); # 2-D view
    camera.Render_Camera_View(); # 3-D view
    camera.Cast_Rays();
    for event in py.event.get():
        if(event.type == py.QUIT):
            running = False;
    keys = py.key.get_pressed();
    if(keys[97]): camera.Rotate(1);
    elif(keys[100]): camera.Rotate(-1);
    if(keys[119]): camera.Move(-1);
    elif(keys[115]): camera.Move(1);
    py.display.update();
    Assets.clock.tick(40);
    py.time.delay(40);
py.quit();