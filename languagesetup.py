#!/usr/bin/env python3
### Setup language for timesync ###

def main():
    import tkinter as gui
    from tkinter import ttk
    import os
    import platformdirs

    def seteng():
        config_path = platformdirs.user_config_dir("timesync")
        with open(config_path + "/language.cfg", "w") as langcfg:
            print("EN", file=langcfg)
            print("", file=langcfg)
        GUI.destroy()
        
    def setger():
        config_path = platformdirs.user_config_dir("timesync")
        with open(config_path + "/language.cfg", "w") as langcfg:
            print("DE", file=langcfg)
            print("", file=langcfg)
        GUI.destroy()
        
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

    GUI.mainloop()

# main() # uncomment this line for debugging
