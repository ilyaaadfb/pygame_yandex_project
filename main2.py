import pygame
import sys
from button import ImageButton


pygame.init()


WIDTH, HEIGHT = 960, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu test")
main_background = pygame.image.load("background.jpeg")

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

            for btn in [start_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [start_button, settings_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def settings_menu():
    ...

def new_game():
    pass

if __name__ == "__main__":
    main_menu()