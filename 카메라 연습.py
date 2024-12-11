import pygame
import time
import math
import sys
from pygame.locals import *



pygame.init()

(width, height) = (640,600)
screen = pygame. display. set_mode((width, height))


pygame.display.set_caption("카메라 연습")


clock = pygame.time.Clock()


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (230,  30,  30)


udangle = 0
lrangle = 0 
     


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running =False

    keys = pygame. key.get_pressed()
    

    if keys[K_q]:
            running =False
    if keys[K_UP]:
            udangle += 2
    if keys[K_DOWN]:
            udangle -= 2
    if keys[K_LEFT]:
            lrangle += 2
    if keys[K_RIGHT]:
            lrangle -= 2




            
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [0,height/2],[width,height/2],6)        
    pygame.draw.line(screen, RED, [0,height/2 + math.sin(math.pi * (udangle/180)) * height/8],[width, height/2 + math.sin(math.pi * (udangle/180)) * height/4 ],3)        
    pygame.draw.line(screen, RED, [0,height/2 + math.sin(math.pi * (udangle/180)) * height/4],[width, height/2 + math.sin(math.pi * (udangle/180)) * height/4 ],3)        
    pygame.draw.line(screen, RED, [0,height/2 + math.sin(math.pi * (udangle/180)) * height],[width, height/2 + math.sin(math.pi * (udangle/180)) * height/4 ],3)        
   



    pygame.draw.line(screen, BLACK, [0,height/2 + math.sin(math.pi * (udangle/180)) * height/2],[width, height/2 + math.sin(math.pi * (udangle/180)) * height/2 ],3)        
    pygame.draw.line(screen, RED, [0,height/2 - math.sin(math.pi * (udangle/180)) * height/4],[width, height/2 - math.sin(math.pi * (udangle/180)) * height/4 ],3)        
    pygame.draw.line(screen, BLACK, [0,height/2 - math.sin(math.pi * (udangle/180)) * height/2],[width, height/2 - math.sin(math.pi * (udangle/180)) * height/2 ],3)        

    pygame.draw.line(screen, BLACK, [width/2,0],[width/2,height],6)        
    pygame.draw.line(screen, RED, [width/2 + math.sin(math.pi *(lrangle/180))*width/4, 0],[width/2 + math.sin(math.pi *(lrangle/180))*width/4, height],3)        
    pygame.draw.line(screen, BLACK, [width/2 + math.sin(math.pi *(lrangle/180))*width/2, 0],[width/2 + math.sin(math.pi *(lrangle/180))*width/2, height],3)        
    pygame.draw.line(screen, RED, [width/2 - math.sin(math.pi *(lrangle/180))*width/4, 0],[width/2 - math.sin(math.pi *(lrangle/180))*width/4, height],3)        
    pygame.draw.line(screen, BLACK, [width/2 - math.sin(math.pi *(lrangle/180))*width/2, 0],[width/2 - math.sin(math.pi *(lrangle/180))*width/2, height],3)        
  





    pygame. display.flip()   
    clock.tick(100)


time.sleep(3)
pygame.quit()
