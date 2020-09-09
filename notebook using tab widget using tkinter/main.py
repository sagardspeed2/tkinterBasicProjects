import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('TAB control notebook')

nb = ttk.Notebook(win)

page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)

nb.add(page1, text = "ONE")
nb.add(page2, text = "TWO")

nb.pack(expand = True, fill = 'both')

label_1 = ttk.Label(page1, text = 'This is a Demo Label For Page 1 : ')
label_1.grid(row = 0, column = 0)

entry_1 = ttk.Entry(page1, width = 26)
entry_1.grid(row = 0, column = 1)

label_1 = ttk.Label(page2, text = 'This is a Demo Label For Page 2 : ')
label_1.grid(row = 0, column = 0)

entry_1 = ttk.Entry(page2, width = 26)
entry_1.grid(row = 0, column = 1)

win.mainloop()