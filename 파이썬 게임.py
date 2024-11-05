import pygame
import sys
import time
from pygame.locals import *

# Pygame 초기화

pygame.init()
sysfont = pygame.font.SysFont(None, 72)



# 화면 설정
(screen_width, screen_height) = (800, 600)
screen = pygame.display.set_mode((screen_width, screen_height),FULLSCREEN)

pygame.display.set_caption("중력")

# 색상 정의 (RGB)
white = (255, 255, 255)
black = (  0,   0,   0)

#공의 최초 좌표
ball_x = int(screen_width /2)
ball_y = 0



#공의 크기
ball_size  = 10

#중력가속도
ball_g = 0
ball_t = 0
#틱 속도
clock = pygame.time.Clock()



# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

  

    ball_g += ball_t * 0.098
    ball_y = ball_y + ball_g
    # 화면 배경색 설정
    screen.fill(white)
    pygame.draw.circle(screen, black, [ball_x, ball_y], ball_size, 0)
    ball_t += 1

    #정지
    if ball_y > screen_height :
        running = False
        
    timetext = str(ball_t).encode('utf-8')
    gravitytext = str(ball_g).encode('utf-8')
    
    Time_txt = sysfont.render(timetext,True,black)#시간
    Gravity_txt = sysfont.render(gravitytext,True,black)#중력

    screen.blit(Time_txt, (0,0))    
    screen.blit(Gravity_txt, (0,50))

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(30)

    

    
time.sleep(3)# Pygame 종료
pygame.quit()
sys.exit()
