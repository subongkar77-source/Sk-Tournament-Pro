 import os
from flask import Flask, render_template

# Render mein working directory ko force karna
template_dir = os.path.join(os.getcwd(), 'templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Render PORT variable deta hai
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
