from tkinter import *


def button_press(number): 
    global equation__text
    equation__text += str(number)
    equation_label.set(equation__text)

def equals(): 
    global equation__text
    try:
        total = str(eval(equation__text))
        equation_label.set(total)
    except ZeroDivisionError:
        equation_label.set("Math Error")
        equation__text = ""
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation__text = ""
    
def clear(): 
    global equation__text
    equation__text = ""
    equation_label.set(equation__text)
    

window = Tk()
window.title("Calculator")
window.geometry("650x650")

equation__text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("Arial", 24), bg="white", fg="black", width=16, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text="1", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                 command= lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text="2", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text="3", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text="4", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text="5", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text="6", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text="7", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text="8", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text="9", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text="0", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= lambda: button_press(0))
button0.grid(row=3, column=1)


button_plus = Button(frame, text="+", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= lambda: button_press("+"))
button_plus.grid(row=0, column=3)

button_minus = Button(frame, text="-", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= lambda: button_press("-"))
button_minus.grid(row=1, column=3)

button_multiply = Button(frame, text="*", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= lambda: button_press("*"))
button_multiply.grid(row=2, column=3)

button_divide = Button(frame, text="/", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= lambda: button_press("/"))
button_divide.grid(row=3, column=3)

button_equals = Button(frame, text="=", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= equals)
button_equals.grid(row=3, column=0)

decimal = Button(frame, text=".", font=("Arial", 24), bg="white", fg="black", width=9, height=4,
                    command= lambda: button_press("."))
decimal.grid(row=3, column=2)

button_clear = Button(window, text="Clear", font=("Arial", 24), bg="white", fg="black", width=15, height=4,
                    command= clear)
button_clear.pack()





window.mainloop()