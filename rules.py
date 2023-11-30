#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox


# In[ ]:


class WordGameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Word Game")

        self.rules_button = tk.Button(master, text="Game Rules", command=self.show_rules)
        self.rules_button.pack(pady=10)

    def play_game(self):
        # call play_game function or integrate the game logic here
        print("Game is being played.")

    def show_rules(self):
        rules_text = (
            "Game Rules:\n\n"
            "Guess a five-letter word, you have one minute and five chances.\n\n"
            "Guess the five words:\n"
            "- If the characters are the same and in the same spot: Green\n"
            "- If the same but in different spots: Yellow\n"
            "- If not: Black, and gray it out on the keyboard\n"
            "- If all Green: user wins"
        )
        messagebox.showinfo("Game Rules", rules_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = WordGameGUI(root)
    root.mainloop()


# In[ ]:




