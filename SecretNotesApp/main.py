import tkinter
from PIL import ImageTk, Image
import hashlib
import base64
import uuid

mainScreen = tkinter.Tk()
mainScreen.config(padx=10)
mainScreen.title("Secret Notes App")
mainScreen.geometry('%dx%d+%d+%d' % (
    300, 600, (mainScreen.winfo_screenwidth() / 2) - (300 / 2), (mainScreen.winfo_screenheight() / 2) - (600 / 2)))

mainFont = ("Arial", 14)
mainFg = "black"

# handling image
frame = tkinter.Frame(mainScreen, pady=40)
frame.pack()
img = ImageTk.PhotoImage(Image.open("mainImage.png"))
imageLabel = tkinter.Label(frame, image=img)

labelTitle = tkinter.Label(text="Enter your title", font=mainFont, pady=10, fg=mainFg)
enrtyTitle = tkinter.Entry(width=60)

labelSecret = tkinter.Label(text="Enter your secret", font=mainFont, pady=10, fg=mainFg)
textSecret = tkinter.Text(width=60, height=10)

labelMasterKey = tkinter.Label(text="Enter your master key", font=mainFont, pady=10, fg=mainFg)
enryMaster = tkinter.Entry(width=60)

imageLabel.pack()
labelTitle.pack()
enrtyTitle.pack()
labelSecret.pack()
textSecret.pack()
labelMasterKey.pack()
enryMaster.pack()


def InsertItemIntoFile(title, secretHash):
    mainTextFile = open("mySecret.txt", "a+")
    mainTextFile.write(f"{title}\n")
    mainTextFile.write(f"{secretHash}\r\n")
    mainTextFile.close()


def decodeGivenHash(secretHash, masterKey):
    #salted = base64.b64decode(base64.b64encode(masterKey.encode()) + secretHash.encode())
    salted = base64.urlsafe_b64decode(base64.b64encode(masterKey.encode()) + secretHash.encode())
    print(salted)


def encodeGivenString(secretString, masterString):
    resultHash = ''
    # tempString = r'eymen efe altun'
    # resultHash = base64.b64encode(tempString.encode())

    salt = base64.b64encode(masterString.encode())
    salted = base64.b64encode(salt + base64.b64encode(secretString.encode()))
    resultHash = str(salted)


    print(salt)
    print(resultHash)
    return resultHash


#encodeGivenString('asd', 'asd')

btnSaveAndEncrypt = tkinter.Button(text="Save & Encrypt",
                                   command=lambda: InsertItemIntoFile
                                       (
                                       title=enrtyTitle.get(),
                                       secretHash=encodeGivenString(textSecret.get(
                                           "1.0", tkinter.END), enryMaster.get())
                                   )
                                   )

btnDecrypt = tkinter.Button(text="Decrypt", pady=10, height=1,
                            command=lambda: decodeGivenHash(secretHash=textSecret.get("1.0", tkinter.END),
                                                              masterKey=enryMaster.get()))

btnSaveAndEncrypt.pack()
btnDecrypt.pack()

mainScreen.mainloop()
