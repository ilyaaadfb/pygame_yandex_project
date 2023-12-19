import pygame
import sys
from button import ImageButton


pygame.init()


WIDTH, HEIGHT = 960, 600
MAX_FPS = 90

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu test")
main_background = pygame.image.load("background.jpeg")
clock = pygame.time.Clock()

# курсор
# cursor = pygame.image.load("cursor.png")
# pygame.mouse.set_visible(False)

def main_menu():
    start_button = ImageButton(WIDTH/2 - (252/2), 150, 252, 74, "Новая игра", "button.jpg", "button2.jpg", "click.mp3")
    settings_button = ImageButton(WIDTH/2 - (252/2), 250, 252, 74, "Настройки", "button.jpg", "button2.jpg", "click.mp3")
    exit_button = ImageButton(WIDTH/2 - (252/2), 350, 252, 74, "Выйти", "button.jpg", "button2.jpg", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (-300, -300))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("BUTTON TEST", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))  # расположение надписи
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                print("Кнопка старт была нажата")
                fade()
                new_game()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                print("Кнопка 'настройки' была нажата")
                fade()
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [start_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [start_button, settings_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # x, y = pygame.mouse.get_pos()
        # screen.blit(cursor, (x-2, y-2))
        pygame.display.flip()

def settings_menu():
    audio_button = ImageButton(WIDTH / 2 - (252 / 2), 150, 252, 74, "Аудио", "button.jpg", "button2.jpg", "click.mp3")
    video_button = ImageButton(WIDTH / 2 - (252 / 2), 250, 252, 74, "Видео", "button.jpg", "button2.jpg", "click.mp3")
    back_button = ImageButton(WIDTH / 2 - (252 / 2), 350, 252, 74, "Назад", "button.jpg", "button2.jpg", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("SETTINGS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 100))  # расположение надписи
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def new_game():
    back_button = ImageButton(WIDTH / 2 - (252/2), 350, 252, 74, "Назад", "button.jpg", "button2.jpg", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(main_background, (0, -700))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Добро пожаловать в игру", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT/2))  # расположение надписи
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                fade()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            for btn in [back_button]:
                btn.handle_event(event)

        for btn in [back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def fade():
    running = True
    fade_alpha = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(MAX_FPS)


if __name__ == "__main__":
    main_menu()