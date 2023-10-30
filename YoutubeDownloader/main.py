import pytube

url = input("enter video url:")

path = ""
pytube.YouTube(url).streams.get_highest_resolution().download(path) # if path is blank it is going to download into the project path in this way