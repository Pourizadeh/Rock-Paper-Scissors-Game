from random import randint
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("700x350")
# Create a list of play options
t = ["Rock", "Paper", "Scissors"]

def show_msg_rock():
    #assign a random play to the computer
    computer = t[randint(0,2)]
    if computer == "Rock":
        messagebox.showinfo("Result","You both chose Rock! Play again!")
    elif computer == "Paper":
        messagebox.showinfo("Result","You lose! Paper covers Rock!")
    else:
        messagebox.showinfo("Result","You win! Rock smashes Scissors!")
def show_msg_paper():
    computer = t[randint(0,2)]
    if computer == "Paper":
        messagebox.showinfo("Result","You both chose Paper! Play again!")
    elif computer == "Scissors":
        messagebox.showinfo("Result","You lose! Scissors cut Paper!")
    else:
        messagebox.showinfo("Result","You win! Paper covers Rock!")

def show_msg_scissors():
    computer = t[randint(0,2)]
    if computer == "Scissors":
        messagebox.showinfo("Result","You both chose Scissors! Play again!")
    elif computer == "Rock":
        messagebox.showinfo("Result","You lose! Rock smashes Scissors!")
    else:
        messagebox.showinfo("Result","You win! Scissors cuts Paper!")

Label(win, text= "Welcome to the Game!", font= ('Aerial 17 bold italic')).pack(pady= 30)

ttk.Button(win, text= "Rock", command=show_msg_rock).pack(pady= 20)
ttk.Button(win, text= "Paper", command=show_msg_paper).pack(pady= 20)
ttk.Button(win, text= "Scissors", command=show_msg_scissors).pack(pady= 20)
win.mainloop()

