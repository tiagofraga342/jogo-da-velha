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


draw_lines()


def draw_verticalLine(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(window, color, (posX, 15), (posX, WINDOW_SIZE - 15), 15)


def draw_horizontalLine(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(window, color, (15, posY), (WINDOW_SIZE - 15, posY), 15)


def draw_diagonalPrincipalLine(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(window, color, (15, 15), (WINDOW_SIZE - 15, WINDOW_SIZE - 15), 15)


def draw_diagonalSecondaryLine(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(window, color, (15, WINDOW_SIZE - 15), (WINDOW_SIZE - 15, 15), 15)


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


# Function to check if a player won the match
def checkWin(player):
    # Check vertical win
    for col in range(BOARD_SIZE):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_verticalLine(col, player)
            return True

    # Check horizontal win
    for row in range(BOARD_SIZE):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontalLine(row, player)
            return True

    # Check principal diagonal win
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_diagonalPrincipalLine(player)
        return True

    # Check secondary diagonal win
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_diagonalSecondaryLine(player)
        return True

    return False


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
                    checkWin(player)
                    player = 2
                elif player == 2:
                    markSquare(clicked_row, clicked_col, player)
                    checkWin(player)
                    player = 1

    pygame.display.update()
