import os
from flask import Flask, render_template

# Ye lines Flask ko batayengi ki templates kahan hain, chahe server kahin bhi ho
template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
