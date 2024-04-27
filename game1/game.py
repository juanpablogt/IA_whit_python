import sys
import pygame

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    bge_color = (0,255,0)
    # Start the main loop for the game.
    while True:
    # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            screen.fill(bge_color)

run_game()
