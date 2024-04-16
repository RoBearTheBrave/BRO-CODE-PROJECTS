from tkinter import *

# Labels are area widgets that are used to display text or images

window = Tk()

label = Label(window, # pass in options as arguments to the Label constructor
              text = "Hello World", 
              font=('Arial', 40, 'bold'), 
              fg='#00FF00', 
              bg='black') # create a label widget with the window as a master container


label.pack() # pack the label widget into the window, deffaults to the top center of the window
label.place(x=100, y=100) # place the label down 100 px and to the right 100 px



window.mainloop()