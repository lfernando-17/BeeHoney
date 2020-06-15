import pygame
import random
pygame.init()
window = pygame.display.set_mode([1280,720])
title = pygame.display.set_caption("BeeHoney")
bee_x = 610
bee_y = 600
bee_direction = 8
bee_anim = 1
bg = pygame.image.load("sprites/bg.png")

spider_image = pygame.image.load("sprites/spider_1.png")
spider_x = 610
spider_y = 0
spider_anim = 1
spider_direction = 16
clock = pygame.time.Clock()
flower_x = 300
flower_y = 0
flower_local = random.randint(300,900)
flower_direction = 20
flower_img = pygame.image.load("sprites/flower.png")
score = 0

def draw():
    pygame.font.init()

    font = pygame.font.get_default_font()
    font_size = pygame.font.SysFont(font,100,True)
    score_text = (f"Score : {score}")
    score_text_render = font_size.render(score_text,True,[255,255,255])
    window.blit(bg,(0,0))
    window.blit(flower_img,(flower_x,flower_y))
    bee_image = pygame.image.load("sprites/bee_"+str(bee_anim)+".png")
    window.blit(bee_image,(bee_x,bee_y))
    spider_image = pygame.image.load("sprites/spider_"+str(spider_anim)+".png")
    window.blit(spider_image,(spider_x,spider_y))
    window.blit(score_text_render,(100,30))

def colision():
    global score
    global flower_y
    global spider_y
    if spider_y > 480 and bee_x + 50 > spider_x > bee_x - 50:
        score -= 10
        spider_y = -100
    if flower_y > 600 and bee_x + 40 > flower_x > bee_x - 40:
        score += 1
        flower_y = -50
while True:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            bee_direction *= -1
    spider_y +=spider_direction
    bee_x += bee_direction
    bee_anim +=1
    spider_anim +=1

    flower_y +=flower_direction

    if spider_x < bee_x:
        spider_x += 2
    elif spider_x > bee_x:
        spider_x -= 2

    if spider_y > 750 : 
        spider_y = -50
        spider_x = bee_x
    if bee_x >= 910:
        bee_x = 910
    elif bee_x <=300:
        bee_x = 300
    if bee_anim==4:
        bee_anim=1
    if spider_anim==4:
        spider_anim=1

    if flower_y > 750:
        flower_y = -50
        flower_local = random.randint(300,900)
        flower_x = flower_local
    draw()
    colision()
    pygame.display.update()