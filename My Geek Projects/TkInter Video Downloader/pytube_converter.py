import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

# define CreateWidgets() to create Tk widgets
def Widgets():

    head_label = Label(root, text="YouTube Video Downloader",
                       padx=10,
                       pady=10,
                       font="SegoeUI 14",
                       bg="palegreen1",
                       fg="red")
    head_label.grid(row=1,
                    column=1,
                    pady=10,
                    padx=5,
                    columnspan=3)
    link_label = Label(root,
                       text="YouTube Link",
                       bg="salmon",
                       pady=5,
                       padx=5)
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)
    root.linkText = Entry(root,
                          width=35,
                          textvariable=video_Link,
                          font="Arial 14")
    root.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    destination_label = Label(root,
                              text="Destination",
                              bg="salmon",
                              pady=5,
                              padx=9)
    destination_label.grid(row=3,
                           column=0,
                           pady=5,
                           padx=5)

    root.destinationText = Entry(root,
                                 width=27,
                                 textvariable=download_Path,
                                 font="Arial 14")
    root.destinationText.grid(row=3,
                              column=1,
                              pady=5,
                              padx=5)

    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="bisque",
                      relief=GROOVE)
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)

    download_B = Button(root,
                        text="Download Video",
                        command=Download,
                        width=20,
                        bg="thistle1",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Georgia, 13")
    download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)


# define Browse() to select a destination to save the video

def Browse():
    # present the user with a pop-up for a directory selection
    # initialdir is optional. 
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Destination folder")

    # display the dir in the directory textbox
    download_Path.set(download_Directory)


# define Download() to download the video

def Download():

    # grab user-input link
    Youtube_link = video_Link.get()

    # select optimal location for saving files
    download_Folder = download_Path.get()

    # create object of youtube
    getVideo = YouTube(Youtube_link)

    # get all available streams of the video 
    videoStream = getVideo.streams.first()

    # downloading the video to destination dir
    videoStream.download(download_Folder)

    # display message
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN \n"
                        + download_Folder)



# object of Tk class
root = tk.Tk()


# title, bg color
# and size of window
# ! disabling resizing property
root.geometry("520x280")
root.resizable(False, False)
root.title("Lex Video Downloader")
root.config(background="PaleGreen1")


# tkinter variables
video_Link = StringVar()
download_Path = StringVar()

# calling Widgets() func
Widgets()


root.mainloop()

