import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import timedelta

import numpy as np
import random
import json 


#Menu Screen:
Menu = tk.Tk()
Menu.title("Bootleg Wordle Menu")
Menu.geometry("600x800")

Welcome_Message = tk.Label(Menu, text = "Welcome to the main menu of Bootleg Wordle! \n" 
                                       "Here, you can select a difficulty, and learn how to play.", 
                           font=('Times New Roman',18)
                          )
Welcome_Message.pack()

How_to_play = tk.Label(Menu, text="How to play:")
How_to_play.pack(pady=10)

Rules_Message = tk.Label(Menu, text="Wordle is a word guessing game.\n"
                                   "You have 6 guesses to match a randomly chosen word!\n"
                                   "Each guess must be 5 letters long.\n"
                                   "The color of the tiles will change to show how close\n"
                                   "your guess was to the word.",
                        font=('Times New Roman', 15)
                        )
Rules_Message.pack(pady=10)  


# define the difficulty label
Rules_Message.pack()
difficulty_var = tk.StringVar()

label_difficulty = tk.Label(Menu, text="Please select a Difficulty:", font=('Arial', 18))
label_difficulty.pack(pady=10)

style = ttk.Style()
style.configure("TRadiobutton", indicatorsize=0)

radio_easy = ttk.Radiobutton(Menu, text="Easy", variable=difficulty_var, value="Easy", style="TRadiobutton", padding=10)
radio_easy.pack()

radio_medium = ttk.Radiobutton(Menu, text="Medium", variable=difficulty_var, value="Medium", style="TRadiobutton", padding=10)
radio_medium.pack()

radio_hard = ttk.Radiobutton(Menu, text="Hard", variable=difficulty_var, value="Hard", style="TRadiobutton", padding=10)
radio_hard.pack()



#Define function to start the game when given difficulty level selection:
def start_game(difficulty):
    Menu.destroy()

#Define function to read selected difficulty and start game with that difficulty:
def select_difficulty(difficulty_var):
    difficulty = difficulty_var.get()
    if difficulty:
        start_game(difficulty)
    else:
        messagebox.showwarning("Difficulty Selection","Please select a difficulty level.")
        

Start_Game = tk.Button(Menu, text="Start Game", command=lambda:select_difficulty(difficulty_var))
Start_Game.pack()
Menu.mainloop()





#End of Menu -- Start of Game screen:

file_path = r'C:\Users\Dell\Downloads\words.json'
with open(file_path, 'r') as file:
    data = json.load(file)

#Creates GUI screen with title and dimension:
root = tk.Tk()
root.title("Bootleg Wordle")
root.geometry("600x800")


#Creates textbox in GUI to type guess in
textbox = tk.Text(root, height=2, font=('Arial',18))
textbox.pack(padx=20,pady=5)


#Label asking for guess:
label = tk.Label(root, text='Please Enter a Guess!', font=('Arial',18))
label.pack()


#Function that will be used inside to make the following keyboard work:
def insert_text(letter):
    current_text = textbox.get("1.0", "end-1c")
    new_text = current_text + letter
    textbox.delete("1.0", "end")
    textbox.insert("1.0", new_text)


#Creates button frame to hold keyboard buttons:
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

Alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"
buttons = []
#Places each button in qwerty order in button frame.
#Each button is assigned the "insert_text" command to actually write the letter when clicked:
for index, letter in enumerate(Alphabet):
    btnltr = tk.Button(buttonframe, text=letter, font=('Arial', 18), command=lambda l=letter: insert_text(l))
    if(index <=9):
        btnltr.grid(row=0, column=index, sticky=tk.W + tk.E)
        
    elif(index >=10 and index <=18):
        btnltr.grid(row=1, column=index-10, sticky=tk.W + tk.E)
        
    else:
        btnltr.grid(row=2, column=index-19, sticky=tk.W + tk.E)
    buttons.append(btnltr)
       
buttonframe.pack()

#Creates function for Backspace button:
def Backspace():
    textbox.delete("end-2c", "end")

btnDelete = tk.Button(buttonframe, text='Delete', font=('Arial',18),command=Backspace)
btnDelete.grid(row=2,column=7,columnspan=2,sticky=tk.W+tk.E)
buttonframe.pack()
#Creates function for clearing the test box after a guess is submitted:
def ClearText():
    textbox.delete("1.0", "end")

