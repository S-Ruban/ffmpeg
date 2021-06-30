import os
from tkinter import *
from tkinter import filedialog


def convert(filename):
    os.system(
        'ffmpeg -i "'
        + filename
        + '" -ab 128k -map_metadata 0 -id3v2_version 3 "'
        + filename[:-4]
        + 'mp3"'
    )
    os.system('del "' + filename.replace("/", "\\") + '"')


def conv():
    gui.call("wm", "attributes", ".", "-topmost", True)
    files = filedialog.askopenfilename(multiple=True)
    files = gui.tk.splitlist(files)
    for f in files:
        convert(f)


gui = Tk(className="Compress video file")
gui.geometry("200x100")
conv = Button(gui, text="Convert", width=10, height=1, command=conv).place(x=50, y=40)

gui.mainloop()
