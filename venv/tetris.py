import pygame
import time


WIDTH = 10  # ширина игрового окна
HEIGHT = 20 # высота игрового окна
TILE = 45
GAME_RES = WIDTH * TILE, HEIGHT * TILE
FPS = 3 # частота кадров в секунду

pygame.init()


pygame.display.set_caption("TETRIZ")
clock = pygame.time.Clock()


grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(WIDTH) for y in range(HEIGHT)]




while True:
    screen = pygame.display.set_mode((GAME_RES))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [pygame.draw.rect(screen, (40, 40, 40), i_rect, 1) for i_rect in grid]

    pygame.display.flip()
    clock.tick(FPS)