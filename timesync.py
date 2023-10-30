#!/usr/bin/env python3
### Date and Time Syncronization program ###

#Import
print("Import functions...")
import os
import tkinter as gui
from tkinter import ttk
from tkinter import messagebox
import subprocess
import platformdirs
import languagesetup # import local file "languagesetup.py"
print("Import finished.")

#Get run_path and config-folder (create config-folder if not exist)
run_path = os.path.abspath(os.path.dirname(__file__)) # get directory of current file (without os.path.dirname it would be just the current file)

config_path = platformdirs.user_config_dir("timesync")
configexist = os.path.isdir(config_path)
if not configexist == True:
    os.makedirs(config_path)

#Set version (show it in debugging mode)
print("Application is running in", run_path)
print("Configuration will be saved in", config_path)
version = open(run_path + "/version.txt", "r")
version = version.readline()
print("timesync version", version)

#language
print("Testing for language...")
configexist = os.path.isfile(config_path + "/language.cfg")
if not configexist == True:
    with open(config_path + "/language.cfg", "w") as langcfg:
        print("None", file=langcfg) # create language.cfg if not exist and write a 0 in it
        print("", file=langcfg)
language = open(config_path + "/language.cfg", "r")
language = language.readline()
language = language.replace("\n", "") # remove empty line(s) from the variable, because "if language == 0 [...]" does not work otherwise
if language == "None":
    languagesetup.main()
elif language == "EN":
    language = str("1")
elif language == "DE":
    language = str("2")
else:
    print("Language Error! Language could not be detectet!")
    exit()
print("Language:", language, "\n 1 = English \n 2 = German \n")

#general commands
print("Load general commands...")
def exitprogram():
    # print("Exit program...") # don't have to be here anymore, because after GUI.mainloop() is already the print command
    GUI.destroy()

def aboutprogram():
    print("show About messagebox...")
    showversion = ("Version: " + version)
    if language == "1" or language == "None":
        showinfolines = ["Date/Time Syncronizer", "Developed by Palace4Software", "", showversion, "", "", "This software is distributed under the MIT License."]
        messagebox.showinfo("About", "\n".join(showinfolines))
    if language == "2":
        showinfolines = ["Datum & Uhrzeit Syncronisierer", "Entwickelt von Palace4Software", "", showversion, "", "", "Diese Software unterliegt der MIT-Lizenz."]
        messagebox.showinfo("Über das Programm", "\n".join(showinfolines))

def syncfin(successfulchecker): #Messagebox after syncronization (with multilanguagesupport)
    if successfulchecker.returncode == 0:
        if language == "1" or language == "None":
            messagebox.showinfo("Successful", "The query was successful")
        if language == "2":
            messagebox.showinfo("Erfolgreich", "Die Abfrage war erfolgreich")
        print("The query was succesful")
    else:
        if language == "1" or language == "None":
            messagebox.showerror("Error", "Wrong password or process aborted")
        if language == "2":
            messagebox.showerror("Fehler", "Falsches Kennwort oder Prozess abgebrochen")
        print("Error - Wrong password or process aborted")

def changelang():
    languagesetup.main()
print("General commands loaded.")

#syncronization commands
print("Load syncronization commands...")
def syncdebian():
    print("Sync with debian.org...")
    command = '''pkexec date -s "$(wget --method=HEAD -qSO- --max-redirect=0 debian.org 2>&1 | sed -n 's/^ *Date: *//p')"'''
    successfulchecker = subprocess.run((command), shell=True)
    print(successfulchecker)
    syncfin(successfulchecker)

def synclinux():
    print("Sync with kernel.org...")
    command = '''pkexec date -s "$(wget --method=HEAD -qSO- --max-redirect=0 kernel.org 2>&1 | sed -n 's/^ *Date: *//p')"'''
    successfulchecker = subprocess.run((command), shell=True)
    print(successfulchecker)
    syncfin(successfulchecker)

def syncduck():
    print("Sync with duckduckgo.com...")
    command = '''pkexec date -s "$(wget --method=HEAD -qSO- --max-redirect=0 duckduckgo.com 2>&1 | sed -n 's/^ *Date: *//p')"'''
    successfulchecker = subprocess.run((command), shell=True)
    print(successfulchecker)
    syncfin(successfulchecker)

