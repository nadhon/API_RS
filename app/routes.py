from flask import  request, jsonify, render_template
from app import app
from app.controllers import adicionar_usuario, listar_usuarios, atualizar_usuario, excluir_usuario



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/say', methods=['GET'])
def say():
    return jsonify({"message": "Bem-vindo a API de exemplo!"})

@app.route('/usuarios', methods=['GET'])
def usuarios():
    try:
        usuarios = listar_usuarios()
        if not usuarios:
            return jsonify({"error": "Nenhum usuário encontrado!"}), 404
        return jsonify(usuarios)
    except Exception as e:
        return jsonify({"error": str("Erro ao listar usuários")}), 500
    

@app.route('/usuarios/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data or 'nome' not in data or 'email' not in data:
                return jsonify({"error": "Dados inválidos!"}), 400
            nome = data['nome']
            email = data['email']
            adicionar_usuario(nome, email)
            if not nome or not email:
                return jsonify({"error": "Nome e email são obrigatórios!"}), 400                                                               
            return jsonify({"mensage": "Usuário adicionado com sucesso!"})
        except Exception as e:
            return jsonify({"error": str("Usuário não adicionado!")}), 404
    # return render_template('adicionar_usuario.html') #reserve a rota para adicionar usuário via GET

@app.route('/usuarios/<int:id>/excluir', methods=['POST'])
def excluir(id):
    excluir_usuario(id)
    try:
        return jsonify({"message": "Usuário excluído com sucesso!"})
    except Exception as e:
        return jsonify({"error": str("Usuário não encontrado")}), 404

@app.route('/usuarios/<int:id>/editar', methods=['GET', 'POST'])
def editar(id):
    try:
        usuario = listar_usuarios(id)
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            atualizar_usuario(id, nome, email)
            return jsonify({"message": "Usuário atualizado com sucesso!"})
        return jsonify(usuario)
    except Exception as e:
        return jsonify({"error": str("Usuário não encontrado")}), 404

