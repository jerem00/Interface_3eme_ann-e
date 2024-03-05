from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Modèle HTML à utiliser pour la rendu de la page (à adapter selon vos besoins)
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

@app.route('/submit', methods=['GET', 'POST'])  # Autoriser à la fois les méthodes GET et POST
def handle_data():
    #if request.method == 'POST':  # Vérifier la méthode de la requête
        if request.is_json:
            data = request.get_json()  # Get data from POST request
            print(data)
            # Render an HTML page with the received data
            jsonify({"Data received"})
            return render_template_string(TEMPLATE, data=data), 200
        else:
            return jsonify({"error": "Request must be JSON"}), 400
    #elif request.method == 'GET':  # Si la méthode est GET, renvoyer la page HTML
    #    return render_template_string(TEMPLATE, data=""), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)