#!/usr/bin/env python3
### Date and Time Syncronization program ###

#Set version
version = str("1.0.1")

#Import
print("timesync, Version: " + version)
print("Import functions...")
import tkinter as gui
from tkinter import ttk
from tkinter import messagebox
import subprocess

#general commands
print("Load general commands...")
def exitprogram():
    print("Exit program...")
    GUI.destroy()

def aboutprogram():
    print("show About messagebox...")
    showversion = ("Version: " + version)
    showinfolines = ["Date/Time Syncronizer", "Developed by PalaceSoftware", "", showversion, "", "", "This software is distributed under the MIT License."]
    messagebox.showinfo("About", "\n".join(showinfolines))

#syncronization commands
print("Load syncroization commands...")
def syncdebian():
    print("Sync with debian.org...")
    command = '''pkexec date -s "$(wget --method=HEAD -qSO- --max-redirect=0 debian.org 2>&1 | sed -n 's/^ *Date: *//p')"'''
    successfulchecker = subprocess.run((command), shell=True)
    print(successfulchecker)
    if successfulchecker.returncode == 0:
        messagebox.showinfo("Succesful", "The query was successful")
    else:
        messagebox.showerror("Error", "Wrong password or process aborted")

def synclinux():
    print("Sync with kernel.org...")
    command = '''pkexec date -s "$(wget --method=HEAD -qSO- --max-redirect=0 kernel.org 2>&1 | sed -n 's/^ *Date: *//p')"'''
    successfulchecker = subprocess.run((command), shell=True)
    print(successfulchecker)
    if successfulchecker.returncode == 0:
        messagebox.showinfo("Succesful", "The query was successful")
    else:
        messagebox.showerror("Error", "Wrong password or process aborted")

def syncduck():
    print("Sync with duckduckgo.com...")
    command = '''pkexec date -s "$(wget --method=HEAD -qSO- --max-redirect=0 duckduckgo.com 2>&1 | sed -n 's/^ *Date: *//p')"'''
    successfulchecker = subprocess.run((command), shell=True)
    print(successfulchecker)
    if successfulchecker.returncode == 0:
        messagebox.showinfo("Succesful", "The query was successful")
    else:
        messagebox.showerror("Error", "Wrong password or process aborted")

def syncgoogle():
    print("Sync with google.com...")
    command = '''pkexec date -s "$(wget --method=HEAD -qSO- --max-redirect=0 google.com 2>&1 | sed -n 's/^ *Date: *//p')"'''
    successfulchecker = subprocess.run((command), shell=True)
    print(successfulchecker)
    if successfulchecker.returncode == 0:
        messagebox.showinfo("Succesful", "The query was successful")
    else:
        messagebox.showerror("Error", "Wrong password or process aborted")

def synccustom():
    #syncstart (see button command down)
    print("Initalize custom sync...")
    def syncstart():
        print("Sync with custom...")
        global customadress
        commandcalc = inputfield.get()
        print(commandcalc)
        customadress = ('''pkexec date -s "$(wget --method=HEAD -qSO- --max-redirect=0 ''' + commandcalc + ''' 2>&1 | sed -n 's/^ *Date: *//p')"''')
        command = (customadress)
        successfulchecker = subprocess.run((command), shell=True)
        print(successfulchecker)
        GUI2.destroy()
        if successfulchecker.returncode == 0:
            messagebox.showinfo("Succesful", "The query was successful")
        else:
            messagebox.showerror("Error", "Wrong password or process aborted")
    #Initalisation secound window
    print("Show custom sync window...")
    GUI2 = gui.Tk()
    GUI2.title("Custom sync")
    GUI2.resizable(width=False, height=False)
    #Button and space
    print("Set buttons of custom sync window...")
    gui.Label(GUI2).pack(expand=True, fill="x")
    inputfield = gui.Entry(GUI2) #cannot be used with .pack(expand=True, fill="x")
    inputfield.pack(expand=True, fill="x")
    gui.Label(GUI2).pack(expand=True, fill="x")
    gui.Button(GUI2, text="Sync", command=syncstart).pack()
    gui.Label(GUI2).pack(expand=True, fill="x")

#Initalisation of window
print("Initalize main program...")
GUI = gui.Tk()
GUI.title("Date/Time Syncronizer")
GUI.geometry("300x375")
GUI.resizable(width=False, height=False)

## Setup background and button
#First space
print("Set first space...")
spaceholder1 = gui.Label(GUI)
spaceholder1.pack(expand=True, fill="both")

#Headline (Title)
print("Set headline...")
headline = gui.Label(GUI, text="Date & Time Syncronizer")
headline.pack(expand=True, fill="x")

#Space between headline and buttons
print("Set space between headline and buttons")
spaceholder2 = gui.Label(GUI)
spaceholder2.pack(expand=True, fill="both")

#Buttons
print("Initalize buttons...")
button1 = ttk.Button(GUI, text="Sync with Debian.org", command=syncdebian)
button1.pack()
button2 = ttk.Button(GUI, text="Sync with Linux (Kernel.org)", command=synclinux)
button2.pack()
button3 = ttk.Button(GUI, text="Sync with DuckDuckGo.com", command=syncduck)
button3.pack()
button4 = ttk.Button(GUI, text="Sync with Google.com", command=syncgoogle)
button4.pack()
button5 = ttk.Button(GUI, text="Sync with custom", command=synccustom)
button5.pack()

#Space between buttons and subbuttons
print("Initalize space between buttons and subbottons...")
spaceholder3 = gui.Label(GUI)
spaceholder3.pack(expand=True, fill="both")

#Buttons (Exit, About)
print("Set About button...")
button2 = ttk.Button(GUI, text="About", command=aboutprogram)
button2.pack(side="right")
print("Set Exit button...")
button3 = ttk.Button(GUI, text="Exit", command=exitprogram)
button3.pack(side="left")

#Space between subbuttons and end
print("Set space between subbuttons and end...")
spaceholder4 = gui.Label(GUI)
spaceholder4.pack(expand=True, fill="x")

GUI.mainloop()
