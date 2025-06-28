from flask import  request, jsonify, render_template
from app import app
from app.data import usuarios
from app.controllers import adicionar_usuario, listar_usuarios, atualizar_usuario, excluir_usuario



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/say', methods=['GET'])
def say():
    return jsonify({"message": """Bem-vindo a API de exemplo!
    🚀 Explore todo potencial"""})

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:    
        return jsonify({"usuarios": [usuario.to_dict() for usuario in usuarios]}), 200
    except Exception as e:
        return jsonify({"error": "Erro ao listar usuários"}), 500
    

@app.route('/usuarios', methods=['POST'])
def adicionar():
    dados = request.get_json(silent=True)
    if dados:
        nome = dados.get('nome')
        email = dados.get('email')
    else:
        nome = request.form.get('nome')
        email = request.form.get('email')

    if not nome or not email:
        return jsonify({"error": "Nome e email são obrigatórios"}), 400

    novo_usuario = adicionar_usuario(nome, email)
    return jsonify(novo_usuario.to_dict()), 201

    # return render_template('adicionar_usuario.html') #reserve a rota para adicionar usuário via GET

@app.route('/usuarios/<int:id>/excluir', methods=['DELETE'])
def excluir(id):
    sucesso = excluir_usuario(id)
    if sucesso:
        return jsonify({"message": "Usuário excluído com sucesso!"}), 200
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404

@app.route('/usuarios/<int:id>/editar', methods=['PUT'])
def editar(id):
    try:
        dados = request.get_json(silent=True)

        if not dados:
            return jsonify({"error": "Dados inválidos"}), 400
        
        nome = dados.get('nome')
        email = dados.get('email')
        if not nome or not email:
            return jsonify({"error": "Nome e email são obrigatórios"}), 400
        
        editar_usuario = atualizar_usuario(id, nome, email)
        
        return jsonify(editar_usuario.to_dict()), 200
    except Exception as e:
        return jsonify({"error": "Erro ao editar usuário"}), 404
