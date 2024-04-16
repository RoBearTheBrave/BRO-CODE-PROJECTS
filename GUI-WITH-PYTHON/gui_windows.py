# make a GUI with the TKinter module library that is included with Python

# import the tkinter module
import tkinter as tk


#understand the difference between a window and a widget
# widgets = GUI elements like buttons, labels, textboxes, etc.
# windows = the main window that contains all the widgets

window = tk.Tk() # instantiate an instance of a window
window.geometry("400x400") # set the dimensions of the window
window.title("My First Python GUI") # set the title of the window
window.config(background = "blue") # set the background color with names or hex values


# icon = tk.PhotoImage(file='GithubPic.jpeg') # create an image object, but Tkiner only supports GIF and PGM/PPM formats
# window.iconphoto(True, icon) # pass this photo to the window object


window.mainloop() # this will place window on computer screen and listen for events
