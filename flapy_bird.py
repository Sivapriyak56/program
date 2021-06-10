import pygame
import time
from random import randint


display_size= (320, 568)
display = pygame.display.set_mode(display_size)
pygame.init()

text = pygame.font.Font(None, 50)
back = pygame.image.load('bg.png')
bird = pygame.image.load('bird.png')

bird_x = 50
bird_y = 200
pole_width = 70
top_pole_height = randint(100, 400)
pole_color = (50, 255, 20)
pole_gab = 100
pole_x = 320
score = 0

clock = pygame.time.Clock()
keep_alive = True
while keep_alive:
    pygame.event.get()

    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        bird_y = bird_y - 5
    if keys[pygame.K_DOWN]:
        bird_y = bird_y + 5
    display.blit(back,[0, 0])
    display.blit(bird, [bird_x, bird_y])
    pole_x = pole_x -2
    if pole_x <= -pole_width:
        pole_x = 320
        top_pole_height = randint(100, 400)
        score = score + 2
        print(score)
    pole = pygame.draw.rect(display,pole_color,[pole_x,0,pole_width,top_pole_height])
    pole = pygame.draw.rect(display, pole_color, [pole_x,top_pole_height+pole_gab,pole_width, 568])

    #collision

    if pole_x <= bird_x + 50 and bird_x <= pole_x + pole_width:
        if bird_y <= top_pole_height or bird_y >= top_pole_height+pole_gab:
            score = score - 2
            if score < -1000:
                game_over_text = text.render("GAME OVER", True, (255, 255, 255))
                time.sleep(2)
                keep_alive = False
                display.blit(game_over_text, [50, 100])
            print("Collision")

    score_text = text.render("score : " + f'{score}', True, (255, 255, 255))
    display.blit(score_text,[0,0])

    pygame.display.update()
    clock.tick(60)