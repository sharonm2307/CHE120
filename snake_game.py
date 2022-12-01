#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 12:16:39 2022

@author: sharonmoorthy
"""
# SM - Sharon Moorthy
# NY - Nitya 
# WA - Wardah Anwer

# WA -  importing libraries
import pygame
import time
import random
 
# WA - initialising pygame
pygame.init()

# WA - defining colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
# WA - screen size
screen_width = 600
screen_height = 400

# WA - # Initialising game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# WA - # FPS (frames per second) controller
clock = pygame.time.Clock()

#WA - frames of speed and movement
snake_block = 10
snake_speed = 10
 
# WA - creating font objects
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def game_score(score):
    value = score_font.render("Score: " + str(score), True, blue)
    screen.blit(value, [0, 0])
 
 
 
def snake_growth(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, white, [x[0], x[1], snake_block, snake_block])
 
 
def message(text, color):
    msg_type = font_style.render(text, True, color)
    screen.blit(msg_type, [screen_width / 6, screen_height / 3])
 
 
def game_loop():
    game_over = False
    close_game = False
 
    x1 = screen_width / 2
    y1 = screen_height / 2
 
    x1_movement = 0
    y1_movement = 0
 
    snake_List = []
    snake_length = 1
 
    x_food = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    y_food = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while close_game == True:
            screen.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", blue)
            game_score(snake_length - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        close_game = False
                    if event.key == pygame.K_c:
                        game_loop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_movement = -snake_block
                    y1_movement = 0
                elif event.key == pygame.K_RIGHT:
                    x1_movement = snake_block
                    y1_movement = 0
                elif event.key == pygame.K_UP:
                    y1_movement = -snake_block
                    x1_movement = 0
                elif event.key == pygame.K_DOWN:
                    y1_movement = snake_block
                    x1_movement = 0
 
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0: #SM - if the snake touches the border:
            close_game = True #SM - game over
        x1 += x1_movement #SM - movement of the snake in the x direction 
        y1 += y1_movement #SM - movement of the snake in the y direction 
        screen.fill(black) #SM - color of the background screen
        pygame.draw.rect(screen, red, [x_food, y_food, snake_block, snake_block]) #S.M. - draw a rectangle [location, color, [x_coordinate, y_coordinate, width, height]]
        snake_head = [] #SM - list containing the added snake heads that appear each time the snake eats food
        snake_head.append(x1) #SM - add the new snake head to the list 
        snake_head.append(y1)
        snake_List.append(snake_head) #SM - add the list snake_head to the snake_List so all the snake blocks are in the snake_List
        if len(snake_List) > snake_length: #SM - if the length of the snake_List is greater than the snake length
            del snake_List[0]
 
        for x in snake_List[:-1]: #SM - for variable x in every value of the list, up until the last one,
            if x == snake_head: #SM - if the snake collides with itself, the game ends
                close_game = True
 
        snake_growth(snake_block, snake_List) #SM - calling the snake_growth function, 
        game_score(snake_length - 1) #SM - calling the game_score function, the score is the value of the snake length minus 1, since the snake already starts with one block
 
        pygame.display.update() #SM - making changes to the display screen
 
        if x1 == x_food and y1 == y_food: #SM - if the position of the snake equals the position of the food (if the snake eats the food):
            x_food = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0 #SM - randomly generate a new x_coordinate for the food (move the location)
            y_food = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0 #SM - randomly generate a new y_coordinate "         "
            snake_length += 1 #SM - when the snake eats the food, increase the length of the snake by one
 
        clock.tick(snake_speed) #SM - pygame function for runtim speed of the game, snake_speed will be the number of frames that pass per second 
 
    pygame.quit() #SM - closes pygame to ensure that it's not running after the while loop and after the game is over
    quit() #SM - built-in python command that closes the running program
 
game_loop() #SM - calling the game_loop function
