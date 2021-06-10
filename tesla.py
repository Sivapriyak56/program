import pygame


display_size = (1200, 400)
display = pygame.display.set_mode(display_size)
pygame.init()


track = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car,(30,60))
car_y = 280
car_x = 155

cam_x_offset = 0
cam_y_offset = 0
direction = 'up'

focal_dis = 25
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15
    up_px = display.get_at((cam_x, cam_y - focal_dis))[0]
    right_px = display.get_at((cam_x + focal_dis, cam_y))[0]
    down_px = display.get_at((cam_x, cam_y + focal_dis))[0]

    print(up_px, right_px, down_px)
    if direction == 'up' and right_px == 255 and up_px != 255:
        direction = 'right'
        car = pygame.transform.rotate(car, -90)
        cam_x_offset = 30

    if direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)

    if direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_y = car_y + 30
        cam_y_offset = 0
        cam_x_offset = 30
        car = pygame.transform.rotate(car, 90)

    if direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)


    if direction == 'up' and up_px == 255:
        car_y = car_y - 2
    elif direction == 'right' and right_px == 255:
        car_x = car_x + 2
    elif direction == 'down' and down_px == 255:
        car_y = car_y + 2


    display.blit(track, [0, 0])
    display.blit(car, [car_x, car_y])
    cam = pygame.draw.circle(display, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
    clock.tick(60)