from flask import Flask, request
from readbot import ReadBot
from PIL import Image, ImageOps
import tempfile
import os

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    image = request.data
    rb = ReadBot()
    (fd, filename) = tempfile.mkstemp()
    try:
        tfile = os.fdopen(fd, "w")
        tfile.write(image)
        tfile.close()
        img = Image.open(filename)
        w, h = img.size
        img = img.resize((w*2, h*2))
        img = ImageOps.grayscale(img)
        img.save(filename, "PNG")
        result = rb.interpret(filename)
    finally:
        os.remove(filename)
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
