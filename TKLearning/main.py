import tkinter

# window
window = tkinter.Tk()
window.title('Python Tkinter')
window.minsize(800, 600)

# label
my_label = tkinter.Label(text="this is a label", font=('Arial', 20, 'bold'))
my_label.config(bg="black", fg="white")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(row=0, column=0)


# button
def getText():
    user_input = my_entry.get()
    print(user_input)


def click_button():
    print("button clicked")
    getText()


my_button = tkinter.Button(text="this is a button", command=click_button)
# my_button.pack()
my_button.grid(row=1, column=1)
# entry
my_entry = tkinter.Entry(width=30)
# my_entry.pack(side = "top")
# my_entry.pack()
my_entry.grid(row=0, column=2)



window.mainloop()
