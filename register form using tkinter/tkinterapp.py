# start of code
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

root = tk.Tk()
root.title('Dispire')

# create label
name_label = ttk.Label(root, text='Enter Your Name: ')
name_label.grid(row=0, column=0, sticky=tk.W)

email_label = ttk.Label(root, text='Enter Youe Email: ')
email_label.grid(row=1, column=0, sticky=tk.W)

age_label = ttk.Label(root, text='Enter Your Age: ')
age_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(root, text='Select Your Gender: ')
gender_label.grid(row=3, column=0, sticky=tk.W)

usertype_label = ttk.Label(root, text='Select User Type: ')
usertype_label.grid(row=4, column=0, sticky=tk.W)

# create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(root, width=16, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(root, width=16, textvariable=email_var)
email_entrybox.grid(row=1, column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(root, width=16, textvariable=age_var)
age_entrybox.grid(row=2, column=1)

# create combo box
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root, width=13, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)

# create radio box
user_type = tk.StringVar()
usertype_radio1 = ttk.Radiobutton(root, text='Student', value='Student', variable=user_type)
usertype_radio1.grid(row=4, column=1)
usertype_radio2 = ttk.Radiobutton(root, text='Teacher', value='Teacher', variable=user_type)
usertype_radio2.grid(row=5, column=1)

# create check button
checkbtn_var = tk.IntVar()
newsletter_check = ttk.Checkbutton(root, text='Check if you want to subscribe our news letter', variable=checkbtn_var)
newsletter_check.grid(row=6, columnspan=3)

# create button


def action():
    username = name_var.get()
    useremail = email_var.get()
    userage = age_var.get()
    usergender = gender_var.get()
    usertype = user_type.get()

    if checkbtn_var.get() == 0:
        subscribed = 'NO'
    else:
        subscribed = 'YES'

    with open('file.csv', 'a', newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['UserName', 'User Email Address', 'User Age', 'User Type', 'Gender', 'subscribed'])
        if os.stat('file.csv').st_size == 0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'UserName': username,
            'User Email Address': useremail,
            'User Age': userage,
            'Gender': usergender,
            'User Type': usertype,
            'subscribed': subscribed
        })

    name_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)


submit_button = ttk.Button(root, text='Submit', command=action)
submit_button.grid(row=7, columnspan=2)

root.mainloop()
