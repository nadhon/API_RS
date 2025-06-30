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
    try:
        dados = request.get_json(silent=True)
        if dados:
            nome = dados.get('nome')
            email = dados.get('email')
        else:
            nome = request.form.get('nome')
            email = request.form.get('email')

        if not nome or not email:
            return jsonify({"error": "Nome e email obrigatórios"}), 400

        novo_usuario = adicionar_usuario(nome, email)
        return jsonify({"message": "Usuario adicionado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400



@app.route('/usuarios/excluir', methods=['DELETE', 'POST'])
def excluir():
    try:
        id = int(request.form['id'])
        usuario = excluir_usuario(id)
        if not usuario:
            return jsonify({"error": "Usuario não encontrado"}), 404
        return jsonify({"message": "Usuario excluído com sucesso!", "usuario": usuario.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": "Erro ao excluir usuario"}), 404

@app.route('/usuarios/editar', methods=['PUT', 'POST'])
def editar():
    try:
        id = int(request.form['id'])
        nome = request.form['nome']
        email = request.form['email']
        if not nome or not email:
            return jsonify({"error": "Nome e email obrigatórios"}), 400
        editar_usuario = atualizar_usuario(id, nome, email)
        return jsonify({"message": "Usuario editado com sucesso!", "usuario": editar_usuario.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": "Erro ao editar usuário"}), 404
    
@app.before_request
def tratamento():
    if request.method == 'POST' and '_method' in request.form:
        metodo =  request.form['_method'].upper()
        if metodo in ['PUT', 'DELETE']:
            request.environ['REQUEST_METHOD'] = metodo
