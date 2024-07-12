import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    simpledialog.askstring(title='MAGIC 8 BALL', prompt='Ask any question here:')
    # Make a variable and initialize it to a random number between 0 and 3
    rand = random.randint(0,3)
    # If the random number is 0
    if rand == 0:
        messagebox.showinfo(title='', message='Yes')
        # tell the user "Yes"

    # If the random number is 1
    if rand == 1:
        messagebox.showinfo(title='', message='Yes')
        # tell the user "No"

    # If the random number is 2
    if rand == 2:
        messagebox.showinfo(title='', message='I honestly have no clue')
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    if rand == 3:
        messagebox.showinfo(title='', message='ERROR, WHAT THE SIGMA')
        # write your own answer
