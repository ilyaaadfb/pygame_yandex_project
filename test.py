import sys
from random import randrange as rnd
import pygame


def main():

    pygame.init()
    pygame.display.set_caption('Заголовок')
    size = width, height = 960, 600
    screen = pygame.display.set_mode(size)

    running = True
    fps = 90
    clock = pygame.time.Clock()
    r = 10
    circles = []
    k = 0
    while running:

        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                k += 1
                if k < 2:
                    circles.append([300, 300, -100, -100])


        for circle in circles:
            pygame.draw.circle(screen, (255, 255, 255), (circle[0], circle[1]), r)
            circle[0] += circle[2] / fps
            circle[1] += circle[3] / fps
            if circle[0] < r or circle[0] > width - r:
                circle[2] *= -1
            if circle[1] < r or circle[1] > height - r:
                circle[3] *= -1

        pygame.draw.rect(screen, (255, 255, 255),
                         (20, 20, 50, 20))

        block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 20) for i in range(12) for j in range(5)]
        color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(12) for j in range(5)]
        [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())
