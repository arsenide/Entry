import pygame as p

p.init()
w =(255,255,255)
size = (800,400) 
sc = p.display.set_mode(size)
p.display.set_caption("bounse ball") 
playing = True
#공 이미지 생성 
ball = p.image.load("ball.png")
b_rect = ball.get_rect(left=0,top=250)
#공 위치 변수
b_y = 0
#fps 설정
clock = p.time.Clock()

while playing:
    clock.tick(50)
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()
            
    sc.fill(w)
    #공 화면 업로드
    sc.blit(ball,b_rect)
    b_rect.top += b_y
    b_y += 1
    if b_rect.top >= 400:
        b_y = -20

    
    p.display.flip()
