#!/bin/bash

### Automatic setup creator for timesync ###

version=$(cat version.txt)

chmod +x install-timesync.sh

mkdir timesync
cp application/timesync.py timesync/timesync
cp application/languagesetup.py timesync/
cp LICENSE timesync/
cp README.md timesync/
cp version.txt timesync/
cp install-timesync.sh timesync/install-timesync-$version.sh

zip -r ts-ressources.zip timesync/
zip ts-ressources.zip timesync.desktop
zip ts-ressources.zip icon.png

mkdir installer
mv ts-ressources.zip installer/ts-ressources-$version && cp install-timesync.sh installer/install-timesync-$version.sh
