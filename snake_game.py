#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 12:16:39 2022

@author: sharonmoorthy
"""
#Bhawna Lachman-BL

import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
screen_width = 600
screen_height = 400
 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 10
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def game_score(score): #function for the user the score of what they are at-BL 
    value = score_font.render("Score: " + str(score), True, blue) #value is the way the score will be presented on the screen in terms of the colour and words-BL 
    screen.blit(value, [0, 0]) #displays the score on the screen at a certain position-BL
 
 
 
def snake_growth(snake_block, snake_list): #function for the snake to grow each time it eats the apple-BL
    for x in snake_list: #for each block in the snake's body-BL
        pygame.draw.rect(screen, white, [x[0], x[1], snake_block, snake_block]) #pygame.draw.rect creates a rectangle on the screen in a white colour at the end of the previous block-BL
 
 
def message(text, color): #function for let the user know when they lose-BL
    msg_type = font_style.render(text, True, color) #this is for the way the message will be presented on the screen-BL
    screen.blit(msg_type, [screen_width / 6, screen_height / 3]) #displays the message on the screen at a certain position-BL
 
 
def game_loop(): #function for the game to continue or stop under certain conditions-BL
    game_over = False #these are variables for when the game is running-BL
    close_game = False #conditions for when the game is running-BL
 
    x1 = screen_width / 2 #this is where the snake will start in terms of the horizontal direction-BL
    y1 = screen_height / 2 #this is the same but in the vertical direction-BL
 
    x1_movement = 0 #these are variables where the position changes depending on the keys the user chooses, this is in the horizontal direction, at the start it is zero-BL
    y1_movement = 0 #this is new position of the snake in the vertical direction, at the start it is zero-BL
 
    snake_List = [] #at the start of the game, the list will be empty since there is no growth yet-BL
    snake_length = 1 #at the beginning of the game, the snake starts with one block-BL
 
    x_food = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0 #this is the random position that the computer generates for the x-direction for the apple to be placed-BL
    y_food = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0 #this is the y-direction for the apple's location, both combined will produce a coordinate for the apple's position-BL
 
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
 
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            close_game = True
        x1 += x1_movement
        y1 += y1_movement
        screen.fill(black)
        pygame.draw.rect(screen, red, [x_food, y_food, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > snake_length:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_head:
                close_game = True
 
        snake_growth(snake_block, snake_List)
        game_score(snake_length - 1)
 
        pygame.display.update()
 
        if x1 == x_food and y1 == y_food:
            x_food = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            y_food = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            snake_length += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
game_loop()
