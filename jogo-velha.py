import pygame
import sys
import numpy as np

pygame.init()

# Constants for sizes, heights and widths of the objects
WINDOW_SIZE = 600
LINE_WIDTH = 15
BOARD_SIZE = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
X_WIDTH = 25
SPACE = 55

# Constants for the colors in RGB
BG_COLOR = (20, 189, 172)
LINE_COLOR = (13, 161, 146)
CIRCLE_COLOR = (242, 235, 211)
X_COLOR = (84, 84, 84)

# Draw the window
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

# Set the window title
pygame.display.set_caption('Joguinho da velha :)')
window.fill(BG_COLOR)

# Set the board matrice
board = np.zeros((BOARD_SIZE, BOARD_SIZE))

# Set the player variable
player = 1


# Function to draw the bg lines
def draw_lines():
    # Horizontal lines
    pygame.draw.line(window, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(window, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(window, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(window, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


# Function to mark the square
def markSquare(row, col, player):
    board[row][col] = player
    if player == 1:
        pygame.draw.circle(window, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
    elif player == 2:
        pygame.draw.line(window, X_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), X_WIDTH)
        pygame.draw.line(window, X_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), X_WIDTH)
    print(board)


# Function to check if a square is available
def availableSquare(row, col):
    return board[row][col] == 0


# Function to check if the board is full
def boardFull():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 0:
                return False

    return True


draw_lines()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]  # Stores the X click coordinate
            mouseY = event.pos[1]  # Stores the Y click coordinate
            clicked_row = int(mouseY // 200)  # Convert the Y coordinate into a row index
            clicked_col = int(mouseX // 200)  # Convert the X coordinate into a col index

            if availableSquare(clicked_row, clicked_col):
                if player == 1:
                    markSquare(clicked_row, clicked_col, player)
                    player = 2
                elif player == 2:
                    markSquare(clicked_row, clicked_col, player)
                    player = 1

    pygame.display.update()
