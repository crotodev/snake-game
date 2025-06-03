import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# Define game window properties
WIDTH, HEIGHT = 600, 400

# Create the display surface
game_display: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock: pygame.time.Clock = pygame.time.Clock()

# Define snake properties
SNAKE_SIZE: int = 10
SNAKE_SPEED: int = 15

# Define fonts
MSG_FONT: pygame.font.Font = pygame.font.SysFont("Arial", 20)
SCORE_FONT: pygame.font.Font = pygame.font.SysFont("Arial", 15)


def print_score(score: int) -> None:
    """
    Displays the current score on the game window.

    :param score: The current score to be displayed.
    """
    text = SCORE_FONT.render("Score: " + str(score), True, ORANGE)
    game_display.blit(text, [0, 0])


def draw_snake(snake_size: int, snake_pixels: list[list[int]]) -> None:
    """
    Draws the snake on the game window.

    :param snake_size: The size of each square that makes up the snake.
    :param snake_pixels: A list of positions of each square that makes up the snake.
    """
    for pixels in snake_pixels:
        pygame.draw.rect(game_display, WHITE, [pixels[0], pixels[1], snake_size, snake_size])


def run_game() -> None:
    """
    The main function to run the snake game. It initializes the game and handles the game loop.
    """
    game_over: bool = False
    game_close: bool = False

    x: int = WIDTH / 2
    y: int = HEIGHT / 2

    x_speed: int = 0
    y_speed: int = 0

    snake_pixels: list[list[int]] = []
    snake_length: int = 1

    target_x: float = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
    target_y: float = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(BLACK)
            game_over_msg = MSG_FONT.render("Game Over!", True, RED)
            game_display.blit(game_over_msg, [WIDTH / 3, HEIGHT / 3])
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -SNAKE_SIZE
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = SNAKE_SIZE
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -SNAKE_SIZE
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = SNAKE_SIZE

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(BLACK)
        pygame.draw.rect(game_display, ORANGE, [target_x, target_y, SNAKE_SIZE, SNAKE_SIZE])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        draw_snake(SNAKE_SIZE, snake_pixels)
        print_score(snake_length - 1)

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x: float = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
            target_y: float = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


if __name__ == "__main__":
    run_game()
