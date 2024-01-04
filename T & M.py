import pygame
import time
import random

pygame.init()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set up the game window
width, height = 800, 600
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set up clock to control the game speed
clock = pygame.time.Clock()

# Set up Snake and Apple
snake_block = 10
snake_speed = 15
font = pygame.font.SysFont(None, 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    # Initialize Snake
    snake_list = []
    length_of_snake = 1

    # Initial position of the snake
    x1 = width / 2
    y1 = height / 2

    # Initial change in position
    x1_change = 0
    y1_change = 0

    # Initial position of the apple
    apple_size = 10
    apple_x = round(random.randrange(0, width - apple_size) / 10.0) * 10.0
    apple_y = round(random.randrange(0, height - apple_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            our_snake(snake_block, snake_list)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if the snake hits the wall
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_display.fill(black)

        # Draw the apple
        pygame.draw.rect(game_display, red, [apple_x, apple_y, apple_size, apple_size])

        # Update snake length
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake collides with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        # Check if the snake eats the apple
        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, width - apple_size) / 10.0) * 10.0
            apple_y = round(random.randrange(0, height - apple_size) / 10.0) * 10.0
            length_of_snake += 1

        pygame.display.update()

        # Set the game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
