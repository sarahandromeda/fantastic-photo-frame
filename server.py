import random
from os import walk

from flask import Flask

app = Flask(__name__)

@app.route('/next_image')
def next_image():
    file_list = []
    for _, _, filenames in walk('static/images'):
        file_list.extend(filenames)
        break
    image_list = [f for f in file_list if f.endswith(('.jpg', '.png'))]
    return '{}/{}'.format('images', random.choice(image_list))


if __name__ == "__main__":
    app.run()
