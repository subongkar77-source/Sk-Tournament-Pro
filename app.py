import os
from flask import Flask, render_template, request, jsonify

# Flask ko batana ki templates folder kahan hai
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Render ke liye port set karna
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
