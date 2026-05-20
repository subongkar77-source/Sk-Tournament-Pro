import os
from flask import Flask, render_template

# Current file path se template folder ka path nikalna
basedir = os.path.abspath(os.path.dirname(__file__))
template_folder = os.path.join(basedir, 'templates')

app = Flask(__name__, template_folder=template_folder)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
