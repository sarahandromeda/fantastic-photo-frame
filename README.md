# Fantastic Photo Frame

Software for displaying photos on a screen,
making it look good and easy to update.

The application will display photos that are placed in
a specific directory, selecting one at random and showing 
it for a while. 

To avoid having black strips of screen on the sides, (since
the images can be in any ratio), the pictures are bordered
with a photo-frame style 'card' mount, that will readjust its
window to fit any photo.

## Setup
The following is more or less how I set it up on a Raspberry Pi.

Get repo and enter directory
```
git clone https://github.com/samuelfekete/fantastic-photo-frame
cd fantastic-photo-frame
```


### Install requirements for Pillow:
```
sudo apt-get install python-dev python-setuptools
sudo apt-get install libtiff5-dev libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
```

### Install requirements photo frame.
```
pip install -r requirements.txt
```

### Make it startup and restart on exit.
```
sudo apt-get install supervisor
sudo cp photoframe.conf /etc/supervisor/conf.d/photoframe.conf
sudo supervisorctl update
sudo supervisorctl restart photoframe
```

### Sync with a google drive.
Install rclone following the instructions here:
http://rclone.org/install/

Create images directory. Photoframe will check this directory for pictures.
```
sudo mkdir -p /opt/photoframe/images
sudo chown pi:pi /opt/photoframe/images
```

To mount it virtually, (photos get fetched from the internet and not stored locally):
```
rclone mount google_drive: fantastic-photo-frame/static/images/ --allow-non-empty
```

To sync a local directory (photos are stored locally)
```
rclone sync google_drive: fantastic-photo-frame/static/images/
```
and add a cronjob to sync every hour or so.
```
13 * * * * /usr/sbin/rclone sync google_drive: /opt/photoframe/images/
```

You can combine the two options by having two sub-directories in `/opt/photoframe/images/`, one
that is mounted and one that is synced. This way there will always be photos, even when the internet
connction is lost, and when there is an internet connection an unlimited number of images can be served from 
the cloud.

### Additional Raspberry Pi config
Set:
`framebuffer_depth=24`
in `/boot/config.txt` to increase bits per pixel.

To stop the screen from going black due to inactivity, run:
`sudo apt-get install xscreensaver`
and disable screen saver
