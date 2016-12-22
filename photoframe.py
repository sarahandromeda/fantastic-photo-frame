from __future__ import division

import random
from os import walk

from Tkinter import *
import sys
from PIL import Image, ImageTk

root = Tk()
root.attributes('-fullscreen', True)
root.config(cursor='none')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
frame_width = screen_width - 100
frame_height = screen_height - 100

# Tile the background image
bg_pattern = Image.open("static/paper.png")
pattern_width, pattern_height = bg_pattern.size
background_image = Image.new('RGB', (screen_width, screen_height))
for i in xrange(0, screen_width, pattern_width):
    for j in xrange(0, screen_height, pattern_height):
        background_image.paste(bg_pattern, (i, j))


# Set background
background_photo = ImageTk.PhotoImage(background_image)
background = Label(
    root,
    image=background_photo,
)
background.place(x=0, y=0)

def get_next_image():
    file_list = []
    for _, _, filenames in walk('static/images'):
        file_list.extend(filenames)
        break
    image_list = [f for f in file_list if f.endswith(('.jpg', '.png', '.JPG'))]
    return 'static/images/{}'.format(random.choice(image_list))

def set_image():
    image = Image.open(get_next_image())
    image_width, image_height = image.size
    if image_height / image_width > frame_height / frame_width:
        scale_factor = frame_height / image_height 
    else:
        scale_factor = frame_width / image_width 

    image = image.resize(
        (int(scale_factor * image_width),
         int(scale_factor * image_height)),
         Image.ANTIALIAS,
    )
    photo = ImageTk.PhotoImage(image)
    picture.config(image=photo)
    picture.image = photo

    root.after(10000, set_image)

picture = Label(
    root,
    relief=SUNKEN,
    borderwidth=4,
)
picture.place(x=screen_width // 2, y=screen_height // 2, anchor=CENTER)

set_image()

root.mainloop()