def Choose_Random_Word():
    RandomWord = random.choice(data).upper()
    return RandomWord
    
#Chooses Word   
actualWord = Choose_Random_Word()

# Initialize global turn variable
global turn
turn=1

def Actual_Game():
    
    global turn
    global actualWord

    #Function to check if all entries in a list are all equal
    def check(list):
        return all(i == list[0] for i in list)
    
    #Pulls the user's guess from the textbox; Makes it capitalalized and removes blank spaces:
    guess = textbox.get("1.0", "end-1c").upper().strip()
    Black = '#000000'
    Yellow = '#c8b653'
    Green = '#6ca965'
    
    #Colors = {'Black' : '#000000', 'Yellow':'#c8b653', Green:'#6ca965'}
    gylist = [Black,Black,Black,Black,Black]

    #If guess length isn't 5, don't run the game and tell the user:
    if len(guess)!=5:
        lose_Win_Length_label.config(text="Only 5 Letter Words!")
        
    #If 5 letter word is entered, play the game!:
    else:
        lose_Win_Length_label.config(text="")
        #Find all Green letters:
        if turn <=5:
            for gcNum, guessChar  in enumerate(guess):
                for acNum, acChar in enumerate(actualWord):
                    if (guessChar == acChar and gcNum == acNum):
                        gylist[gcNum] = Green
            
            #Find all Yellow letters
            for acNum, acChar in enumerate(actualWord):
                if (gylist[acNum] != Green):
                     for gcNum, guessChar  in enumerate(guess):
                        # Make sure character has not already been colored
                          if (guessChar == acChar and gylist[gcNum] == Black):
                              gylist[gcNum] = Yellow
                    
            #Once one yellow character has been found corresponding to a specific actual character, break inner-loop
                              break
            for i, letter in enumerate(guess):
                position = Alphabet.index(letter)
                current_color = buttons[position].cget("fg")
                if current_color != Green and current_color != Yellow and gylist[i]!=Black:
                    buttons[position].config(fg = gylist[i])
                elif current_color != Green and current_color != Yellow and gylist[i]==Black:
                    buttons[position].config(fg = '#808080')     
                elif current_color == Yellow and gylist[i]==Green:
                    buttons[position].config(fg = gylist[i])   
            
            #Makes Frame to layout the Wordle guesses vertically:
            GuessLabels = tk.Frame(root)
            GuessLabels.columnconfigure(3, weight=1)
            GuessLabels.columnconfigure(4, weight=1)
            GuessLabels.columnconfigure(5, weight=1)
        
            #Creates Label for each letter in guess, colored accordingly
            k=0
            for k in range(0,5):
                GuessLetter = tk.Label(GuessLabels, text= guess[k], font=('Arial',20),bg=gylist[k],width=4,height=2)
                GuessLetter.grid(row=turn, column=k, sticky=tk.W+tk.E, padx=5, pady=5)
                GuessLabels.pack()
            #Checks if all letters are color Green (You got the word!):
            if check(gylist) is True and gylist[0]==Green:
                lose_Win_Length_label.config(text=f"You win! The word was {actualWord}")
                btnSubmit.config(state=DISABLED)
            # Covers the case where all letters are black or yellow on last turn(You lost!):
            elif turn>=5:
                lose_Win_Length_label.config(text=f"You Lose! The word was {actualWord}")
                btnSubmit.config(state=DISABLED)
        
            #Moves to next turn
            turn +=1
            
            #Clears the textbox 
            ClearText()


btnfrm2 = tk.Frame(root)
btnfrm2.columnconfigure(0, weight=1)
btnfrm2.columnconfigure(1, weight=1)
btnfrm2.columnconfigure(2, weight=1)


#Creates Submit button that activates "Actual_Game"
btnSubmit = tk.Button(btnfrm2, text ='Guess',font=('Arial',18),command=Actual_Game)
btnSubmit.grid()
btnfrm2.pack()

#Creates a Label to tell the user if they win or lose, and to give error if not 5 character guess:
lose_Win_Length_label = tk.Label(root, text= "", font=('Arial',24))
lose_Win_Length_label.pack()

root.mainloop()

