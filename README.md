# timesync
Program to sync the time with different (preset) servers and also a custom server function.


## The application
### How to install the application?
1. Download "ts-ressources" and "install-timesync.sh" from the Releases-section.
2. Start the terminal in the Downloads folder.
3. Type ``` chmod +x install-timesync.sh ``` and press enter.
4. Type ``` sudo ./install-timesync.sh ``` and follow the installation instructions.

### How to start the application?
In your applications (e.g. GNOME application list, Start menu, or Mint menu), there should be a new application called "Time and Date Synchronization". You can launch it by clicking on it.
If you need a debugging-enviroment, you can start the application from the terminal by typing:
```
python3 /opt/timesync/timesync.py
```

### How to use the application?
#### Preset server
1. Start the application by clicking on the entry in your menu.
2. Press on the server you'd like to sync your date and time with.
3. Enter your password (or the root password) and press enter.
4. Time and date should now be synced.

#### Custom server
1. Start the application by clicking on the entry in your menu.
2. Press on "Sync with custom".
3. Enter the server or website you'd like to sync with (e.g. opensource.org) and click the "Sync" button. *(Not every website/server allows time synchronization! If it is not possible to sync, the time is automatically set to 0 o'clock.)*
4. Enter your password (or the root password) and press enter.
5. Time and date should now be synced.


## Building
### How to build the installer?
1. Download the timesync repository (see website below) and extract all the files.
2. Install the package "zip" (with ``` sudo apt install zip ```)
3. Run the "build-installer.sh" script.
4. Now you got a new folder, called "installer". Here you can find the install-timesync.sh and the ts-ressources archive.
5. This files have to be in the same folder. Run the "install-timesync.sh" program to install or uninstall the program.

### Compatiblity
* The installer and the build-setup is written for Debian GNU/Linux or Linux distributions based on it.
* You need python3, python3-tk (Tkinter) in version 3.11.2 (or higher) to run the program. Also the packages pkexec, wget and sed. These are downloaded automatically during installation.


## Website
* See https://github.com/PalaceSoftware/timesync for updates and informations
* See https://github.com/PalaceSoftware/timesync/commits/main for changelog
