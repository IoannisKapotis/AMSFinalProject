#!/usr/bin/env python
# coding: utf-8

# In[53]:


import numpy as np
import pandas as pd
import random
import json


# In[ ]:


#？

#with open('path/to/words.json', 'r') as file:
#data = json.load(file)


# In[1]:


#？
#pip install english-words


# In[75]:


# can be modified

dictionary = ["apple", "banana", "cherry", "delta", "elephant", "falcon", "giraffe", "happy", "igloo"]

def choose_random_word():
    # select a random word from the dictionary
    random_word = random.choice(dictionary)

    # ensure the selected word is five letters long
    while len(random_word) != 5:
        random_word = random.choice(dictionary)

    return random_word


# In[76]:


# example usage:
target_word = choose_random_word()
# print the target word before the game
print(f"The target word is: {target_word}")  


# In[ ]:





# In[77]:


# code from Thomas- show the color

def update_game_state(actual_word, user_guess, gylist):
    # Find all green letters
    for gcNum, guessChar in enumerate(user_guess):
        for acNum, acChar in enumerate(actual_word):
            if guessChar == acChar and gcNum == acNum:
                gylist[gcNum] = 'g'

    for acNum, acChar in enumerate(actual_word):
        if gylist[acNum] != 'g':
            for gcNum, guessChar in enumerate(user_guess):
                if guessChar == acChar and gylist[gcNum] != 'g':
                    gylist[gcNum] = 'y'
    
                    break

    return gylist


# In[ ]:





# In[78]:


#main game
def play_game():
    target_word = choose_random_word()
    max_guesses = 5
    current_guess = 0
    gylist = ['b', 'b', 'b', 'b', 'b']


    while current_guess < max_guesses:
        # get user input for the guess
        user_guess = input("Guess a five-letter word: ").lower()

        # check if the guess is valid
        if len(user_guess) != 5 or user_guess not in dictionary:
            print("Invalid guess. Please enter a valid five-letter word.")
            continue

        # update game state based on the user's guess
        gylist = update_game_state(target_word, user_guess, gylist)

        # print feedback to the user
        print(f"Feedback: {gylist}")

        # check if the user guessed the word
        if 'b' not in gylist:
            print(f"Congratulations! You guessed the correct word: {target_word}.")
            break
        else:
            print("Incorrect guess. Keep trying!")

        current_guess += 1

    # check if the player ran out of guesses
    if current_guess == max_guesses:
        print(f"Sorry, you ran out of guesses. The correct word was {target_word}.")


# In[79]:


# example play the game
play_game()


# In[ ]:





# In[ ]:




