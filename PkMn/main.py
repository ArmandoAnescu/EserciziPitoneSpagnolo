from game_base.pokemon import Pokemon
from game_base.battle import battle

urPkMn=[]
oppPkMn=[]
opzioni=["Lotta","Vedi i miei Pkmn","Aggiungi Pkmn","RimuoviPkmn","Esci"]
userName = "Test"
import pygame
import sys

# Inizializza Pygame
pygame.init()

# Impostazioni della finestra
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu di gioco")

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Font per il menu
font = pygame.font.Font(None, 36)


# Funzione per disegnare il menu
def draw_menu():
    screen.fill(BLACK)
    title_text = font.render("MENU PRINCIPALE", True, WHITE)
    start_text = font.render("1. Inizia Gioco", True, WHITE)
    quit_text = font.render("2. Esci", True, WHITE)

    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 100))
    screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, 200))
    screen.blit(quit_text, (screen_width // 2 - quit_text.get_width() // 2, 250))

    pygame.display.flip()


# Funzione per gestire le selezioni
def handle_selection():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Verifica se il click è su un'opzione
                if 200 <= mouse_y <= 240:  # Range per "Inizia Gioco"
                    print("Gioco iniziato")
                    running = False  # Esci dal menu e avvia il gioco (ad esempio)
                elif 250 <= mouse_y <= 290:  # Range per "Esci"
                    pygame.quit()
                    sys.exit()

        draw_menu()


# Esegui il menu
handle_selection()
