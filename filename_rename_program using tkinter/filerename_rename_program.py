from tkinter import *
from tkinter import filedialog
import os

a = Tk()


def fileopen():
    file1 = filedialog.askdirectory()
    filepath = file1

    os.chdir(filepath)

    f_num = 21

    for f in os.listdir():
        file_name, file_ext = os.path.splitext(f)
        os.rename(f, f'{f_num}__{file_name}{file_ext}')
        f_num += 1


button = Button(text="open file", width="30", command=fileopen).pack()

a.mainloop()
