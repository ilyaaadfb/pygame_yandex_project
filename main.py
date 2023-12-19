import pygame
import sys
from button import ImageButton

pygame.init()

WIDTH, HEIGHT = 600, 550

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu test")
main_background = pygame.image.load("background.jpeg")


green_button = ImageButton(WIDTH/2-(252/2), 100, 252, 74, "", "button.jpg", "button2.jpg", "click.mp3")

green_button2 = ImageButton(WIDTH/2-(252/2), 300, 252, 74, "Выйти", "button.jpg", "button2.jpg", "click.mp3")

red_button = ImageButton(WIDTH/2-(252/2), 200, 252, 74, "", "button.jpg", "button2.jpg", "click.mp3")

icon_button = ImageButton(WIDTH/2-(252/2), 400, 85, 85, "", "button.jpg", "button2.jpg", "click.mp3")

icon_button2 = ImageButton(320, 400, 85, 85, "", "button.jpg", "button2.jpg", "click.mp3")

def main_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("BUTTON TEST", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 50)) # расположение надписи
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == green_button:
                print("Кнопка 1 была нажата")

            if event.type == pygame.USEREVENT and event.button == red_button:
                print("Кнопка 2 была нажата")

            if event.type == pygame.USEREVENT and event.button == green_button2:
                print("Кнопка 3 была нажата")

            if event.type == pygame.USEREVENT and event.button == icon_button:
                print("Кнопка 4 была нажата")

            if event.type == pygame.USEREVENT and event.button == icon_button2:
                print("Кнопка 5 была нажата")


            green_button.handle_event(event)
            green_button2.handle_event(event)
            red_button.handle_event(event)
            icon_button.handle_event(event)
            icon_button2.handle_event(event)

        green_button.check_hover(pygame.mouse.get_pos())
        green_button.draw(screen)
        green_button2.check_hover(pygame.mouse.get_pos())
        green_button2.draw(screen)
        red_button.check_hover(pygame.mouse.get_pos())
        red_button.draw(screen)
        icon_button.check_hover(pygame.mouse.get_pos())
        icon_button.draw(screen)
        icon_button2.check_hover(pygame.mouse.get_pos())
        icon_button2.draw(screen)
        pygame.display.flip()
main_menu()