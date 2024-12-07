import pygame
import sys
import time
from pygame.locals import *

# Pygame 초기화

pygame.init()
sysfont = pygame.font.SysFont(None, 72)

# 화면 설정
(screen_width, screen_height) = (1200, 600)
screen = pygame.display.set_mode((screen_width, screen_height),
                                 FULLSCREEN
                                 )

#제목
pygame.display.set_caption("중력")

# 색상 정의 (RGB)
white = (255, 255, 255)
black = (  0,   0,   0)

#공의 최초 좌표
ball_x =  screen_width / 2
ball_y = 20

#공의 크기
ball_size  = 10

#변수
ball_upspeed = 0
ball_speed = 0
ball_t = 0
ball_g = 0


#틱 속도
clock = pygame.time.Clock()

#중력

    
# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

    if ball_x < 0 and ball_speed:
        ball_speed*= -1

    keys = pygame.key.get_pressed()
    
    if keys[K_LEFT]:
        ball_speed = -30

    if keys[K_RIGHT]:
        ball_speed =  30

    if keys[K_UP]:
        ball_upspeed -=5

    if keys[K_DOWN]:
        ball_upspeed +=5
    
    if keys[K_q]:
        running = False



    #y좌표
    if ball_y + 50 > screen_height  :
        if ball_upspeed < 0 :
            ball_upspeed += 1
            ball_y += ball_upspeed
        else :
            ball_upspeed *= -1/3
            if -1 <ball_upspeed <1 :
                ball_upspeed = 0
       
    else :
        ball_upspeed += 1
        ball_y += ball_upspeed




    #x좌표
    if ball_speed > 0:
        ball_speed += -1

    elif ball_speed < 0:
        ball_speed += 1
        
    ball_x += ball_speed
    

    if ball_x <= 30 and ball_speed < 0:
        ball_speed *= -1
        
    if ball_x > screen_width - 10 and ball_speed > 0 :
        ball_speed*= -1


    if ball_x < 0 :
        ball_speed = 0
        ball_x += 10
    if ball_x > screen_width :
        ball_speed = 0
        ball_x -= 10
        

    # 화면 배경색 설정
    screen.fill(white)
    pygame.draw.circle(screen, black, [ball_x, ball_y], ball_size, 0)
    ball_t += 1
        
    timetext = str(ball_t).encode('utf-8')
    speedtext = str(ball_upspeed).encode('utf-8')
    x_speedtext = str(ball_speed).encode('utf-8')
        
    Time_txt = sysfont.render(timetext,True,black)#시간
    Speed_txt = sysfont.render(speedtext,True,black)#중력
    X_Speed_txt = sysfont.render(x_speedtext,True,black)#중력

    screen.blit(Time_txt, (0,0))    
    screen.blit(Speed_txt, (0,50))
    screen.blit(X_Speed_txt, (0,100))

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)
    
time.sleep(3)# Pygame 종료
pygame.quit()
sys.exit()
