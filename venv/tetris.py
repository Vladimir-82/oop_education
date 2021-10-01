import pygame
import time


WIDTH = 700  # ширина игрового окна
HEIGHT = 800 # высота игрового окна
FPS = 3 # частота кадров в секунду

pygame.init()

# pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TETRIZ")
clock = pygame.time.Clock()

x = WIDTH // 2
y = 600
run = True

while True:
    clock.tick(FPS)
    pygame.draw.circle(screen, (100, 50, 0), (x, y), (100))
    pygame.display.update()
    pygame.draw.circle(screen, (0, 0, 0), (x, y), (100))

    y -= 50
    if y == 100:
        break

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
