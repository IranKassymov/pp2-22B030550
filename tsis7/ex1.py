import pygame
import datetime
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

clock = pygame.image.load("image/mickey.jpeg")
scale_clock = pygame.transform.scale(clock, (clock.get_width() // 2, clock.get_height() // 2))
clockr = scale_clock.get_rect(center=(width/2, height/2))

second = pygame.image.load("image/arrow.png")
scale_second = pygame.transform.scale(second, (second.get_width() // 2, second.get_height() // 2))

minute = pygame.image.load("image/arrow.png")
scale_minute = pygame.transform.scale(minute, (minute.get_width() // 2, minute.get_height() // 2))

running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((255, 255, 255))
    screen.blit(scale_clock, clockr)
    t = datetime.datetime.now()
    minutes, seconds = t.minute, t.second
    rots = pygame.transform.rotate(scale_second, (-6*seconds)+90)
    rots_rect = rots.get_rect(center=(400, 300))
    screen.blit(rots, rots_rect)
    rotm = pygame.transform.rotate(scale_minute, (-6*minutes)+90)
    rotm_rect = rotm.get_rect(center=(400, 300))
    screen.blit(rotm, rotm_rect)
    pygame.display.update()