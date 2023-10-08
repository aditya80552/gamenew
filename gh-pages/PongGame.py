import pygame

# Define the game constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 300
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
BALL_RADIUS = 5

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the paddle objects
paddle1 = pygame.Rect(10, 100, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(480, 100, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create the ball object
ball = pygame.Rect(250, 150, BALL_RADIUS * 2, BALL_RADIUS * 2)

# Set the ball's velocity
ball.dx = 5
ball.dy = -5

# Game loop
while True:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles
    paddle1.y += pygame.key.get_pressed()[pygame.K_w] - pygame.key.get_pressed()[pygame.K_s]
    paddle2.y += pygame.key.get_pressed()[pygame.K_UP] - pygame.key.get_pressed()[pygame.K_DOWN]

    # Keep the paddles within the bounds of the screen
    paddle1.y = min(paddle1.y, SCREEN_HEIGHT - PADDLE_HEIGHT)
    paddle1.y = max(paddle1.y, 0)
    paddle2.y = min(paddle2.y, SCREEN_HEIGHT - PADDLE_HEIGHT)
    paddle2.y = max(paddle2.y, 0)

    # Move the ball
    ball.x += ball.dx
    ball.y += ball.dy

    # Check for collisions with the paddles
    if ball.colliderect(paddle1):
        ball.dx = -ball.dx
    if ball.colliderect(paddle2):
        ball.dx = -ball.dx

    # Check if the ball has hit the top or bottom of the screen
    if ball.y < 0 or ball.y > SCREEN_HEIGHT - BALL_RADIUS * 2:
        ball.dy = -ball.dy

    # Check if the ball has gone past a paddle
    if ball.x < 0 or ball.x > SCREEN_WIDTH - BALL_RADIUS * 2:
        # Game over
        break

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the paddles
    pygame.draw.rect(screen, (255, 255, 255), paddle1)
    pygame.draw.rect(screen, (255, 255, 255), paddle2)

    # Draw the ball
    pygame.draw.ellipse(screen, (255, 0, 0), ball)

    # Update the display
    pygame.display.flip()

# Game over
pygame.quit()


