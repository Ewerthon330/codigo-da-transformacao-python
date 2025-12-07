# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simples função de soma para o endpoint
def somar(a, b):
    try:
        a = float(a)
        b = float(b)
        return a + b
    except ValueError:
        # Lidar com entradas não numéricas
        raise ValueError("Ambos os inputs devem ser números.")

@app.route('/calculadora/somar', methods=['POST'])
def rota_somar():
    dados = request.get_json()
    
    # Validação de dados de entrada
    if 'a' not in dados or 'b' not in dados:
        return jsonify({"erro": "Requisição inválida. É necessário fornecer 'a' e 'b'."}), 400

    try:
        resultado = somar(dados['a'], dados['b'])
        return jsonify({"resultado": resultado}), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400 # Retorna erro 400 (Bad Request)