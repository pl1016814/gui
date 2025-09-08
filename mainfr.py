import tkinter as tk
from PIL import Image, ImageTk
#for this code to run, you must run "pip install pillow"

root = tk.Tk()
root.title("GUI")
root.geometry("1920x1080")

icons = {}
def load_png(path, subsample=4):
    img = tk.PhotoImage(file=path).subsample(subsample, subsample)
    icons[path] = img
    return img

upIcon = load_png("up-arrow.png", subsample=4)
leftIcon = load_png("left-arrow.png", subsample=4)
playIcon = load_png("play-arrow.png", subsample=6)
stopIcon = load_png("stop-arrow.png", subsample=3)
rightIcon = load_png("right-arrow.png", subsample=4)
downIcon = load_png("down-arrow.png", subsample=4)
topLeftImageVariable = tk.PhotoImage(file="road.png").subsample(2, 2)
bottomLeftImageVariable = tk.PhotoImage(file="road.png").subsample(2, 2)

#topleft
topLeftFrame = tk.Frame(root, bd=2, relief="groove")
topLeftFrame.grid(row=0, column=0)
topLeftLabel = tk.Label(topLeftFrame, text="VIDEO STREAM")
topLeftLabel.pack(side="top", fill="both")
topLeftImage = tk.Label(topLeftFrame, image=topLeftImageVariable).pack(side="bottom")

#bottomLeft
bottomLeftFrame = tk.Frame(root, bd=2, relief="groove")
bottomLeftFrame.grid(row=0, column=1)
bottomLeftLabel = tk.Label(bottomLeftFrame, text="VIDEO STREAM")
bottomLeftLabel.pack(side="top", fill="both")
bottomLeftImage = tk.Label(bottomLeftFrame, image=bottomLeftImageVariable).pack(side="bottom")

#topRight
playing = False
def togglePlay():
    global playing
    playing = not playing
    if playing:
        playButton.config(image=stopIcon)
    else:
        playButton.config(image=playIcon)
topRightFrame = tk.Frame(root)
topRightFrame.grid(row=1, column=0)
for i in range(3):
    topRightFrame.rowconfigure(i, weight=1)
    topRightFrame.columnconfigure(i, weight=1)
upButton = tk.Button(topRightFrame, image=upIcon, bd=0)
upButton.grid(row=0, column=1, sticky="nsew")
leftButton = tk.Button(topRightFrame, image=leftIcon, bd=0)
leftButton.grid(row=1, column=0, sticky="nsew")
playButton = tk.Button(topRightFrame, image=playIcon, command=togglePlay, bd=0)
playButton.grid(row=1, column=1, sticky="nsew")
rightButton = tk.Button(topRightFrame, image=rightIcon, bd=0)
rightButton.grid(row=1, column=2, sticky="nsew")
downButton = tk.Button(topRightFrame, image=downIcon, bd=0)
downButton.grid(row=2, column=1, sticky="nsew")

#bottomRight
bottomRightFrame = tk.Frame(root)
bottomRightFrame.grid(row=1, column=1)
logTitleLabel = tk.Label(root, text="USER LOG")
logText = tk.Text(bottomRightFrame, wrap="word", height=20, width=60)
logText.pack(expand=True, fill="both")
logText.insert("end", "USER LOG")

root.grid_columnconfigure(0, minsize=960)
root.grid_columnconfigure(1, minsize=960)
root.grid_columnconfigure(0, minsize=540)
root.grid_columnconfigure(1, minsize=540)
topLeftFrame.grid(row=0, column=0, sticky="nsew")
topRightFrame.grid(row=0, column=1, sticky="nsew")
bottomLeftFrame.grid(row=1, column=0, sticky="nsew")
bottomRightFrame.grid(row=1, column=1, sticky="nsew")

root.mainloop()
