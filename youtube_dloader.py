from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube 
from tkinter import messagebox

Folder_Name = ""

#File Location Function 
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose File Save Location",fg="red")

#Download Video Function
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again",fg="red")


    #download function
    messagebox.askyesno("Warning", "Are you sure you want to save the file to {} ?".format(Folder_Name))
    select.download(Folder_Name)
    ytdError.config(text="Download Completed")
    


root = Tk()
root.title("Youtube Downloader")
root.geometry("400x400") 
root.columnconfigure(0,weight=1)


mainLabel = Label(root,text="Youtube Downloader",font=("helvetica",20, "bold"))
mainLabel.grid(pady = 30)


#Yotube Link Label
ytdLabel = Label(root,text="Enter the URL of the Video",font=("helvetica",15))
ytdLabel.grid(pady = 5)

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid(padx = 20)

#Error Msg
ytdError = Label(root,text="",fg="green",font=("helvetica",10))
ytdError.grid()

#Label Save File
saveLabel = Label(root,text="Save the Video File",font=("helvetica",15))
saveLabel.grid()

#Button Save File
saveEntry = Button(root,width=10,bg="white",fg="black",text="Choose Path",command=openLocation)
saveEntry.grid()

#Error Msg Location
locationError = Label(root,text="",fg="green",font=("helvetica",10))
locationError.grid(pady = 10)

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("helvetica",15))
ytdQuality.grid()

#ComboBox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#Button Download
downloadbtn = Button(root,text="Download",width=10,bg="white",fg="black",command=DownloadVideo)
downloadbtn.grid()

root.mainloop()