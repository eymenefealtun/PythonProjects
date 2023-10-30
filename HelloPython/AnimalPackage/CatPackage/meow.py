def speakDirect():
    print("meow direct")

def speakImported():
    print("meow imported")


if __name__ == "__main__":  ## if this class ir running from __main__ run this code
    speakDirect()
else:
    speakImported()   # this line is fired in main.py after importing this meow.py