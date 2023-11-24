#!/bin/bash

### Automatic .deb creator for timesync ###

version=$(cat version.txt)

# move files to deb building folder
mkdir -p deb/usr/lib/timesync/
cp timesync.py deb/usr/lib/timesync/timesync
cp languagesetup.py deb/usr/lib/timesync/
cp version.txt deb/usr/lib/timesync/
cp LICENSE deb/usr/lib/timesync/
cp README.md deb/usr/lib/timesync/

mkdir -p deb/usr/share/icons/hicolor/256x256/apps/
cp icon.png deb/usr/share/icons/hicolor/256x256/apps/timesync.png

mkdir -p deb/usr/share/applications/
cp timesync.desktop deb/usr/share/applications/

mkdir -p deb/usr/bin/
echo "#!/bin/bash
exec /usr/lib/timesync/timesync" > deb/usr/bin/timesync

# chmod
chmod +x deb/usr/lib/timesync/timesync
chmod +x deb/usr/bin/timesync
chmod 755 deb/DEBIAN

# build
dpkg-deb --build -Zxz deb
mkdir installer
mv deb.deb installer/timesync-$version.deb

#clearup
rm -r deb/usr
