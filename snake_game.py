#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 12:16:39 2022

@author: sharonmoorthy
"""

import pygame
import time
import random
 
pygame.init()

#Colours 
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
 
        while close_game == True: #NY-the game is still not over.
            screen.fill(black) #NY-filling the screen with black colour.
            message("You Lost! Press C-Play Again or Q-Quit", blue)#NY-prints "You Lost! Press C-Play Again or Q-Quit" message with blue ink.
            game_score(snake_length - 1)#NY-1 subtracted from the length is the new score now
            pygame.display.update()#NY-display is updated according to the score.
 
            for event in pygame.event.get(): #NY-loop for the functions executed by pressing the listed keys by the user
                if event.type == pygame.KEYDOWN: #NY-if the user taps the down key
                    if event.key == pygame.K_q: #NY-then tap q key
                        game_over = True #NY-game gets over
                        close_game = False
                    if event.key == pygame.K_c: #NY-if the user taps c key then the game keeps on playing
                        game_loop()
 
        for event in pygame.event.get(): #NY-loop for the functions executed by pressing the listed keys by the user
            if event.type == pygame.QUIT: #NY-if the user taps QUIT then the game is over
                game_over = True
            if event.type == pygame.KEYDOWN: #NY-if down key is pressed
                if event.key == pygame.K_LEFT: #NY-the user taps on LEFT
                    x1_movement = -snake_block #NY-the snake moves towards left (a negative sign is used as the snake goes in the negative(left) direction)
                    y1_movement = 0 #NY-variable y1 is 0 as the snake doesn't move vertically
                elif event.key == pygame.K_RIGHT: #NY-the user taps on RIGHT
                    x1_movement = snake_block #NY-the snake moves towards right
                    y1_movement = 0 #NY-variable y1 is 0 as the snake doesn't move vertically
                elif event.key == pygame.K_UP: #NY-the user taps on UP
                    y1_movement = -snake_block #NY-the snake moves upwards (a negative sign is used as the snake goes in the negative(up) direction)
                    x1_movement = 0 #NY-variable x1 is 0 as the snake doesn't move horizontally
                elif event.key == pygame.K_DOWN: #NY-the user taps on DOWN
                    y1_movement = snake_block #NY-the snake moves downwards
                    x1_movement = 0 #NY-variable x1 is 0 as the snake doesn't move horizontally
 
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
