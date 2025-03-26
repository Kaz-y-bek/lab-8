import pygame
import random
pygame.init()
blue = (50, 153, 213)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
dis_width = 600
dis_height = 400
snake_block = 10
display = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()
font = pygame.font.SysFont("bahnschrift", 20)
def message(msg, color, x, y):
    text = font.render(msg, True, color)
    display.blit(text, [x, y])
def game_loop():
    q = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    snake_length = 1
    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10
    while not q:
        while game_close:
            display.fill(blue)
            message("Game Over!", red, dis_width / 4, dis_height / 3)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        q = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                q = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display, green, [food_x, food_y, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for x in snake_list:
            pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])
        pygame.display.update()
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10
            food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10
            snake_length += 1
        clock.tick(10)
    pygame.quit()
game_loop()

