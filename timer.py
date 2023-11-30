#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the Tkinter module
import tkinter as tk
from datetime import timedelta


# In[ ]:





# In[19]:


#timer
class TimerApp:
    #  object is created from the class
    def __init__(self, root):
        #set the title 
        self.root = root
        self.root.title("Timer")
        
        # create a StringVar to hold the time value
        self.time_var = tk.StringVar()
        self.time_var.set("01:00")
        
        # create a label to display the time
        self.label = tk.Label(root, textvariable=self.time_var, font=("Arial", 50))
        self.label.pack(padx=20, pady=20)

        # window size
        root.geometry("200x200")

        # countdown time can be modify
        self.seconds = 60

        # start the timer when the application launches
        self.start_timer()

        
    # initiates the timer by calling the update_timer method
    def start_timer(self):
        self.update_timer()
    
    # check if the remaining time is greater than 0
    def update_timer(self):
        if self.seconds > 0:
            self.seconds -= 1
            self.update_display()
            # update after 1000 milliseconds(1 second)
            self.root.after(1000, self.update_timer)  
   
    # format the remaining time into a string
    def update_display(self):
        minutes, seconds = divmod(self.seconds, 60)
        time_str = f"{minutes}:{seconds:02d}"
        # update the time displayed in the label
        self.time_var.set(time_str)

        
if __name__ == "__main__":
    # create the main Tkinter window
    root = tk.Tk()
    #  create an instance of the TimerApp class
    app = TimerApp(root)
    # run the Tkinter event loop
    root.mainloop()


# In[ ]:





# In[ ]:




