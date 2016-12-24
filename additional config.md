
Install requirements for Pillow:
sudo apt-get install python-dev python-setuptools
sudo apt-get install libtiff5-dev libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk

Set:
framebuffer_depth=24
in /boot/config.txt to increase bits per pixel.

To stop the screen from going black due to inactivity, run:
sudo apt-get install xscreensaver
and disable screen saver


sudo apt-get install supervisor

sudo cp photoframe.conf /etc/supervisor/conf.d/photoframe.conf

sudo supervisorctl update
sudo supervisorctl restart photoframe

Install rclone to sync the images directory:
http://rclone.org/install/

rclone mount google_drive: fantastic-photo-frame/static/images/ --allow-non-empty
or
rclone sync google_drive: fantastic-photo-frame/static/images/

After installing teamviewer, add:
ExecStartPre = sleep 60
in 
/etc/systemd/system/teamviewerd.service
section Service
