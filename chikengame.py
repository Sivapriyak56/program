import pygame
import random

screen_size = [360, 400]
screen = pygame.display.set_mode(screen_size)
pygame.font.init()

background = pygame.image.load('background.png')
user = pygame.image.load('user.png')
chicken = pygame.image.load('chicken.png')


def display_score(score):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    score_text = 'score ' + str(score)
    text_img = font.render(score_text, True, (0, 255, 0))
    screen.blit(text_img, [20, 10])


def random_off():
    return -1 * random.randint(100, 1500)


chicken_y = [random_off(), random_off(), random_off()]
user_x = 180
score = 0


def update_off(ind):
    global score
    if chicken_y[ind] > 600:
        chicken_y[ind] = random_off()
        score = score + 5
        print('score', score)
    else:
        chicken_y[ind] = chicken_y[ind] + 5


def crash(ind):
    global score
    score = score - 50
    print('crashed', ind)
    chicken_y[ind] = random_off()


clock = pygame.time.Clock()
keep_alive = True
while keep_alive:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user_x < 300:
        user_x = user_x + 10
    elif keys[pygame.K_LEFT] and user_x > 0:
        user_x = user_x - 10
    update_off(0)
    update_off(1)
    update_off(2)

    screen.blit(background, [0, 0])
    screen.blit(user, [user_x, 325])
    screen.blit(chicken, [0, chicken_y[0]])
    screen.blit(chicken, [150, chicken_y[1]])
    screen.blit(chicken, [280, chicken_y[2]])

    if chicken_y[0] > 320 and user_x < 70:
        crash(0)
    if chicken_y[1] > 320 and user_x > 80 and user_x < 2000:
        crash(1)
    if chicken_y[2] > 320 and user_x > 220:
        crash(2)

    display_score(score)

    pygame.display.update()
    clock.tick(25)

