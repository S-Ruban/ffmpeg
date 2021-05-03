from tkinter import *
from tkinter import filedialog
import os


def get_input_file():
    in_file.set(filedialog.askopenfilename(filetypes=(("Video files", "*.mp4;*.flv;*.avi;*.mkv"),
                                                      ("All files", "*.*"))))
    input_file.config(text=in_file.get())


def get_output_dir():
    out_dir.set(filedialog.askdirectory())
    if(len(out_dir.get()) != 0):
        output_dir.config(text=out_dir.get())
    else:
        out_dir.set(os.getcwd())
        output_dir.config(text=os.getcwd())


def compress():
    # print("Input : " + in_file.get())
    # print("Output : " + out_dir.get() + "/" + filename.get() + ".mp4")
    os.system("ffmpeg -i \"" + in_file.get() + "\" -vcodec libx265 -crf 28 \"" +
              out_dir.get() + "/" + filename.get()+".mp4\"")


gui = Tk(className="Compress video file")
gui.geometry("600x200")

in_file = StringVar()
out_dir = StringVar()
out_dir.set(os.getcwd())

Label(gui, text="Input File : ").place(x=5, y=10)
input_file = Label(gui, text="", wraplength=350, justify="left")
input_file.place(x=60, y=10)
sel_if = Button(gui, text="Select Input File", width=20,
                height=1, command=get_input_file).place(x=425, y=7)

Label(gui, text="Output Directory : ").place(x=5, y=70)
output_dir = Label(gui, text=os.getcwd(), wraplength=350, justify="left")
output_dir.place(x=120, y=70)
sel_od = Button(gui, text="Select Output Directory", width=20,
                height=1, command=get_output_dir).place(x=425, y=67)

Label(gui, text="Output File Name : ").place(x=5, y=120)
filename = Entry(gui, width=50)
filename.place(x=125, y=120)
Label(gui, text=".mp4").place(x=425, y=120)

conv = Button(gui, text="Compress", width=10, height=1,
              command=compress).place(x=250, y=150)

gui.mainloop()
