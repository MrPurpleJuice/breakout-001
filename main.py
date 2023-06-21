import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the paddle
paddle_width = 80
paddle_height = 10
paddle_x = (width - paddle_width) // 2
paddle_y = height - 20
paddle_dx = 5

# Set up the ball
ball_radius = 8
ball_x = width // 2
ball_y = height // 2
ball_dx = 3
ball_dy = 3

# Set up the bricks
brick_rows = 5
brick_cols = 8
brick_width = 75
brick_height = 20
brick_gap = 10
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_gap) + brick_gap
        brick_y = row * (brick_height + brick_gap) + brick_gap
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_dx
    if keys[K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += paddle_dx

    # Handle ball collisions with walls
    if ball_x < 0 or ball_x > width - ball_radius:
        ball_dx *= -1
    if ball_y < 0:
        ball_dy *= -1

    # Update the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Handle ball collision with paddle
    if (
        ball_y + ball_radius >= paddle_y
        and ball_x + ball_radius >= paddle_x
        and ball_x - ball_radius <= paddle_x + paddle_width
    ):
        ball_dy *= -1

    # Draw the paddle
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw the ball
    ball = pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Handle ball collision with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy *= -1
            break

    # Draw the bricks
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)

    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()

