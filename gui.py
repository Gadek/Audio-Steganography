import tkinter as tk
from tkinter import filedialog as fd
from write import write_to_file
from read import read_from_file
import tkinter.scrolledtext as tkscrolled
filename_path_source= ""
filename_path_destination= ""
filename_path_reveal_from= ""

window = tk.Tk()
window.geometry("700x900")
window.title('Hide a message')
window.resizable(False, False)

def _type(key):
    print(io_text.get('1.0', 'end'))
    print(key)

def option(args):
    io_label.config(text=args)
    button.config(text=args)
    io_text.delete("1.0", "end")

    if args == "hide text":
        io_label.pack_forget()
        io_label.pack(anchor = tk.W, before=label)
        
        length_label.pack(anchor = tk.W, after=io_label)
        
        io_text.pack_forget()
        io_text.pack(anchor = tk.W, expand=tk.YES, fill=tk.BOTH, pady=(0, 10), after=length_label)

        set_length_label.pack_forget()
        secret_length.pack_forget()

        file_path_text_source.pack(anchor=tk.W, after=seed)
        open_file_btn_source.pack( anchor = tk.W, pady=(0,10), after=file_path_text_source)
        file_path_text_destination.pack(anchor=tk.W, after=open_file_btn_source)
        open_file_btn_destination.pack( anchor = tk.W, pady=(0,10), after=file_path_text_destination)
        file_path_text_reveal_from.pack_forget()
        open_file_btn_reveal_from.pack_forget()
    elif args == "reveal text":
        io_label.pack_forget()
        io_label.pack(anchor = tk.W)

        length_label.pack_forget()

        io_text.pack_forget()
        io_text.pack(anchor = tk.W, expand=tk.YES, fill=tk.BOTH, pady=(0, 10), after=io_label)


        set_length_label.pack( anchor = tk.W, after=seed )
        secret_length.pack( anchor = tk.W, pady=(0,10), after=set_length_label )

        file_path_text_source.pack_forget()
        open_file_btn_source.pack_forget()
        file_path_text_destination.pack_forget()
        open_file_btn_destination.pack_forget()
        file_path_text_reveal_from.pack(anchor=tk.W, after=secret_length)
        open_file_btn_reveal_from.pack( anchor = tk.W, pady=(0,10), after=file_path_text_reveal_from)

def hide_or_reveal(desition):
    if desition.get()==0: #hide
        write_to_file(filename_path_source, filename_path_destination, int(LSB.get()), int(cryptokey.get()), io_text.get('1.0', 'end'), int(seed.get()))
    else:
        message = read_from_file(filename_path_reveal_from, int(LSB.get()), int(cryptokey.get()), int(seed.get()), int(secret_length.get()))
        io_text.delete("1.0", "end")
        io_text.insert(tk.END, message)

def open_file(arg):
    if arg == "source":
        global filename_path_source
        filename_path_source = fd.askopenfilename()
        file_path_text_source.config(text=filename_path_source)
    elif arg == "destination":
        global filename_path_destination
        filename_path_destination = fd.askopenfilename()
        file_path_text_destination.config(text=filename_path_destination)
    elif arg == "reveal_from":
        global filename_path_reveal_from
        filename_path_reveal_from = fd.askopenfilename()
        file_path_text_reveal_from.config(text=filename_path_reveal_from)

desition = tk.IntVar()
option1 = tk.Radiobutton(window, text="hide", variable=desition, value=0, command=lambda: option("hide text"))
option1.pack( anchor = tk.N )
option2 = tk.Radiobutton(window, text="reveal", variable=desition, value=1, command=lambda: option("reveal text"))
option2.pack( anchor = tk.N )

left_frame = tk.Frame(window)
left_frame.pack(side = tk.LEFT,anchor = tk.N, padx=10, pady=10)


io_label = tk.Label(master=left_frame)
io_label.config(text="Text to hide. Click on text area to update length of message")
io_label.pack(anchor = tk.W)

length_label = tk.Label(master=left_frame)
length_label.config(text="Length of message")
length_label.pack(anchor = tk.W)

io_text = tkscrolled.ScrolledText(master=left_frame, height=12, width=35)
io_text.pack(anchor = tk.W, expand=tk.YES, fill=tk.BOTH, pady=(0, 10))
io_text.bind("<Button>", lambda event, arg=(0): length_label.config(text=len(io_text.get('1.0', 'end'))-1))

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

seed_label = tk.Label(left_frame)
seed_label.config(text="Set seed for random number generator (1-999)")
seed_label.pack( anchor = tk.W )

seed = tk.Spinbox(left_frame, from_=1, to=999)
seed.pack( anchor = tk.W, pady=(0,10) )

set_length_label = tk.Label(left_frame)
set_length_label.config(text="Set length of hidden text")

secret_length = tk.Spinbox(left_frame, from_=1, to=1000000)

file_path_text_source = tk.Label(master=left_frame)
file_path_text_source.config(text="Choose a source .wav file")
file_path_text_source.pack(anchor=tk.W)

open_file_btn_source = tk.Button(master=left_frame, text="Open a source wave file", command=lambda: open_file("source"))
open_file_btn_source.pack( anchor = tk.W, pady=(0,10))

file_path_text_destination = tk.Label(master=left_frame)
file_path_text_destination.config(text="Choose a destination .wav file")
file_path_text_destination.pack(anchor=tk.W)

open_file_btn_destination = tk.Button(master=left_frame, text="Open a destination file", command=lambda: open_file("destination"))
open_file_btn_destination.pack( anchor = tk.W, pady=(0,10))

file_path_text_reveal_from = tk.Label(master=left_frame)
file_path_text_reveal_from.config(text="Choose a source .wav file with hidden message")

open_file_btn_reveal_from = tk.Button(master=left_frame, text="Open a source file with hidden message", command=lambda: open_file("reveal_from"))

button = tk.Button(
    master=left_frame,
    text="hide text",
    width=15,
    height=2,
    bg="blue",
    fg="yellow",
    command=lambda: hide_or_reveal(desition)
)

button.pack( anchor = tk.W )
window.mainloop()