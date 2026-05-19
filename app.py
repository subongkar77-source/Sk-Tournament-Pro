import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# स्क्रीनशॉट फ़ाइलें सुरक्षित रखने के लिए फोल्डर सेट करें
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# अगर प्रोजेक्ट में 'static/uploads' फोल्डर नहीं है, तो यह उसे अपने आप बना देगा
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# होम पेज का रूट (जो आपकी index.html फ़ाइल को लोड करेगा)
@app.route('/')
def home():
    return render_template('index.html')

# पेमेंट और रजिस्ट्रेशन डेटा रिसीव करने का रूट
@app.route('/submit_payment', methods=['POST'])
def submit_payment():
    try:
        match_name = request.form.get('matchName')
        fee = request.form.get('fee')
        player_uid = request.form.get('playerUID')
        whatsapp = request.form.get('whatsapp')
        txn_id = request.form.get('txnId')
        screenshot = request.files.get('screenshot')
        
        if not all([match_name, player_uid, whatsapp, txn_id, screenshot]):
            return jsonify({"status": "error", "message": "कृपया सभी विवरण भरें और स्क्रीनशॉट अपलोड करें!"}), 400
            
        clean_filename = secure_filename(screenshot.filename)
        unique_filename = f"{player_uid}_{txn_id}_{clean_filename}"
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        screenshot.save(file_path)
        
        print("\n=== नया टूर्नामेंट रजिस्ट्रेशन प्राप्त हुआ ===")
        print(f"मैच: {match_name} | प्लेयर FF UID: {player_uid} | UTR: {txn_id}")
        print("============================================\n")
        
        return jsonify({"status": "success", "message": "रजिस्ट्रेशन सफल रहा!"})
        
    except Exception as e:
        return jsonify({"status": "error", "message": "सर्वर में कोई तकनीकी खराबी आई है।"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
