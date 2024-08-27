from flask import Flask, request, jsonify
import numpy as np
from funções.funcoes_adicionais import *
from funções.funcoes_criadas import *

app = Flask(__name__)

#criando as matrizes de permutação para usar nas funções
P = permutacao_identidade()
E = permutacao_identidade()

#criando as rotas para cada função
@app.route('/para_one_hot', methods=['POST'])
def api_para_one_hot():
    data = request.json
    string_mensagem = data['string_mensagem']
    resultado = para_one_hot(string_mensagem)
    return jsonify(resultado.tolist())

@app.route('/para_string', methods=['POST'])
def para_string_endpoint():
    data = request.json
    matriz_codificada_one_hot = np.array(data['matriz'])
    string_resultante = para_string(matriz_codificada_one_hot)
    return jsonify({"string": string_resultante})

@app.route('/cifrar', methods=['POST'])
def api_cifrar():
    data = request.json
    string_mensagem = data['string_mensagem']
    resultado = cifrar(string_mensagem, P)
    return jsonify({'mensagem_codificada': resultado})

@app.route('/de_cifrar', methods=['POST'])
def api_de_cifrar():
    data = request.json
    mensagem_codificada = data['mensagem_codificada']
    resultado = de_cifrar(mensagem_codificada, P)
    return jsonify({'mensagem_decodificada': resultado})

@app.route('/enigma', methods=['POST'])
def api_enigma():
    data = request.json
    string_mensagem = data['string_mensagem']
    resultado = enigma(string_mensagem, P, E)
    return jsonify({'mensagem_codificada': resultado})

@app.route('/de_enigma', methods=['POST'])
def api_de_enigma():
    data = request.json
    mensagem_codificada = data['mensagem_codificada']
    resultado = de_enigma(mensagem_codificada, P, E)
    return jsonify({'mensagem_decodificada': resultado})

if __name__ == '__main__':
    app.run(debug=True)
