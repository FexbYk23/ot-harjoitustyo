import chip8
import sys
import pygame


if len(sys.argv) != 2:
    exit("USAGE: chip8 program")


with open(sys.argv[1], "rb") as f:
    program = f.read()


c8 = chip8.Chip8()
c8.load_program(program, 0x200)
c8.debug_print = True

pygame.init()
SCALE = 8
screen = pygame.display.set_mode((64*SCALE, 32*SCALE))
clk = pygame.time.Clock()
while True:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            exit()
    screen.fill((0, 0, 0))

    c8.exec_next()

    for y in range(32):
        for x in range(64):
            pixelRect = pygame.Rect((SCALE*x, SCALE*y), (SCALE, SCALE))
            if c8.framebuf[y * 64 + x] > 0:
                pygame.draw.rect(screen, (255, 255, 255), pixelRect)

    pygame.display.flip()
    clk.tick(60)
