import os
import sys
import tkinter.messagebox
from pathlib import Path
from threading import Thread
from tkinter import Tk, Frame, Entry, Button, LabelFrame, Label, X, BOTH, YES, filedialog, Menu

import requests as req

from utils.audio import Audio
from utils.conf import Configuration
from utils.languages import Language
from utils.video import Video

LANG = Language()
CONF = Configuration()

with open("utils/language.conf", "r") as language:
    for line in language:
        if "EN" in line:
            LANG.EN()
            CONF.EN()
            break
        elif "FR" in line:
            LANG.FR()
            CONF.FR()
            break
        else:
            os.system("echo EN > utils/language.conf")
            LANG.EN()
            CONF.EN()

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def languageEnglish():
    os.system("echo EN > utils/language.conf")
    restart_program()

def languageFrench():
    os.system("echo FR > utils/language.conf")
    restart_program()

# reset the displayed history when the limit is reached
def destroyHistory():
    audiosList_frame.destroy()
    videosList_frame.destroy()
def resetHistory():
    destroyHistory()
    global audiosList_frame
    global videosList_frame

    audiosList_frame = LabelFrame(window, bg="#bfc5c9", text=LANG.audio, bd=5, height=155)
    audiosList_frame.pack(fill=X, padx=5, pady=5)

    videosList_frame = LabelFrame(window, bg="#bfc5c9", text=LANG.video, bd=5, height=155)
    videosList_frame.pack(fill=X, padx=5, pady=5)

def clearEntry():
    link_entry.delete(0, "end")


def pasteEntry():
    try:
        text = window.clipboard_get()
    except:
        tkinter.messagebox.showerror(LANG.error, LANG.clipboardEmpty)
        return
    clearEntry()
    link_entry.insert(0, text)


def getLenAudioLogs():
    with open("utils/audio_logs", "r") as file:
        count = 0
        for line in file:
            count += 1
    return count

def getLenVideoLogs():
    with open("utils/video_logs", "r") as file:
        count = 0
        for line in file:
            count += 1
    return count

# update the history
def update():  # update the logs
    with open("utils/audio_logs", "r") as file:
        count = 0
        for line in file:
            Label(audiosList_frame, text=line, bg="#bfc5c9").place(x=0, y=count * 20)
            Label(audiosList_frame, text=LANG.downloaded, bg="#bfc5c9").place(x=CONF.Xdownloaded, y=count * 20)
            count += 1

    with open("utils/video_logs", "r") as file:
        count = 0
        for line in file:
            Label(videosList_frame, text=line, bg="#bfc5c9").place(x=0, y=count * 20)
            Label(videosList_frame, text=LANG.downloaded, bg="#bfc5c9").place(x=CONF.Xdownloaded, y=count * 20)
            count += 1

def saveAudio(filename):  # save the name of the downloaded files (audio_logs)
    with open("utils/audio_logs", "r") as file:
        count = 0
        for line in file:
            count += 1

        if count == 5:
            resetHistory()
            os.system(f"echo {filename} > utils/audio_logs")
        else:
            os.system(f"echo {filename} >> utils/audio_logs")
    update()


def saveVideo(filename):  # save the name of the downloaded files (video_logs)
    with open("utils/video_logs", "r") as file:
        count = 0
        for line in file:
            count += 1

        if count == 5:
            resetHistory()
            os.system(f"echo {filename} > utils/video_logs")
        else:
            os.system(f"echo {filename} >> utils/video_logs")

    update()


def mp3threading():
    t1 = Thread(target=mp3)
    t1.start()


def mp4threading():
    t1 = Thread(target=mp4)
    t1.start()


# add https to the link
def correctTheLink(link):
    if link[0] != "h":
        link = "https://" + link

    return link


# check if the link is valid and if it's from youtube
def isValidYoutubeLink(link):
    if link == "":
        tkinter.messagebox.showerror(LANG.error, LANG.entryEmpty)
        return True

    link = correctTheLink(link)

    try:
        r = req.get(link)
        # check if the youtube video is available
        if "Video unavailable" in r.text:
            tkinter.messagebox.showerror(LANG.error, LANG.videoUnavailable)
            return True
    except:
        # if the link is
        tkinter.messagebox.showerror(LANG.error, LANG.noValidLink)
        return True

    if "youtube" not in link:
        tkinter.messagebox.showerror(LANG.error, LANG.notYoutube)
        return True
    return False



