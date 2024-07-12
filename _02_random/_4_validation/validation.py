import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment

    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
    for i in range(5):
        if random_number == 1:
            messagebox.showinfo(title='', message='You have good hair!')
        elif random_number == 2:
            messagebox.showinfo(title='', message='You smell nice')
        elif random_number == 3:
            messagebox.showinfo(title='', message='Youre face is good!')
        if random_number == 1:
            messagebox.showinfo(title='', message='You are built like a door')
        if random_number == 1:
            messagebox.showinfo(title='', message='You wear good cloths')
