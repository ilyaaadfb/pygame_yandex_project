import pygame
from random import randrange as rnd
import sys

WIDTH, HEIGHT = 960, 600

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
img = pygame.image.load('background.jpeg').convert()


def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy



def main():
    fps = 60
    paddle_w = 150
    paddle_h = 10
    paddle_speed = 15
    paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)
    ball_radius = 10
    ball_speed = 5
    ball_rect = int(ball_radius * 2 ** 0.5)
    ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
    dx, dy = 1, -1
    block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(11) for j in range(4)]
    color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(11) for j in range(4)]
    running = True
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
    print("Нажмите пробел")
    q = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                q = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        # отрисовка
        sc.blit(img, (0, 0))
        [pygame.draw.rect(sc, color_list[color], block) for color, block in enumerate(block_list)]
        pygame.draw.rect(sc, pygame.Color('darkorange'), paddle)
        pygame.draw.circle(sc, pygame.Color('white'), ball.center, ball_radius)

        if not q:
            font = pygame.font.Font(None, 50)
            text = font.render("Нажмите на пробел!", True, (100, 255, 100))
            text_x = WIDTH // 2 - text.get_width() // 2
            text_y = HEIGHT // 2 - text.get_height() // 2
            sc.blit(text, (text_x, text_y))




        if q:
            # механика игра
            ball.x += ball_speed * dx
            ball.y += ball_speed * dy
            if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
                dx = -dx
            if ball.centery < ball_radius:
                dy = -dy
            if ball.colliderect(paddle) and dy > 0:
                dx, dy = detect_collision(dx, dy, ball, paddle)
            hit_index = ball.collidelist(block_list)
            if hit_index != -1:
                hit_rect = block_list.pop(hit_index)
                hit_color = color_list.pop(hit_index)
                dx, dy = detect_collision(dx, dy, ball, hit_rect)
                hit_rect.inflate_ip(ball.width * 3, ball.height * 3)
                pygame.draw.rect(sc, hit_color, hit_rect)
                fps += 2
            if ball.bottom > HEIGHT:
                running = False

            elif not len(block_list):
                running = False

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and paddle.left > 0:
                paddle.left -= paddle_speed
            if key[pygame.K_RIGHT] and paddle.right < WIDTH:
                paddle.right += paddle_speed


        pygame.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    sys.exit(main())
