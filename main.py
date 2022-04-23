from tkinter import *

root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry('720x360')
root.title("Minesweeper Game")
root.resizable(False, False)


top_frame = Frame(
    root,
    bg='red', # Change later to black
    width=720,
    heigh=45,
)
top_frame.place(x=0, y=0)

# Run the window
root.mainloop()

# Cambio minimo de prueba

