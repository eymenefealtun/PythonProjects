from tkinter import *

window = Tk()
window.title("Tkinter Python")
window.minsize(600, 600)
window.config(padx=20, pady=20)  # gives a padding to all screen

label = Label(text="my label")
# label.config(bg="black")
label.config(fg="red")
label.config(padx=10, pady=10)

# label.place(x=200,y=300)
label.pack()


def clickButton():
    print("button clicked")
    print(f"entry content {entry.get()}")
    print(f"text content {text.get(1.0, END)}")  # reads from first line 0th character


button = Button(text="button", command=clickButton)
button.config(padx=10, pady=10)
button.pack()

entry = Entry(width=20)
entry.pack()

text = Text(width=30, height=5)
text.focus()
text.pack()


def scaleSelection(value):
    print(f"chosen scale: {value}")


# scale
my_scale = Scale(from_=0, to=50, orient=HORIZONTAL, command=scaleSelection)
my_scale.pack()


def spinBoxSelection():
    print(f"spin box value: {my_spinbox.get()}")


# spin box
my_spinbox = Spinbox(from_=0, to=50, command=spinBoxSelection)
my_spinbox.pack()


def checkButtonSelected():
    print(f"check button: {check_state.get()}")
# check button
check_state = IntVar()
my_checkButton = Checkbutton(text="check", variable= check_state, command = checkButtonSelected)
my_checkButton.pack()


def radioSelected():
    print(radio_state.get())

# radio button
radio_state = IntVar()
my_radiobutton = Radiobutton(text="1. option", value=10,variable=radio_state,command=radioSelected)
my_radiobutton2 = Radiobutton(text="2. option", value=20,variable=radio_state,command=radioSelected)

my_radiobutton.pack()
my_radiobutton2.pack()



def listBoxSelected(event):
    print(my_listbox.get(my_listbox.curselection()))

# list box
my_listbox = Listbox()
name_list = ["asd","asdasd","asdasd","pjğdg"]
for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])
my_listbox.bind('<<ListboxSelect>>',listBoxSelected)
my_listbox.pack()

window.mainloop()
