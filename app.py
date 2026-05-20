import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # यह लाइन आपके रेंडर लॉग्स में दिखाएगी कि सर्वर असल में क्या देख रहा है
    files = os.listdir('.')
    templates_files = os.listdir('templates') if os.path.exists('templates') else "Templates folder not found"
    print(f"Current Directory Files: {files}")
    print(f"Templates Folder Contents: {templates_files}")
    
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
