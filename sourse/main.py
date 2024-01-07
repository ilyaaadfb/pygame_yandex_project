import pygame
import sys
from button import ImageButton
import game_arc

pygame.init()

WIDTH, HEIGHT = 960, 600
MAX_FPS = 90

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcanoid")
main_background = pygame.image.load("background_image.png")
clock = pygame.time.Clock()

pygame_icon = pygame.image.load('arkanoid_ava.jpg')
pygame.display.set_icon(pygame_icon)


class Menu:
    def __init__(self):
        self.f = False

    def main_menu(self):
        WIDTH, HEIGHT = 960, 600
        start_button = ImageButton(WIDTH / 2 - (252 / 2), 150, 252, 74, "Новая игра", "grey_button.png",
                                   "blue_button.png",
                                   "click_sound.mp3")
        settings_button = ImageButton(WIDTH / 2 - (252 / 2), 250, 252, 74, "Настройки", "grey_button.png",
                                      "blue_button.png",
                                      "click_sound.mp3")
        exit_button = ImageButton(WIDTH / 2 - (252 / 2), 350, 252, 74, "Выйти", "grey_button.png", "blue_button.png",
                                  "click_sound.mp3")
        self.audio = True
        running = True
        while running:
            pygame.mixer.music.pause()
            screen.fill((0, 0, 0))
            screen.blit(main_background, (-600, -300))

            font = pygame.font.Font(None, 72)
            text_surface = font.render("ARCANOID", True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))  # расположение надписи
            screen.blit(text_surface, text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.USEREVENT and event.button == start_button:
                    print("Кнопка старт была нажата")
                    self.fade()
                    if self.audio:
                        pygame.mixer.music.load("music.mp3")
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.1)
                    game_arc.main()

                if event.type == pygame.USEREVENT and event.button == settings_button:
                    print("Кнопка 'настройки' была нажата")
                    self.fade()
                    self.settings_menu()

                if event.type == pygame.USEREVENT and event.button == exit_button:
                    running = False
                    pygame.quit()
                    sys.exit()

                for btn in [start_button, settings_button, exit_button]:
                    btn.handle_event(event)

            for btn in [start_button, settings_button, exit_button]:
                btn.check_hover(pygame.mouse.get_pos())
                btn.draw(screen)

            pygame.display.flip()

    def settings_menu(self):
        if not self.f:
            audio_button = ImageButton(WIDTH / 2 - (252 / 2), 220, 252, 74, "Аудио вкл", "grey_button.png",
                                       "blue_button.png",
                                       "click_sound.mp3")
            self.fl = True
        else:
            audio_button = ImageButton(WIDTH / 2 - (252 / 2), 220, 252, 74, "Аудио выкл", "grey_button.png",
                                       "blue_button.png",
                                       "click_sound.mp3")
            self.fl = False
        back_button = ImageButton(WIDTH / 2 - (252 / 2), 350, 252, 74, "Назад", "grey_button.png", "blue_button.png",
                                  "click_sound.mp3")

        running = True

        self.audio = True
        while running:
            screen.fill((0, 0, 0))
            screen.blit(main_background, (0, 0))

            font = pygame.font.Font(None, 72)
            text_surface = font.render("SETTINGS", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
            screen.blit(text_surface, text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.fade()
                        running = False

                if event.type == pygame.USEREVENT and event.button == back_button:
                    self.fade()
                    running = False

                if event.type == pygame.USEREVENT and event.button == audio_button:
                    if not self.f:
                        audio_button = ImageButton(WIDTH / 2 - (252 / 2), 220, 252, 74, "Аудио выкл", "grey_button.png",
                                                   "blue_button.png",
                                                   "click_sound.mp3")
                        self.audio = False
                        print(self.audio)

                    if self.f:
                        audio_button = ImageButton(WIDTH / 2 - (252 / 2), 220, 252, 74, "Аудио вкл", "grey_button.png",
                                                   "blue_button.png",
                                                   "click_sound.mp3")
                        self.audio = True
                        print(self.audio)

                    if self.f:
                        self.f = False
                    else:
                        self.f = True

                for btn in [audio_button, back_button]:
                    btn.handle_event(event)

            for btn in [audio_button, back_button]:
                btn.check_hover(pygame.mouse.get_pos())
                btn.draw(screen)

            pygame.display.flip()

    def new_game(self):
        back_button = ImageButton(WIDTH / 2 - (252 / 2), 350, 252, 74, "Назад", "grey_button.png", "blue_button.png",
                                  "click_sound.mp3")

        running = True
        while running:
            screen.fill((0, 0, 0))

            screen.blit(main_background, (0, -700))

            font = pygame.font.Font(None, 72)
            text_surface = font.render("Добро пожаловать в игру", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(text_surface, text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.fade()
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.fade()
                        running = False

                if event.type == pygame.USEREVENT and event.button == back_button:
                    self.fade()
                    running = False

                for btn in [back_button]:
                    btn.handle_event(event)

            for btn in [back_button]:
                btn.check_hover(pygame.mouse.get_pos())
                btn.draw(screen)

            pygame.display.flip()

    def fade(self):
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


if __name__ == '__main__':
    menu = Menu()
    menu.main_menu()
