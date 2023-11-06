from tkinter import *

mainWindow = Tk()
mainWindow.title("Bmi Calculator")
mainWindow.minsize(300, 300)
mainWindow.config(padx=10, pady=10)

lblWeight = Label(text="Enter Your Weight (kg)")
lblHeight = Label(text="Enter Your Height (cm)")
entryWeight = Entry(width=20)
entryHeight = Entry(width=20)
lblResult = Label(text="")

def analyseBmi(givenBmi):
    if givenBmi <= 18.5:
        return "Underweight"
    elif givenBmi <= 24.9:
        return "Normal range"
    elif givenBmi <= 29.9:
        return "Overweight"
    elif (givenBmi >= 30 and givenBmi <= 34.9):
        return "Obese class 1"
    elif givenBmi <= 39.9:
        return "Obese class 2"
    else:
        return "Obese class 3"


def handleResultLable(result):
    lblResult.config(text=f"{result}")

def calculateBmi():
    if (entryHeight.get() == 0 or entryWeight.get() == 0):
        print()
    try:
        bmi = format(int(entryWeight.get()) / ((int(entryHeight.get()) / 100) ** 2), ".2f")
        bmiInt = int(entryWeight.get()) / ((int(entryHeight.get()) / 100) ** 2)
        handleResultLable(f"Your BMI is {bmi}. \nIt means you are {analyseBmi(givenBmi=bmiInt)}")
    except:
        handleResultLable(f"Something went wrong. Please check your input.")


btnCalculate = Button(width=10, text="calculate", command=calculateBmi)

lblWeight.pack()
entryWeight.pack()
lblHeight.pack()
entryHeight.pack()
btnCalculate.pack(pady=20)
lblResult.pack()

mainWindow.mainloop()
