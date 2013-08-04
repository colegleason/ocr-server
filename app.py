from flask import Flask, request
from readbot import ReadBot
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
        result = rb.interpret(filename)
    finally:
        os.remove(filename)
    print result
    return result

if __name__ == "__main__":
    app.debug = True
    app.run()
