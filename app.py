import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Debugging print
    print(f"Current Working Directory: {os.getcwd()}")
    print(f"Files in folder: {os.listdir('.')}")
    if os.path.exists('templates'):
        print(f"Files in templates: {os.listdir('templates')}")
    else:
        print("Templates folder not found!")
    
    return render_template('index.html')
