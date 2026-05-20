import os
from flask import Flask, render_template

# Path ko force kar rahe hain taaki templates folder mil jaye
template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Render PORT variable deta hai, agar na mile toh 5000 use karein
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
