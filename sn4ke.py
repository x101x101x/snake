import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (52, 235, 158)
GREEN = (235, 52, 232)

# Snake and food
snake_block = 20
snake_speed = 10  # Starting speed

# Initialize clock
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 50)



def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    lines = msg.split('\n')
    line_height = 50
    start_y = height/3
    for i, line in enumerate(lines):
        mesg = font.render(line, True, color)
        text_rect = mesg.get_rect(center=(width/2, start_y + i*line_height))
        window.blit(mesg, text_rect)


def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    current_speed = snake_speed

    while not game_over:

        while game_close == True:
            window.fill('pink')
            message(f"You Lost!\nScore: {length_of_snake - 1}\nQ-Quit or C-Play Again", 'black')
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
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

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill('pink')
        pygame.draw.rect(window, RED, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        # Display current score
        score = font.render(f"Score: {length_of_snake - 1}", True, WHITE)
        window.blit(score, [0, 0])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            length_of_snake += 1

            # Increase speed every 5 points
            if length_of_snake % 5 == 0:
                current_speed += 1

        clock.tick(current_speed)

    pygame.quit()
    quit()


gameLoop()