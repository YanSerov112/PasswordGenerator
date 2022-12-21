import random
from tkinter import *

def rGnrt():
    PWNAns = []
    PWCS = random.randint(0,3)
    PWNTall = random.randint(11,20)
    PWLTall = random.randint(2,7)
    
    for PWN in range(int(PWNTall)):
        PWN = random.randint(0,9)
        PWNAns.append(PWN)
    
    PWL = random.randint(0,9)
    if PWCS == 0:
        PWCS = "-"
    elif PWCS == 1:
        PWCS = "_"
    elif PWCS == 2:
        PWCS = "!"
    elif PWCS == 3:
        PWCS = "@"
    
    for PWN in range(int(PWLTall)):
        PWN = random.randint(0,9)
        if PWL == 0:
            PWL = "F"
        elif PWL == 1:
            PWL = "I"
        elif PWL == 2:
            PWL = "p"
        elif PWL == 3:
            PWL = "J"
        elif PWL == 4:
            PWL = "Q"
        elif PWL == 5:
            PWL = "u"
        elif PWL == 6:
            PWL = "W"
        elif PWL == 7:
            PWL = "x"
        elif PWL == 8:
            PWL = "Y"
        elif PWL == 9:
            PWL = "z"
        PWNAns.insert(random.randint(0, int(PWNTall)), PWL)

    PWNAns.insert(random.randint(1, int(PWNTall) - 2), PWCS)
    PWNANS = ''.join(map(str, PWNAns))
    print(PWNANS)
    password["text"] = PWNANS


root = Tk()
root['bg'] = 'white'
root.title = "Password Generator"
root.geometry("250x200")
root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg='yellow')
frame.place(relx=0.15, rely =0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Password generator', bg='yellow')
title.pack()
btn = Button(frame, text='Regenerate', bg='orange', command=rGnrt)
btn.pack(side=BOTTOM)
password = Label(frame, text='Password Here', bg='orange')
password.pack()

root.mainloop()