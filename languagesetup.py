#!/usr/bin/env python3
### Setup language for timesync ###

def main():
    print("Initalize 'Change lanuguage' subwindow...")
    import tkinter as gui
    from tkinter import ttk
    from tkinter import messagebox
    import os
    import platformdirs

    def seteng():
        with open(config_path + "/language.cfg", "w") as langcfg:
            print("EN", file=langcfg)
            print("", file=langcfg)
        print("Language set to English.")
        GUI.destroy()
        if firststart == True:
            messagebox.showwarning("Language changed", "The language is now set to English.")
        else:
            messagebox.showwarning("Language changed", "You may have to restart the application to apply the changes.")
        
    def setger():
        with open(config_path + "/language.cfg", "w") as langcfg:
            print("DE", file=langcfg)
            print("", file=langcfg)
        print("Language set to German.")
        GUI.destroy()
        if firststart == True:
            messagebox.showwarning("Sprache geändert", "Sie müssen die Anwendung schließen und neu öffnen, damit die Sprache übernommen werden kann.")
        else:
            messagebox.showwarning("Sprache geändert", "Möglicherweise müssen Sie die Anwendung neu starten, um die Änderungen zu übernehmen.")
    
    config_path = platformdirs.user_config_dir("timesync")
    checkfirststart = os.path.isfile(config_path + "/firststart.cfg")
    if checkfirststart == True:
        firststart = False # no firststart (because file exist)
        with open(config_path + "/firststart.cfg", "w") as frststrt:
            print("False", file=frststrt)
            print("# DO NOT CHANGE OR DELETE THIS FILE", file=frststrt)
            print("", file=frststrt)
    else:
        firststart = True # firststart (because file do not exist)
        with open(config_path + "/firststart.cfg", "w") as frststrt:
            print("True", file=frststrt)
            print("# DO NOT CHANGE OR DELETE THIS FILE", file=frststrt)
            print("", file=frststrt)
    
    GUI = gui.Tk()
    GUI.title("Choose language")
    GUI.geometry("187x100")
    GUI.resizable(height="false", width="false")
    
    spaceholder1 = gui.Label(GUI).pack(expand=True, fill="x")
    
    englishbutton = ttk.Button(GUI, text="English", command=seteng)
    englishbutton.pack()
    germanbutton = ttk.Button(GUI, text="Deutsch", command=setger)
    germanbutton.pack()
    
    spaceholder2 = gui.Label(GUI).pack(expand=True, fill="x")
    
    print("Initialisation of subwindow finished.")
    GUI.mainloop()

# main() # uncomment this line for debugging
