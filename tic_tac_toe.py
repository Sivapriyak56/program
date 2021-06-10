import pygame
from pygame.locals import *


screen_size = [550, 550]
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Siva's PONG game")
pygame.init()


img_x = pygame.image.load('x.png')
img_zero = pygame.image.load('zero.png')
frame = pygame.image.load('download.png')

first = pygame.draw.rect(screen, (225,255,255), (25,25,150,150))
second = pygame.draw.rect(screen, (225,255,255), (200,25,150,150))
third = pygame.draw.rect(screen, (225,255,255), (375,25,150,150))

four = pygame.draw.rect(screen, (225,255,255), (25,200,150,150))
five = pygame.draw.rect(screen, (225,255,255), (200,200,150,150))
six = pygame.draw.rect(screen, (225,255,255), (375,200,150,150))

seven = pygame.draw.rect(screen, (225,255,255), (25,375,150,150))
eight = pygame.draw.rect(screen, (225,255,255), (200,375,150,150))
nine = pygame.draw.rect(screen, (225,255,255), (375,375,150,150))

f_p = True
s_p = True
t_p = True
fo_p = True
fi_p = True
si_p = True
se_p = True
e_p = True
n_p = True


draw_object = 'rect'

keep_alive = True
while keep_alive:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:


                f_p = True
                s_p = True
                t_p = True
                fo_p = True
                fi_p = True
                si_p = True
                se_p = True
                e_p = True
                n_p = True

                first = pygame.draw.rect(screen, (225, 255, 255), (25, 25, 150, 150))
                second = pygame.draw.rect(screen, (225, 255, 255), (200, 25, 150, 150))
                third = pygame.draw.rect(screen, (225, 255, 255), (375, 25, 150, 150))

                four = pygame.draw.rect(screen, (225, 255, 255), (25, 200, 150, 150))
                five = pygame.draw.rect(screen, (225, 255, 255), (200, 200, 150, 150))
                six = pygame.draw.rect(screen, (225, 255, 255), (375, 200, 150, 150))

                seven = pygame.draw.rect(screen, (225, 255, 255), (25, 375, 150, 150))
                eight = pygame.draw.rect(screen, (225, 255, 255), (200, 375, 150, 150))
                nine = pygame.draw.rect(screen, (225, 255, 255), (375, 375, 150, 150))

        if event.type == pygame.MOUSEBUTTONUP:
            pos =pygame.mouse.get_pos()
            print(pos)
            if first.collidepoint(pos) and f_p:
                if draw_object == 'rect':
                    screen.blit(img_x, [80, 80])
                    draw_object = 'circle'
                    f_p = False
                else:
                    screen.blit(img_zero, [80, 80])
                    draw_object = 'rect'
                    f_p = False

            if second.collidepoint(pos) and s_p:
                if draw_object == 'rect':
                    screen.blit(img_x, [250, 80])
                    draw_object = 'circle'
                    s_p = False

                else:
                    screen.blit(img_zero, [250, 80])
                    draw_object = 'rect'
                    s_p = False
            if third.collidepoint(pos) and t_p:
                if draw_object == 'rect':
                    screen.blit(img_x, [450, 80])
                    draw_object = 'circle'
                    t_p = False
                else:
                    screen.blit(img_zero, [450, 80])
                    draw_object = 'rect'
                    t_p = False
            if four.collidepoint(pos) and fo_p:
                if draw_object == 'rect':
                    screen.blit(img_x, [80, 250])
                    draw_object = 'circle'
                    o_p = False
                else:
                    screen.blit(img_zero, [80, 250])
                    draw_object = 'rect'
                    fo_p = False
            if five.collidepoint(pos) and fi_p:
                if draw_object == 'rect':
                    screen.blit(img_x, [250, 250])
                    draw_object = 'circle'
                    fi_p = False
                else:
                    screen.blit(img_zero, [250, 250])
                    draw_object = 'rect'
                    fi_p = False
            if six.collidepoint(pos) and si_p:
                if draw_object == 'rect':
                    screen.blit(img_x, [450, 250])
                    draw_object = 'circle'
                    si_p = False
                else:
                    screen.blit(img_zero, [450, 250])
                    draw_object = 'rect'
                    si_p = False
            if seven.collidepoint(pos) and se_p:
                if draw_object == 'rect':
                    screen.blit(img_x, [80, 430])
                    draw_object = 'circle'
                    se_p = False
                else:
                    screen.blit(img_zero, [80, 430])
                    draw_object = 'rect'
                    se_p = False
            if eight.collidepoint(pos) and e_p:
                if draw_object == 'rect':
                    screen.blit(img_x, [250, 430])
                    draw_object = 'circle'
                    e_p = False
                else:
                    screen.blit(img_zero, [250, 430])
                    draw_object = 'rect'
                    e_p = False
            if nine.collidepoint(pos) and n_p:
                if draw_object == 'rect':
                    screen.blit(img_x, [450, 430])
                    draw_object = 'circle'
                    n_p = False
                else:
                    screen.blit(img_zero, [450, 430])
                    draw_object = 'rect'
                    n_p = False




     # screen.blit(img_zero, [150, 110]

    pygame.display.update()