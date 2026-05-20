import os
from flask import Flask, render_template, request, jsonify

# Naya path setup yahan hai
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_payment', methods=['POST'])
def generate_payment():
    try:
        data = request.json
        player_uid = data.get('uid', 'Unknown')
        upi_url = f"upi://pay?pa=shubhankar@eksbi&pn=SK%20TOURNAMENT&tn=Entry%20for%20UID%20{player_uid}&am=20&cu=INR"
        qr_code_url = f"https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl={upi_url}"
        return jsonify({"status": "success", "upi_url": upi_url, "qr_code_url": qr_code_url})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    return jsonify({"status": "success", "message": "Registration Successful!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