# download the mp3 file
def mp3():
    link = link_entry.get()

    if isValidYoutubeLink(link):
        return

    AudioDownloader = Audio(link)
    filename = AudioDownloader.getFilename()

    try:

        a = Label(audiosList_frame, text=filename, bg="#bfc5c9")
        a.place(x=0, y=getLenAudioLogs()*20)
        b = Label(audiosList_frame, text=LANG.downloading, bg="#bfc5c9")
        b.place(x=CONF.Xdownloading, y=getLenAudioLogs()*20)

        AudioDownloader.download(directory_label.cget("text"))

        a.destroy()
        b.destroy()
    except:
        tkinter.messagebox.showerror(LANG.error, LANG.noValidLink)
        return


    saveAudio(filename)
    tkinter.messagebox.showinfo(LANG.download, f"{filename[:-4]} {LANG.downloadedSuccefully}")


# download the mp4 file
def mp4():
    link = link_entry.get()

    if isValidYoutubeLink(link):
        return

    VideoDownloader = Video(link)
    filename = VideoDownloader.getFilename()

    try:
        a = Label(videosList_frame, text=filename, bg="#bfc5c9")
        a.place(x=0, y=getLenVideoLogs() * 20)
        b = Label(videosList_frame, text=LANG.downloading, bg="#bfc5c9")
        b.place(x=CONF.Xdownloading, y=getLenVideoLogs() * 20)

        VideoDownloader.download(directory_label.cget("text"))

        a.destroy()
        b.destroy()
    except:
        tkinter.messagebox.showerror(LANG.error, LANG.noValidLink)
        return

    saveVideo(filename)
    tkinter.messagebox.showinfo(LANG.download, f"{filename[:-4]} {LANG.downloadedSuccefully}")


window = Tk()

# Set the parameters for the window
window.title("Youtube Downloader")
window.geometry("500x600")
window.resizable(0, 0)
window.iconbitmap("./utils/logo.ico")
window.config(background="#a6a7a8")

# link entry
link_frame = Frame(window, bg="#a6a7a8")

link_entry = Entry(link_frame, width=38, font=("Liberation Serif", 13), bg="#bfc5c9", relief="groove")
link_entry.place(x=75, y=1)

# buttons
# mp3
buttonMp3 = Button(link_frame, text=f"{LANG.download} mp3", command=mp3threading, padx=CONF.padxButtonMP3)
buttonMp3.place(x=CONF.XbuttonMP3, y=CONF.YbuttonMP3)

# mp4
buttonMp4 = Button(link_frame, text=f"{LANG.download} mp4", command=mp4threading, padx=CONF.padxButtonMP4)
buttonMp4.place(x=CONF.XbuttonMP4, y=CONF.YbuttonMP4)

# clear
buttonClear = Button(link_frame, text=f"{LANG.clear}", command=clearEntry, padx=CONF.padxButtonClear)
buttonClear.place(x=CONF.XbuttonClear, y=CONF.YbuttonClear)

# paste
buttonPaste = Button(link_frame, text=LANG.paste, command=pasteEntry, padx=CONF.padxButtonPaste)
buttonPaste.place(x=CONF.XbuttonPaste, y=CONF.YbuttonPaste)

#browse directories (to choose where to download the file)
def browseFolder():
    folder = filedialog.askdirectory()
    directory_label.config(text=folder)

def clickedDirectoryLabel(event=None):
    folder = directory_label.cget("text")
    folder = folder.replace("/", "\\")

    os.system(f"explorer {folder}")


defaultDownloadFolder = str(os.path.join(Path.home(), "Downloads"))

directory_label = Label(link_frame, width=38, font=("Liberation Serif", 13), bg="#bfc5c9", text=defaultDownloadFolder, fg="blue", relief="groove")
directory_label.place(x=75, y=100)
directory_label.bind("<Button-1>", clickedDirectoryLabel)
directory_label.bind("<Enter>", directory_label.config(cursor="hand2"))

buttonDirectory = Button(link_frame, text=LANG.browse, command=browseFolder, padx=CONF.padxButtonBrowse)
buttonDirectory.place(x=CONF.XbuttonBrowse, y=CONF.YbuttonBrowse)


link_frame.pack(pady=50, fill=BOTH, expand=YES)

# AUDIO
audiosList_frame = LabelFrame(window, bg="#bfc5c9", text=LANG.audio, bd=5, height=155)

audiosList_frame.pack(fill=X, padx=5, pady=5)


# VIDEO
videosList_frame = LabelFrame(window, bg="#bfc5c9", text=LANG.video, bd=5, height=155)

videosList_frame.pack(fill=X, padx=5, pady=5)

# UPDATE THE LOGS WHEN THE SOFTWARE START
update()


#menu
my_menu = Menu(window, bg="#a6a7a8")
window.config(menu=my_menu)

language_menu = Menu(my_menu)
my_menu.add_cascade(label=LANG.menuLanguage, menu=language_menu)
language_menu.add_command(label="English", command=languageEnglish)
language_menu.add_command(label="Français", command=languageFrench)



# show the window
window.mainloop()
