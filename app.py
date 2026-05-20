import os
from flask import Flask, render_template, request, jsonify

# Render ke liye pathing ko fix karna zaroori hai
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)

# --- CONFIGURATION ---
YOUR_UPI_ID = "shubhankar@oksbi"
YOUR_NAME = "SK TOURNAMENT"

# --- ROUTES ---
@app.route('/')
def home():
    # Ab Flask seedha 'templates/index.html' dhundhega
    return render_template('index.html')

@app.route('/generate_payment', methods=['POST'])
def generate_payment():
    try:
        data = request.json
        player_uid = data.get('uid', 'Unknown')
        amount = "20"
        txn_note = f"Entry for UID {player_uid}"
        
        import urllib.parse
        upi_url = f"upi://pay?pa={YOUR_UPI_ID}&pn={urllib.parse.quote(YOUR_NAME)}&tn={urllib.parse.quote(txn_note)}&am={amount}&cu=INR"
        qr_code_url = f"https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl={urllib.parse.quote(upi_url)}"
        
        return jsonify({"status": "success", "upi_url": upi_url, "qr_code_url": qr_code_url})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    try:
        match_name = request.form.get('matchName')
        player_uid = request.form.get('playerUID')
        whatsapp = request.form.get('whatsapp')
        utr_id = request.form.get('utrID')
        
        print(f"NEW REGISTRATION: {match_name}, UID: {player_uid}")
        return jsonify({"status": "success", "message": "Registration Successful!"})
    except Exception as e:
        return jsonify({"status": "error", "message": "Server error"}), 500

if __name__ == '__main__':
    # Render ke liye dynamic port
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
