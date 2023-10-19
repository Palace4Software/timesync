#!/bin/bash

### Automatic setup creator for timesync ###

chmod+x install-timesync.sh

mkdir timesync
mv timesync.py timesync/
mv LICENSE timesync/
mv icon.png timesync/
cp install-timesync.sh timesync/

zip -r ts-ressources.zip timesync/
zip ts-ressources.zip timesync.desktop
mv ts-ressources.zip ts-ressources

mkdir installer
mv ts-ressources installer/ && mv install-timesync.sh installer/
