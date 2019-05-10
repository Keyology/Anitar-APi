from flask import Flask
app = Flask(__name__)

@app.route('/api/v0/random/anime/poster')
def random_image():
    return "<img src=image_download/image0.jpg />"


