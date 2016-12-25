from __future__ import division

import functools
import os
import random

from Tkinter import *
import sys
from PIL import Image, ImageTk

root = Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
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


def image_transpose_exif(im):
    """Rotate images taken incorrectly.

    Taken from: http://stackoverflow.com/a/30462851
    """
    exif_orientation_tag = 0x0112 # contains an integer, 1 through 8
    exif_transpose_sequences = [  # corresponding to the following
        [],
        [Image.FLIP_LEFT_RIGHT],
        [Image.ROTATE_180],
        [Image.FLIP_TOP_BOTTOM],
        [Image.FLIP_LEFT_RIGHT, Image.ROTATE_90],
        [Image.ROTATE_270],
        [Image.FLIP_TOP_BOTTOM, Image.ROTATE_90],
        [Image.ROTATE_90],
    ]

    try:
        seq = exif_transpose_sequences[im._getexif()[exif_orientation_tag] - 1]
    except Exception:
        return im
    else:
        return functools.reduce(lambda im, op: im.transpose(op), seq, im)


def get_next_image(source='static/images'):
    file_list = []
    for dirpath, _, filenames in os.walk(source):
        file_list.extend([
            os.path.join(dirpath, filename) for filename in filenames
            if filename.endswith(('.jpg', '.png', '.JPG'))
        ])
    if not file_list:
        if not source == 'static/images':
            return get_next_image('static/images')
        else:
            raise RuntimeError('Could not find any images')
    return random.choice(file_list)

def set_image(event=None):
    image = Image.open(get_next_image('/opt/photoframe/images'))
    image = image_transpose_exif(image)
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
