import requests
import tkinter
import json
from tkinter.messagebox import showerror

class AppGUI(tkinter.Tk):
    def __init__(self):
        super().__init__()

        # API Key (You can use this but I might delete this in future so You can make your own)
        self.API = "AIzaSyA1_niLyH_wZhVsEV-_ja5BwCQFXKHiItg"
        self.showingFrame = None
        
        # Desigining GUI
        self.title("Youtube Statistics Shower")
        self.geometry("800x500")
        self.config(bg="grey")
        tkinter.Label(self,text="Youtube Statistics Counter",fg="green",font=("Times",20)).pack(fill='x')
       
        container = tkinter.LabelFrame(self,bg="grey",text="Channel Info")
        container.pack(fill='x',pady=15)
        tkinter.Label(container,bg="grey",font=("Elephant",16),text="Please Enter your Channel name (KEY)under the following box").pack(fill="x")

        self.entry = tkinter.StringVar()
        tkinter.Entry(container,font=("Elephant",16),textvariable=self.entry).pack(fill='x')
        self.entry.set("UCT3_L8_0DXOL_Gox76I0BOw") # It will defaulty load my channel

        tkinter.Button(container,text="Click to Get Details",command=self.get_details,font=("Elephant",12)).pack()

    def get_details(self):
        if self.showingFrame:
            self.showingFrame.destroy()
            self.showingFrame = None
            
        if self.entry.get().lstrip().rstrip() != "":
            # Checking whether the link is empty or not

            try:
                req = requests.get(f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.entry.get()}&key={self.API}")
            except:
                showerror("No Internet","Make sure you have working internet connection")
                return
                
            # Fetching with the JSON
            jsonified = json.loads(req.text)

            # Getting Data
            try:
                self.views = jsonified["items"][0]["statistics"]["viewCount"]
                self.subscribers = jsonified["items"][0]["statistics"]["subscriberCount"]
                self.videos = jsonified["items"][0]["statistics"]["videoCount"]
            except:
                showerror("Error","Wrong Link, make sure you have typed correct link (or maybe an API problem)")
                return

            # Showing all details in  the GUI
            self.show_details()

    def show_details(self):
        self.showingFrame = tkinter.Frame(self)
        
        tkinter.Label(self.showingFrame,bg = "Red",font=("Elephant",12),text=f"Views to the Channel is ->  {self.views}").pack(fill='x')
        tkinter.Label(self.showingFrame,bg = "Red",font=("Elephant",12),text=f"The number of subscribers  is ->  {self.subscribers}").pack(fill='x')
        tkinter.Label(self.showingFrame,bg = "Red",font=("Elephant",12),text=f"The number of videos uploaded on  this channel is ->  {self.videos}").pack(fill='x')

        self.showingFrame.pack(fill='x')
        
if __name__=="__main__":
    AppGUI().mainloop()
