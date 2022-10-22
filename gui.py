import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT)

frame2 = tk.Frame(master=window, width=200, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT)


button = tk.Button(
    text="Click me!",
    width=15,
    height=2,
    bg="blue",
    fg="yellow",
)

button.place(x=5, y=0)
window.mainloop()