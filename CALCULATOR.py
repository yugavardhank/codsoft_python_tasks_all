from tkinter import *
import math

# globally declare the expression variable 
expression = "" 

# Function to update expression in the text entry box 
def press(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression) 

# Function to evaluate the final expression 
def equalpress(): 
    try: 
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    except: 
        equation.set(" error ") 
        expression = "" 

# Function to clear the contents of text entry box 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 

# Function to get the factors of the entered number
def get_factors(): 
    try: 
        global expression 
        num = int(expression)
        factors = [i for i in range(1, num + 1) if num % i == 0]
        equation.set(factors) 
        expression = "" 
    except ValueError: 
        equation.set(" error ") 
        expression = "" 

# Function to check if a number is prime
def is_prime():
    try:
        global expression
        num = int(expression)
        if num > 1:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    equation.set(f"{num} is not a prime number")
                    expression = ""
                    return
            equation.set(f"{num} is a prime number")
        else:
            equation.set(f"{num} is not a prime number")
        expression = ""
    except ValueError:
        equation.set(" error ")
        expression = ""

# Function to calculate square of the entered number
def square(): 
    try: 
        global expression 
        result = float(expression) ** 2
        equation.set(str(result)) 
        expression = "" 
    except ValueError: 
        equation.set(" error ") 
        expression = "" 

# Function to calculate square root of the entered number
def square_root(): 
    try: 
        global expression 
        result = math.sqrt(float(expression))
        equation.set(str(result)) 
        expression = "" 
    except ValueError: 
        equation.set(" error ") 
        expression = "" 

# Function to calculate cube of the entered number
def cube(): 
    try: 
        global expression 
        result = float(expression) ** 3
        equation.set(str(result)) 
        expression = "" 
    except ValueError: 
        equation.set(" error ") 
        expression = "" 

# Function to calculate cube root of the entered number
def cube_root(): 
    try: 
        global expression 
        result = float(expression) ** (1/3)
        equation.set(str(result)) 
        expression = "" 
    except ValueError: 
        equation.set(" error ") 
        expression = "" 

# Function to calculate factorial of the entered number
def factorial(): 
    try: 
        global expression 
        result = math.factorial(int(expression))
        equation.set(str(result)) 
        expression = "" 
    except ValueError: 
        equation.set(" error ") 
        expression = "" 

# Function to calculate sine of the entered number
def sine(): 
    try: 
        global expression 
        result = math.sin(math.radians(float(expression)))
        equation.set(str(result)) 
        expression = "" 
    except ValueError: 
        equation.set(" error ") 
        expression = "" 

# Function to calculate cosine of the entered number
def cosine(): 
    try: 
        global expression 
        result = math.cos(math.radians(float(expression)))
        equation.set(str(result)) 
        expression = "" 
    except ValueError: 
        equation.set(" error ") 
        expression = "" 

# Function to calculate tangent of the entered number
def tangent(): 
    try: 
        global expression 
        result = math.tan(math.radians(float(expression)))
        equation.set(str(result)) 
        expression = "" 
    except ValueError: 
        equation.set(" error ") 
        expression = "" 

# Function to calculate exponential of the entered number
def exponential():
    try:
        global expression
        result = math.exp(float(expression))
        equation.set(str(result))
        expression = ""
    except ValueError:
        equation.set(" error ")
        expression = ""

# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 

    # set the background colour of GUI window 
    gui.configure(background="black") 

    # set the title of GUI window 
    gui.title("Simple Calculator") 

    # set the configuration of GUI window 
    gui.geometry("260x210") 

    # StringVar() is the variable class we create an instance of this class 
    equation = StringVar() 

    # create the text entry box for showing the expression 
    expression_field = Entry(gui, textvariable=equation) 

    # grid method is used for placing the widgets at respective positions 
    # in table like structure 
    expression_field.grid(columnspan=4, ipadx=70)

    # create Buttons and place at a particular location inside the root window 
    # when user press the button, the command or function affiliated to that button is executed 
    button1 = Button(gui, text=' 1 ', fg='black', bg='red', command=lambda: press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 

    button2 = Button(gui, text=' 2 ', fg='black', bg='red', command=lambda: press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 

    button3 = Button(gui, text=' 3 ', fg='black', bg='red', command=lambda: press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 

    button4 = Button(gui, text=' 4 ', fg='black', bg='red', command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 

    button5 = Button(gui, text=' 5 ', fg='black', bg='red', command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 

    button6 = Button(gui, text=' 6 ', fg='black', bg='red', command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 

    button7 = Button(gui, text=' 7 ', fg='black', bg='red', command=lambda: press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 

    button8 = Button(gui, text=' 8 ', fg='black', bg='red', command=lambda: press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 

    button9 = Button(gui, text=' 9 ', fg='black', bg='red', command=lambda: press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 

    button0 = Button(gui, text=' 0 ', fg='black', bg='red', command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=1) 

    plus = Button(gui, text=' + ', fg='black', bg='red', command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=2, column=3) 

    minus = Button(gui, text=' - ', fg='black', bg='red', command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=3, column=3) 

    multiply = Button(gui, text=' * ', fg='black', bg='red', command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=4, column=3) 

    divide = Button(gui, text=' / ', fg='black', bg='red', command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=5, column=3) 

    equal = Button(gui, text=' = ', fg='black', bg='red', command=equalpress,height=1,width=7)
    equal.grid(row=5, column=2) 

    clear = Button(gui, text='Clear', fg='black', bg='red', command=clear, height=1, width=7) 
    clear.grid(row=5, column=0) 

    Decimal= Button(gui, text='.', fg='black', bg='red', command=lambda: press('.'), height=1, width=7) 
    Decimal.grid(row=6, column=3) 

    factors = Button(gui, text='Factors', fg='black', bg='red', command=get_factors, height=1, width=7) 
    factors.grid(row=6, column=2) 

    prime = Button(gui, text='Prime', fg='black', bg='red', command=is_prime, height=1, width=7) 
    prime.grid(row=6, column=0) 

    sqr = Button(gui, text='x²', fg='black', bg='red', command=square, height=1, width=7) 
    sqr.grid(row=7, column=0) 

    sqrt = Button(gui, text='√x', fg='black', bg='red', command=square_root, height=1, width=7) 
    sqrt.grid(row=7, column=1) 

    cube = Button(gui, text='x³', fg='black', bg='red', command=cube, height=1, width=7) 
    cube.grid(row=7, column=2) 

    cube_root = Button(gui, text='∛x', fg='black', bg='red', command=cube_root, height=1, width=7) 
    cube_root.grid(row=7, column=3) 

    factorial = Button(gui, text='x!', fg='black', bg='red', command=factorial, height=1, width=7) 
    factorial.grid(row=8, column=0) 

    sine = Button(gui, text='sin', fg='black', bg='red', command=sine, height=1, width=7) 
    sine.grid(row=8, column=1) 

    cosine = Button(gui, text='cos', fg='black', bg='red', command=cosine, height=1, width=7) 
    cosine.grid(row=8, column=2) 

    tangent = Button(gui, text='tan', fg='black', bg='red', command=tangent, height=1, width=7) 
    tangent.grid(row=8, column=3) 

    exponential = Button(gui, text='e^x', fg='black', bg='green', command=exponential, height=1, width=7) 
    exponential.grid(row=6, column=1) 

    # start the GUI 
    gui.mainloop()
