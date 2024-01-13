import customtkinter as ctk
from api import generateKey,keyCheck
from tournamentSchedule import pollEvents,getActiveEvents
from interleaver import interleaver
import pandas as pd 
import csv

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class Dashboard(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        self.geometry("640x480")
        self.title("SKVDashboard")
        self.df = pd.DataFrame()

        #define frames
        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(side="left" ,pady=20, padx=10, fill="both",expand=True)
        self.frame2 = ctk.CTkFrame(master=self)
        self.frame2.pack(side="right",pady=20, padx=10, fill="both",expand=True)
        self.frame3 = ctk.CTkFrame(master=self.frame2)
        self.frame3.pack(side="left",pady=20, padx=10, fill="both",expand=True)

        #scoring system connection - Frame 1
        self.label=ctk.CTkLabel(master=self.frame,text="Connect to Scoring System")
        self.label.pack(pady=12,padx=10)
        self.entry1=ctk.CTkEntry(master=self.frame,placeholder_text="Server IP")
        self.entry1.pack(pady=12,padx=10)
        self.button=ctk.CTkButton(master=self.frame,text="connect",command=self.connect)
        self.button.pack(pady=12,padx=10)

        #Checks Live Events for Interleaver
        self.label2=ctk.CTkLabel(master=self.frame3,text="Get active events - ONLY RUN WHEN SCHEDULES ARE MADE AND USE BEFORE INTERLEAVER")
        self.label2.pack(pady=12,padx=10)
        self.button2=ctk.CTkButton(master=self.frame3,text="Check Active events",command=self.checkEvents)
        self.button2.pack(pady=12,padx=10)
        self.label3=ctk.CTkLabel(master=self.frame3,text="No Active Events")
        self.label3.pack(pady=12,padx=10)
        #Interleaver
        self.button2=ctk.CTkButton(master=self.frame3,text="Run Interleaver",command=self.runInterleaver)
        self.button2.pack(pady=12,padx=10)

        self.toplevel_window = None


    def checkEvents(self):
        ip=self.entry1.get()
        liveEvents= pollEvents(ip)
        activeLeagues=getActiveEvents(liveEvents,ip)
        self.label3.configure(text=activeLeagues)
        
    def runInterleaver(self):
        ip=self.entry1.get()
        liveEvents= pollEvents(ip)
        activeLeagues=getActiveEvents(liveEvents,ip)
        interleavedSchedule=interleaver(activeLeagues,ip)
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


    def connect(self):
        ip=self.entry1.get()
        print(ip)
        isActive=False

        generateKey("SDFTCController",ip)

class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1280x720")
        self.title("SKVDashboard Match Schedule") 
        with open("dftocsv.csv", newline="") as file:
            reader = csv.reader(file)

            # r and c tell us where to grid the labels
            for r, col in enumerate(reader):
                for c, row in enumerate(col):
                    # i've added some styling
                    label = ctk.CTkLabel(
                        self, width=100, height=20, text=row
                    )
                    label.grid(row=r, column=c)  

        

app=Dashboard()
app.mainloop()