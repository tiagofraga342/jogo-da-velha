import pygame
import sys
import numpy as np

pygame.init()

# Constants for sizes, heights and widths of the objects
WINDOW_SIZE = 600
LINE_WIDTH = 15

# Constants for the colors in RGB
BG_COLOR = (20, 189, 172)
LINE_COLOR = (13, 161, 146)

# Draw the window
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

# Set the window title
pygame.display.set_caption('Joguinho da velha :)')
window.fill(BG_COLOR)


# Function to draw the lines
def draw_lines():
    # Horizontal lines
    pygame.draw.line(window, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(window, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(window, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(window, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


draw_lines()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
