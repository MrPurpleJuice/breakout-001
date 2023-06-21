import pygame
from pygame.locals import *
from config import *

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Breakout")

clock = pygame.time.Clock()

# Set up the paddle
paddle_x = (WINDOW_WIDTH - PADDLE_WIDTH) // 2
paddle_y = WINDOW_HEIGHT - PADDLE_BOTTOM_MARGIN - PADDLE_HEIGHT
paddle_dx = PADDLE_SPEED

# Set up the ball
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

# Set up the bricks
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick_x = col * (BRICK_WIDTH + BRICK_GAP) + BRICK_GAP
        brick_y = row * (BRICK_HEIGHT + BRICK_GAP) + BRICK_GAP
        bricks.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))

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
    if keys[K_RIGHT] and paddle_x < WINDOW_WIDTH - PADDLE_WIDTH:
        paddle_x += paddle_dx

    # Handle ball collisions with walls
    if ball_x < 0 or ball_x > WINDOW_WIDTH - BALL_RADIUS:
        ball_dx *= -1
    if ball_y < 0:
        ball_dy *= -1

    # Handle ball collision with paddle
    if (
        ball_y + BALL_RADIUS >= paddle_y
        and ball_x + BALL_RADIUS >= paddle_x
        and ball_x - BALL_RADIUS <= paddle_x + PADDLE_WIDTH
    ):
        ball_dy *= -1

    # Update the ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Handle ball collision with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy *= -1
            break

    # Draw the paddle
    pygame.draw.rect(screen, PADDLE_COLOR, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)

    # Draw the bricks
    for brick in bricks:
        pygame.draw.rect(screen, BRICK_COLOR, brick)

    pygame.display.flip()
    clock.tick(FRAME_RATE)

# Quit the game
pygame.quit()
