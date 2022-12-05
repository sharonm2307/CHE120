#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:31:15 2022

@author: sharonmoorthy
"""
# SM - Sharon Moorthy
# BL - Bhawna Lachman
# NY - Nitya Yadav
# WA - Wardah Anwer


# WA -  importing libraries
import pygame #WA - allows to import all the available pygame modules necessary into the package
import time #WA -  this module represents time in code within objects, numbers, and strings; provides functionality
import random #WA -  manipulates and generates random integers

pygame.init() # WA - initializes all imported pygame modules

# WA - defining colors 
# WA - each line of code, known has RGB (red, green, and blue) can be combined in various proportions to obtain any color in the visible spectrum
# WA - it additionally describes a colour as a tuple within the range of 0 and 255 that can be used on computer display
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# WA - screen size dimensions
screen_width = 600
screen_height = 400

# WA - initialising game window using the variables
screen = pygame.display.set_mode((screen_width, screen_height))
#WA - when the screen appears, it will be automatically labelled by 'Snake Game'
pygame.display.set_caption('Snake Game') 

# WA - # FPS (frames per second) controller 
clock = pygame.time.Clock() #WA - it initially creates an object to track time and is represented in milliseconds

#WA - frames of speed and movement; FPS can assist in controlling how fast or slow the "animation" must move 
snake_block = 10
snake_speed = 15

# WA - creating font objects by stating the font style and size
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
# BL - function for the user the score of what they are at
def game_score(score):  
     # BL - value is the way the score will be presented on the screen in terms of the colour and words
     value = score_font.render("Score: " + str(score), True, blue)  
     # BL - displays the score on the screen at a certain position
     screen.blit(value, [0, 0]) 
 
 
 
# BL - function for the snake to grow each time it eats the apple
def snake_growth(snake_block, snake_list): 
     # BL - for each block in the snake's body
     for x in snake_list: 
         # BL - pygame.draw.rect creates a rectangle on the screen in a white colour at the end of the previous block
         pygame.draw.rect(screen, white, [x[0], x[1], snake_block, snake_block]) 
 
 
# BL - function for let the user know when they lose
def message(text, color): 
     # BL - this is for the way the message will be presented on the screen
     msg_type = font_style.render(text, True, color) 
     # BL - displays the message on the screen at a certain position
     screen.blit(msg_type, [screen_width / 6, screen_height / 3]) 
 
 
# BL - function for the game to continue or stop under certain conditions
def game_loop():
     # BL - these are variables for when the game is running
     game_over = False 
     # BL - conditions for when the game is running
     close_game = False 
     
     # BL - this is where the snake will start in terms of the horizontal direction
     x1 = screen_width / 2 
     # BL - this is the same but in the vertical direction
     y1 = screen_height / 2 
     
     # BL - these are variables where the position changes depending on the keys the user chooses, this is in the horizontal direction, at the start it is zero
     x1_movement = 0 
     # BL - this is new position of the snake in the vertical direction, at the start it is zero
     y1_movement = 0 
     
     # BL - at the start of the game, the list will be empty since there is no growth yet
     snake_List = [] 
     # BL - at the beginning of the game, the snake starts with one block
     snake_length = 1 
     
     # BL - this is the random position that the computer generates for the x-direction for the apple to be placed
     x_food = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0 
     # BL - this is the y-direction for the apple's location, both combined will produce a coordinate for the apple's position
     y_food = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0 
 
     while not game_over:
 
         #NY-the game is still not over.
         while close_game == True: 
             #NY-filling the screen with black colour.
             screen.fill(black) 
             #NY-prints "You Lost! Press C-Play Again or Q-Quit" message with blue ink.
             message("You Lost! Press C-Play Again or Q-Quit", blue)
             #NY-1 subtracted from the length is the new score now
             game_score(snake_length - 1)
             #NY-display is updated according to the score.
             pygame.display.update()

             #NY-loop for the functions executed by pressing the listed keys by the user
             for event in pygame.event.get(): 
                 #NY-if the user taps the down key
                 if event.type == pygame.KEYDOWN:
                     #NY-then tap q key
                     if event.key == pygame.K_q: 
                         #NY-game gets over
                         game_over = True 
                         close_game = False
                    
                     #NY-if the user taps c key then the game keeps on playing
                     if event.key == pygame.K_c: 
                         game_loop()
 
         #NY-loop for the functions executed by pressing the listed keys by the user                 
         for event in pygame.event.get(): 
           #NY-if the user taps QUIT then the game is over
           if event.type == pygame.QUIT: 
               game_over = True  
           #NY-if down key is pressed
           if event.type == pygame.KEYDOWN: 
               #NY-the user taps on LEFT
               if event.key == pygame.K_LEFT: 
                   #NY-the snake moves towards left (a negative sign is used as the snake goes in the negative(left) direction)
                   x1_movement = -snake_block 
                   #NY-variable y1 is 0 as the snake doesn't move vertically
                   y1_movement = 0 
               #NY-the user taps on RIGHT
               elif event.key == pygame.K_RIGHT: 
                   #NY-the snake moves towards right
                   x1_movement = snake_block 
                   #NY-variable y1 is 0 as the snake doesn't move vertically
                   y1_movement = 0 
               #NY-the user taps on UP
               elif event.key == pygame.K_UP: 
                   #NY-the snake moves upwards (a negative sign is used as the snake goes in the negative(up) direction)
                   y1_movement = -snake_block 
                   #NY-variable x1 is 0 as the snake doesn't move horizontally
                   x1_movement = 0 
               #NY-the user taps on DOWN
               elif event.key == pygame.K_DOWN: 
                   #NY-the snake moves downwards
                   y1_movement = snake_block 
                   #NY-variable x1 is 0 as the snake doesn't move horizontally
                   x1_movement = 0 
        
 
         # SM - if the snake touches the border: 
         if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
          # SM - game over
          close_game = True 
          
         # SM - movement of the snake in the x direction     
         x1 += x1_movement 
         # SM - movement of the snake in the y direction 
         y1 += y1_movement 
         # SM - color of the background screen
         screen.fill(black) 
         # S.M. - draw a rectangle [location, color, [x_coordinate, y_coordinate, width, height]]
         pygame.draw.rect(screen, red, [x_food, y_food, snake_block, snake_block]) 
         # SM - list containing the added snake heads that appear each time the snake eats food
         snake_head = [] 
         # SM - add the new snake head to the list causing the snake to grow by one block
         snake_head.append(x1) 
         snake_head.append(y1)
         # SM - add the list snake_head to the snake_List so all the snake blocks are in the snake_List
         snake_List.append(snake_head) 
         # SM - if the length of the snake_List is greater than the snake length, delete the first item in the list
         if len(snake_List) > snake_length: 
             del snake_List[0]
 
         # SM - for variable x in every value of the list, up until the last one,
         for x in snake_List[:-1]:
            # SM - if the snake collides with itself, the game ends
            if x == snake_head:
                close_game = True
                
         # SM - calling the snake_growth function
         snake_growth(snake_block, snake_List)
         # SM - calling the game_score function, the score is the value of the snake length minus 1, since the snake already starts with one block
         game_score(snake_length - 1)
         # SM - making changes to the display screen
         pygame.display.update()
 
         if x1 == x_food and y1 == y_food: 
            # SM - randomly generate a new x_coordinate for the food (move the location)
            x_food = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0 
            # SM - randomly generate a new y_coordinate
            y_food = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            # SM - when the snake eats the food, increase the length of the snake by one
            snake_length += 1 
 
         # SM - pygame function for runtim speed of the game, snake_speed will be the number of frames that pass per second 
         clock.tick(snake_speed)
 
     # SM - closes pygame to ensure that it's not running after the while loop and after the game is over
     pygame.quit()
     # SM - built-in python command that closes the running program
     quit()
 
#SM - calling the game_loop function to run the game 
game_loop()