def syncgoogle():
    print("Sync with google.com...")
    command = '''pkexec date -s "$(wget --method=HEAD -qSO- --max-redirect=0 google.com 2>&1 | sed -n 's/^ *Date: *//p')"'''
    successfulchecker = subprocess.run((command), shell=True)
    print(successfulchecker)
    syncfin(successfulchecker)

def synccustom():
    #syncstart (see button command down)
    print("Initalize custom sync...")
    def syncstart():
        print("Sync with custom...")
        global customadress
        commandcalc = inputfield.get()
        print(commandcalc)
        with open(config_path + "/lastcustom.cfg", "w") as lastcustom:
            print(commandcalc, file=lastcustom)
            print("", file=lastcustom)
        customadress = ('''pkexec date -s "$(wget --method=HEAD -qSO- --max-redirect=0 ''' + commandcalc + ''' 2>&1 | sed -n 's/^ *Date: *//p')"''')
        command = (customadress)
        successfulchecker = subprocess.run((command), shell=True)
        print(successfulchecker)
        GUI2.destroy()
        syncfin(successfulchecker)
    #Initalisation second window
    print("Show custom sync window...")
    GUI2 = gui.Tk()
    GUI2.title("Custom sync")
    GUI2.resizable(width=False, height=False)
    #Button and space
    print("Set buttons of custom sync window...")
    gui.Label(GUI2).pack(expand=True, fill="x")

    #create lastcustom.cfg if not exist and read from it
    configexist = os.path.isfile(config_path + "/lastcustom.cfg")
    if not configexist == True:
        with open(config_path + "/lastcustom.cfg", "w") as lastcustom:
            print("Enter webadress", file=lastcustom)
            print("", file=lastcustom)
    presetinput = open(config_path + "/lastcustom.cfg", "r")
    presetinput = presetinput.readline()
    presetinput = presetinput.replace("\n", "")
    if language == "2" and presetinput == "Enter webadress": #language for preset entry in inputfield
        presetinput = "Webadresse eingeben"
    
    inputfield = gui.Entry(GUI2) #cannot be used with .pack(expand=True, fill="x")
    inputfield.pack(expand=True, fill="x")
    inputfield.insert(0, presetinput) #insert lastcustom.cfg (or default entry) into inputfield

    gui.Label(GUI2).pack(expand=True, fill="x")
    syncbutton = gui.Button(GUI2, text="Sync", command=syncstart)
    syncbutton.pack()
    if language == "2": #language for button
        syncbutton.config(text="Syncronisieren")
    gui.Label(GUI2).pack(expand=True, fill="x")
    print("Buttons and spaces created.")
print("Syncronization commands loaded.")

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
button7 = ttk.Button(GUI, text="About", command=aboutprogram)
button7.pack(side="left")
print("Set Exit button...") #must be set before button7
button8 = ttk.Button(GUI, text="Exit", command=exitprogram)
button8.pack(side="right")
print("Set Change language button...")
button6 = ttk.Button(GUI, text="Change language", command=changelang)
button6.pack(side="top")

#Space between subbuttons and end
print("Set space between subbuttons and end...")
spaceholder4 = gui.Label(GUI)
spaceholder4.pack(expand=True, fill="x")

print("Main window successfully loaded.")

#Different language text (sub windows have they own lanuguageconfig)
if language != "1":
    print("Change the display to different language:", language)

if language == "2":
    GUI.title("Datum/Uhrzeit Syncronisierer")

    headline.config(text="Datum & Uhrzeit Syncronisierer")

    button1.config(text="Mit Debian.org syncronisieren")
    button2.config(text="Mit Linux (Kernel.org) syncronisieren")
    button3.config(text="Mit DuckDuckGo.com syncronisieren")
    button4.config(text="Mit Google.com syncronisieren")
    button5.config(text="Manuell syncronisieren")

    button6.config(text="Sprache ändern")
    button7.config(text="Über")
    button8.config(text="Beenden")

if language != "1":
    print("Language loaded.")

GUI.mainloop()
print("Exit program...")
