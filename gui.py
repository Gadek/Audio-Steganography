import tkinter as tk
from tkinter import filedialog as fd
from write import write_to_file
from read import read_from_file
filename_path_source= ""
filename_path_destination= ""

window = tk.Tk()
window.geometry("700x550")
window.title('Hide a message')
window.resizable(False, False)

def option(args):
    io_label.config(text=args)
    button.config(text=args)


desition = tk.IntVar()
option1 = tk.Radiobutton(window, text="hide", variable=desition, value=0, command=lambda: option("hide text"))
option1.pack( anchor = tk.N )
option2 = tk.Radiobutton(window, text="reveal", variable=desition, value=1, command=lambda: option("reveal text"))
option2.pack( anchor = tk.N )

left_frame = tk.Frame(window)
left_frame.pack(side = tk.LEFT,anchor = tk.N, padx=10, pady=10)


io_label = tk.Label(master=left_frame)
io_label.config(text="Text to hide")
io_label.pack(anchor = tk.W)

io_text = tk.Text(master=left_frame, height=5, width=35)
io_text.pack(anchor = tk.W, expand=tk.YES, fill=tk.BOTH, pady=(0, 10))


label = tk.Label(left_frame)
label.config(text="Number of LSB used")
label.pack( anchor = tk.W )

LSB = tk.IntVar()
R1 = tk.Radiobutton(left_frame, text="1", variable=LSB, value=1)
R1.pack( anchor = tk.W )
R2 = tk.Radiobutton(left_frame, text="2", variable=LSB, value=2)
R2.pack( anchor = tk.W )
R3 = tk.Radiobutton(left_frame, text="3", variable=LSB, value=3)
R3.pack( anchor = tk.W )
R4 = tk.Radiobutton(left_frame, text="4", variable=LSB, value=4)
R4.pack( anchor = tk.W, pady=(0,10) )

cryptokey_label = tk.Label(left_frame)
cryptokey_label.config(text="Set cryptographic key from 0 to 6")
cryptokey_label.pack( anchor = tk.W )

cryptokey = tk.Spinbox(left_frame, from_=0, to=6)
cryptokey.pack( anchor = tk.W, pady=(0,10) )

def open_file(arg):
    if arg == "source":

        global filename_path_source
        filename_path_source = fd.askopenfilename()
        file_path_text_source.config(text=filename_path_source)
    else:
        global filename_path_destination
        filename_path_destination = fd.askopenfilename()
        file_path_text_destination.config(text=filename_path_destination)

file_path_text_source = tk.Label(master=left_frame)
file_path_text_source.config(text="Choose a source .wav file")
file_path_text_source.pack(anchor=tk.W)

open_file_btn = tk.Button(master=left_frame, text="Open a source wave file", command=lambda: open_file("source"))
open_file_btn.pack( anchor = tk.W, pady=(0,10))

file_path_text_destination = tk.Label(master=left_frame)
file_path_text_destination.config(text="Choose a destination .wav file")
file_path_text_destination.pack(anchor=tk.W)

open_file_btn = tk.Button(master=left_frame, text="Open a destination file", command=lambda: open_file("destination"))
open_file_btn.pack( anchor = tk.W, pady=(0,10))

def hide_or_reveal(desition):
    if desition.get()==0: #hide
        write_to_file(filename_path_source, filename_path_destination, LSB.get(), cryptokey.get(), io_text.get('1.0', 'end'))
    else:
        read_from_file(filename_path_source, LSB.get(), cryptokey.get())

button = tk.Button(master=left_frame,
    text="reveal text",
    width=15,
    height=2,
    bg="blue",
    fg="yellow",
    command=lambda: hide_or_reveal(desition)
)

button.pack( anchor = tk.W )
window.mainloop()