from flask import Flask
from flask import render_template
import random
from uploadS3 import get_file_url

app = Flask(__name__)

@app.route('/')
def random_image():
    image = random.choice(get_file_url())
    print("IMAGE", image)

    return render_template("index.html", image=image)


if __name__ == "__main__":  
    app.run(debug=True)