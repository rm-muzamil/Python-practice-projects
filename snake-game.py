import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Initialize game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control game speed
clock = pygame.time.Clock()

# Fonts
score_font = pygame.font.SysFont("comicsansms", 35)
game_over_font = pygame.font.SysFont("comicsansms", 50)

# Snake properties
snake_speed = 5
snake_block = CELL_SIZE

def display_score(score):
    """Display the current score."""
    value = score_font.render(f"Your Score: {score}", True, WHITE)
    screen.blit(value, [10, 10])

def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    # Snake initial position and body
    x, y = WIDTH // 2, HEIGHT // 2
    snake_body = [[x, y]]
    direction = "RIGHT"

    # Food position
    food_x = round(random.randrange(0, WIDTH - snake_block) / CELL_SIZE) * CELL_SIZE
    food_y = round(random.randrange(0, HEIGHT - snake_block) / CELL_SIZE) * CELL_SIZE

    # Score
    score = 0

    while not game_over:
        while game_close:
            screen.fill(BLACK)
            game_over_text = game_over_font.render("Game Over!", True, RED)
            screen.blit(game_over_text, [WIDTH // 3, HEIGHT // 3])
            display_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Quit
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Continue
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"

        # Update snake's position
        if direction == "LEFT":
            x -= snake_block
        elif direction == "RIGHT":
            x += snake_block
        elif direction == "UP":
            y -= snake_block
        elif direction == "DOWN":
            y += snake_block

        # Check for collisions with boundaries
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Check for collisions with itself
        if [x, y] in snake_body[:-1]:
            game_close = True

        # Add new position to snake's body
        snake_body.append([x, y])

        # Check if food is eaten
        if x == food_x and y == food_y:
            score += 10
            food_x = round(random.randrange(0, WIDTH - snake_block) / CELL_SIZE) * CELL_SIZE
            food_y = round(random.randrange(0, HEIGHT - snake_block) / CELL_SIZE) * CELL_SIZE
        else:
            snake_body.pop(0)  # Remove the tail segment

        # Draw the game elements
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, [food_x, food_y, snake_block, snake_block])
        for segment in snake_body:
            pygame.draw.rect(screen, BLUE, [segment[0], segment[1], snake_block, snake_block])

        display_score(score)
        pygame.display.update()

        # Control the speed of the game
        clock.tick(snake_speed + (score/10))

    pygame.quit()
    quit()

# Start the game
game_loop()
