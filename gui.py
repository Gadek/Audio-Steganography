import tkinter as tk
from tkinter import filedialog as fd
window = tk.Tk()
window.geometry("700x450")
window.title('Hide a message')
window.resizable(False, False)


left_frame = tk.Frame(window)
left_frame.pack(side = tk.LEFT,anchor = tk.N, padx=10, pady=10)


inputtxt = tk.Label(master=left_frame)
inputtxt.config(text="Text to hide")
inputtxt.pack( anchor = tk.W )

E1 = tk.Text(master=left_frame, height=5, width=35)
E1.pack( anchor = tk.W , expand=tk.YES, fill=tk.BOTH, pady=(0,10))

var = tk.IntVar()
label = tk.Label(left_frame)
label.config(text="Number of LSB used")
label.pack( anchor = tk.W )

R1 = tk.Radiobutton(left_frame, text="1", variable=var, value=1)
R1.pack( anchor = tk.W )
R2 = tk.Radiobutton(left_frame, text="2", variable=var, value=2)
R2.pack( anchor = tk.W )
R3 = tk.Radiobutton(left_frame, text="3", variable=var, value=3)
R3.pack( anchor = tk.W )
R4 = tk.Radiobutton(left_frame, text="4", variable=var, value=4)
R4.pack( anchor = tk.W, pady=(0,10) )

# file_path=tk.StringVar()
def open_file():
    filename = fd.askopenfilename()
    file_path_text.config(text=filename)


open_file_btn = tk.Button(master=left_frame, text="Open a wave file", command=open_file)
open_file_btn.pack( anchor = tk.W,)

file_path_text = tk.Label(master=left_frame)
file_path_text.config(text="Choose a .wav file")
file_path_text.pack(anchor=tk.W, pady=(0,10))

button = tk.Button(master=left_frame,
    text="Click me!",
    width=15,
    height=2,
    bg="blue",
    fg="yellow",
)

button.pack( anchor = tk.W )
window.mainloop()