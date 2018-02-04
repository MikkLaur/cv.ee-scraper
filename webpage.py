from flask import Flask, render_template
import pickle
import time

from persistence import load, Columns
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', adverts=load(), c=Columns)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5550, debug=False)