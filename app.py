 import os
from flask import Flask, render_template

# Render server ke root directory structure ko access karne ka sabse safe tareeka
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Render ke diye gaye PORT par run karein
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
