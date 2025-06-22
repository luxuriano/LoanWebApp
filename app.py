from flask import Flask, request, jsonify, render_template
from LoanAPP import obtener_respuesta

app = Flask(__name__, template_folder=".")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/preguntar', methods=['POST'])
def preguntar():
    datos = request.json
    pregunta = datos.get("mensaje", "")
    if not pregunta:
        return jsonify({"error": "Mensaje vacío"}), 400

    respuesta = obtener_respuesta(pregunta)
    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run(debug=True)
