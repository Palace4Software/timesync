#!/bin/bash

### Automatic setup creator for timesync ###

version=$(cat version.txt)

chmod +x install-timesync.sh

mkdir timesync
cp timesync.py timesync/timesync
cp languagesetup.py timesync/
cp LICENSE timesync/
cp README.md timesync/
cp version.txt timesync/
cp install-timesync.sh timesync/install-timesync-$version.sh

zip -r ts-ressources.zip timesync/
zip ts-ressources.zip timesync.desktop
zip ts-ressources.zip icon.png

mkdir installer
mv ts-ressources.zip ts-ressources-$version && cp install-timesync.sh install-timesync-$version.sh

tar -cvzf timesync-manualsetup-$version.tar.gz ts-ressources-$version install-timesync-$version.sh && mv timesync-manualsetup-$version.tar.gz installer/ && rm install-timesync-$version.sh ts-ressources-$version
