#!/bin/bash

### Automatic setup creator for timesync ###

version=$(cat version.txt)

chmod +x install-timesync.sh

mkdir timesync
mv timesync.py timesync/
mv LICENSE timesync/
mv README.md timesync/
mv icon.png timesync/
mv version.txt timesync/
cp install-timesync.sh timesync/

zip -r ts-ressources.zip timesync/
zip ts-ressources.zip timesync.desktop
mv ts-ressources.zip ts-ressources

mkdir installer
mv ts-ressources installer/ts-ressources-$version && mv install-timesync.sh installer/
