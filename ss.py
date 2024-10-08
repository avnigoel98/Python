import pyautogui
from tkinter import *

# ss = pyautogui.screenshot()
# ss.save("ss.png")


def take_ss():
    # print(entry.get())
    add_data = entry.get()
    path= add_data+"\\test.png"
    print(path)
    ss = pyautogui.screenshot()
    ss.save(path)

win = Tk()
win.title("Snipping tool")
win.geometry("600x500")
win.config(bg = "yellow")
win.resizable(False, False)

entry = Entry(win, font=('Time New Roman', 30))
entry.place(x = 20, height=70, width = 550, y = 50)


button = Button(win, text="Take SS", font=('Time New Roman', 50), command=take_ss)
button.place(x=100, y=180, height=80, width=400)

win.mainloop()



#https://pypi.org/project/pyinstaller/
#https://docs.python.org/3/library/tkinter.html
#https://pyautogui.readthedocs.io/en/latest/screenshot.html#the-screenshot-function