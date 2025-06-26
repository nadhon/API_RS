from flask import redirect, request, jsonify, url_for
from app import app
from app.controllers import adicionar_usuario, listar_usuarios, atualizar_usuario, excluir_usuario
from flask import render_template

@app.route('/usuarios')
def usuarios():
    usuarios = listar_usuarios()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/usuarios/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        adicionar_usuario(nome, email)
        return redirect(url_for('usuarios'))
    return render_template('adicionar_usuario.html')

@app.route('/usuarios/<int:id>/editar', methods=['GET', 'POST'])
def editar(id):
    usuario = listar_usuarios(id)
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        atualizar_usuario(id, nome, email)
        return redirect(url_for('usuarios'))
    return render_template('editar_usuario.html', usuario=usuario)

@app.route('/usuarios/<int:id>/excluir', methods=['POST'])
def excluir(id):
    excluir_usuario(id)
    return redirect(url_for('usuarios'))