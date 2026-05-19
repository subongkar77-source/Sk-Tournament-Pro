import os
import urllib.parse
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='.')

# ⚠️ YAHAN APNI ASLI UPI ID DAALO (Jahan aapko paisa chahiye)
YOUR_UPI_ID = "shubhankar@oksbi"  # Isko apni real UPI ID se badal lena
YOUR_NAME = "SK TOURNAMENT"

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 1. Home Page Route
@app.route('/')
def home():
    return render_template('index.html')

# 2. Payment details aur QR Code generate karne ka Route
@app.route('/generate_payment', methods=['POST'])
def generate_payment():
    data = request.json
    player_uid = data.get('uid', 'Unknown')
    amount = "20"  # Match entry fee ₹20
    
    # Ek unique message banate hain jo payment ke waqt dikhega
    txn_note = f"Entry for UID {player_uid}"
    
    # Standard Indian UPI URL Format
    upi_url = f"upi://pay?pa={YOUR_UPI_ID}&pn={urllib.parse.quote(YOUR_NAME)}&am={amount}&cu=INR&tn={urllib.parse.quote(txn_note)}"
    
    # Google ke free API se dynamic QR Code ka link banayenge
    qr_code_url = f"https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl={urllib.parse.quote(upi_url)}"
    
    return jsonify({
        "status": "success",
        "upi_url": upi_url,
        "qr_code_url": qr_code_url
    })

# 3. Final Form aur UTR Submit karne ka Route
@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    try:
        match_name = request.form.get('matchName')
        fee = request.form.get('fee')
        player_uid = request.form.get('playerUID')
        whatsapp = request.form.get('whatsapp')
        utr_id = request.form.get('utrId')  # User ka UTR Number

        if not all([match_name, player_uid, whatsapp, utr_id]):
            return jsonify({"status": "error", "message": "Kripya saari details aur UTR Number bharein!"}), 400

        # Render logs me data print hoga (Aap yahan se verify kar sakte ho)
        print("\n=== 🎯 NAYA TOURNAMENT REGISTRATION ===")
        print(f"Match: {match_name}")
        print(f"Player FF UID: {player_uid}")
        print(f"WhatsApp: {whatsapp}")
        print(f"UTR / Transaction ID: {utr_id}")
        print(f"Fee: ₹{fee}")
        print("=========================================\n")

        return jsonify({"status": "success", "message": "Registration Safal Raha! Aapki details verify ki ja rahi hain."})

    except Exception as e:
        return jsonify({"status": "error", "message": f"Server me koi dikkat aayi: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
