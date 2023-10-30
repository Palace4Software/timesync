#!/bin/bash
### Setup for timesync program ###

# release-version (important!)
ver="2.0.0"

if [[ $EUID -ne 0 ]]; then
   echo "The installation/uninstallation must be run as root. Aborting..." 
   exit 1
fi

installerdir=$(dirname "$0")

echo "Checking if timesync is already installed..."
if [ -e "/opt/timesync/isinstalled.check" ]; then
   echo "timesync is already installed."
   answer="n"
   read -p "Do you want to uninstall it? (y/N): " answer
   if [[ $answer == "y" ]]; then
      echo "Uninstallation..."
      rm -r /opt/timesync
      rm /usr/share/applications/timesync.desktop
      rm /usr/bin/timesync
      echo "Uninstallation finished."
      echo "It's recommended, that you remove the configuration of timesync. (Can be found under ~/.config/timesync)"
      exit 0
   else
      echo "Uninstallation aborted."
      exit 0
   fi
fi

echo "Timesync is not installed. Checking resources archive..."
if [ -e "$installerdir/ts-ressources-$ver" ]; then
   echo "Archive found."
else
   echo "The ressources archive cannot be found. Please be sure, that the file is called 'ts-ressources-$ver' and that you don't deleted it."
   exit 2
fi
echo "Dependencies will be downloaded..."
apt install python3 python3-tk pkexec unzip wget sed -y
echo "Dependencies downloaded."
echo
echo "Prepairing ressources archive..."
unzip -o $installerdir/ts-ressources-$ver
echo "Install timesync to /opt/timesync/ ..."
mv timesync /opt/
mv timesync.desktop /usr/share/applications/
echo "#!/bin/bash
exec /opt/timesync/timesync" > /usr/bin/timesync
chmod +x /opt/timesync/timesync
chmod +x /opt/timesync/install-timesync-$ver.sh
chmod +x /usr/bin/timesync
echo "
DO NOT DELETE THIS FILE!

This file is important to let the (un)installer know, that 'timesync' is installed." > /opt/timesync/isinstalled.check
echo "Installation finished. To uninstall, you must run the installer (can also be found in /opt/timesync/) again."
echo "You may need to restart the session to apply all changes."
exit 0
