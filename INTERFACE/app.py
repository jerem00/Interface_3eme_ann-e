import json
from flask import Flask, render_template, request, jsonify, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask API Test</title>
</head>
<body>
    <h1>Data Received:</h1>
    <p>{{ data }}</p>
</body>
</html>
"""

def load_data_from_json():
    with open('static/data.json', 'r') as file:
        data = json.load(file)
        patients = []
        for patient_index, patient_data in enumerate(data['patients'], start=1):
            patients.append({
                'patient': f'Patient {patient_index}',
                'temperature': f"{patient_data['temperature']}°C",
                'spo2': f"{patient_data['spo2']}%",
                'heart_rate': f"{patient_data['heart_rate']} bpm"
            })
        return patients
    
@app.route('/')
def index():
    patients = load_data_from_json()
    return render_template('test.html', patients=patients)

if __name__ == '__main__':
    app.run(debug=True)