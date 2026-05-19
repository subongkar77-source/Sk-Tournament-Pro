import os
import urllib.parse
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ⚠️ Yahan apni UPI ID aur Name check kar lena
YOUR_UPI_ID = "shubhankar@oksbi"  
YOUR_NAME = "SK TOURNAMENT"

# 1. Home Page Loading Route
@app.route('/')
def home():
    return render_template('index.html')

# 2. QR Code aur Intent Link generate karne ka Route
@app.route('/generate_payment', methods=['POST'])
def generate_payment():
    try:
        data = request.json
        player_uid = data.get('uid', 'Unknown')
        amount = "20"  # Entry Fee ₹20
        
        txn_note = f"Entry for UID {player_uid}"
        
        # Indian Standard UPI Deep Link Format
        upi_url = f"upi://pay?pa={YOUR_UPI_ID}&pn={urllib.parse.quote(YOUR_NAME)}&am={amount}&cu=INR&tn={urllib.parse.quote(txn_note)}"
        
        # Google API se automatic QR image link generate karna
        qr_code_url = f"https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl={urllib.parse.quote(upi_url)}"
        
        return jsonify({
            "status": "success",
            "upi_url": upi_url,
            "qr_code_url": qr_code_url
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 3. Final Form aur UTR Data receive karne ka Route
@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    try:
        match_name = request.form.get('matchName')
        fee = request.form.get('fee')
        player_uid = request.form.get('playerUID')
        whatsapp = request.form.get('whatsapp')
        utr_id = request.form.get('utrId')

        if not all([match_name, player_uid, whatsapp, utr_id]):
            return jsonify({"status": "error", "message": "Kripya saari details aur UTR Number bharein!"}), 400

        # Render dashboard logs me display hone wala registration data
        print("\n=== 🎯 NEW REGISTRATION RECEIVED ===")
        print(f"Match Name : {match_name}")
        print(f"Player UID : {player_uid}")
        print(f"WhatsApp   : {whatsapp}")
        print(f"UTR / Txn  : {utr_id}")
        print(f"Fee Paid   : ₹{fee}")
        print("=====================================\n")

        return jsonify({"status": "success", "message": "Registration Safal Raha! Admin verification ke baad aapka slot approve ho jayega."})

    except Exception as e:
        return jsonify({"status": "error", "message": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
