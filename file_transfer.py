
import os
import shutil
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import tkinter.filedialog



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.geometry("500x300")
        self.master.title('Move updated files')
        self.master.config(bg='grey93')

        
        self.txtSource = Entry(self.master, width=30,  text=folderPathStart, font=('Helvetica', 16), fg='black', bg='lightblue')  
        self.txtSource.grid(row=1, column=1, padx=(5, 5), pady=(5, 5))
        
        self.btnSource = Button(self.master, text='Get', width=10, height=2, command=source_Folder)  
        self.btnSource.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky='W')

        self.txtDestination = Entry(self.master, width=30, text=folderPathEnd, font=('Helvetica', 16), fg='black', bg='lightblue') 
        self.txtDestination.grid(row=2, column=1, padx=(5, 5), pady=(5, 5))
        
        self.btnDestination = Button(self.master, text='Send', width=10, height=2, command=destination_Folder) 
        self.btnDestination.grid(row=2, column=0, padx=(5, 5), pady=(5, 5), sticky='SW')

        self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command=move_File)  
        self.btnSubmit.grid(row=3, column=1, padx=(5,5), pady=(10,0))

def source_Folder():
    name = tkinter.filedialog.askdirectory()
    folderPathStart.set(name)

def destination_Folder():
    name = tkinter.filedialog.askdirectory()
    folderPathEnd.set(name)

def move_File():
    source = folderPathStart.get()
    destination = folderPathEnd.get()
    current_time = datetime.now()
    source_files = os.listdir(source)
    for i in source_files:
        filePath = os.path.join(source, i)
        past_24hours = current_time - timedelta(hours = 24)
        modify_date_seconds = os.path.getmtime(filePath)
        recently_updated = datetime.fromtimestamp(modify_date_seconds)
        if past_24hours < recently_updated:
            shutil.move(source + '/' + i, destination)
            print (i + 'File transfer was successful.')
        else:
            print('No recent updates to files.')
    
    
    



if __name__ == "__main__":
    root = Tk()
    folderPathStart = StringVar() 
    folderPathEnd = StringVar() 
    App = ParentWindow(root)
    root.mainloop()
