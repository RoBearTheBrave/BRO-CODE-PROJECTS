from tkinter import *
import random

window = Tk()
window.title("Tic Tac Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [0,0,0], [0,0,0], [0,0,0]

label = Label(text=f"Player {player} turn", font=("Arial", 24))
label.pack(side=TOP)

def next_turn(row, col):
    global player

    if buttons[row][col]["text"] == "" and check_winner() is False:
        buttons[row][col]["text"] = player

        if player == players[0]:
            
            buttons[row][col]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=f"Player {players[1]} turn")

            elif check_winner() is True:
                label.config(text=f"Player {players[0]} wins!")
            
            elif check_winner() == "Tie":
                label.config(text="It's a tie!")

        else:
            
            buttons[row][col]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=f"Player {players[0]} turn")

            elif check_winner() is True:
                label.config(text=f"Player {players[1]} wins!")
            
            elif check_winner() == "Tie":
                label.config(text="It's a tie!")

def check_winner():
    for row in range(3): #check the horizontal rows for a win
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True
        
    for col in range(3): #check the vertical columns for a win
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return True


    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    
    elif empty_spaces() is False:
        return "Tie"
    
    else:
        return False
    
def empty_spaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def new_game(): 
    global player

    player = random.choice(players)

    label.config(text=f"Player {player} turn")

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="") 



reset_button = Button(text="New Game?", font=("Arial", 24), command=new_game)
reset_button.pack(side=TOP)

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=("Arial", 24), width=5, height=2, 
                                   command= lambda row=row, col=col: next_turn(row, col))
        buttons[row][col].grid(row=row, column=col)

window.mainloop()