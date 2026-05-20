import os
from flask import Flask, render_template

# यह कोड आपकी वर्तमान डायरेक्टरी के आधार पर 'templates' फोल्डर ढूंढ लेगा
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
