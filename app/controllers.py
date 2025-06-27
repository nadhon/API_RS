from app.models import Usuario
from app.data import usuarios

def adicionar_usuario(nome, email):
    usuario_id = len(usuarios) + 1
    novo_usuario = Usuario(usuario_id, nome, email)
    usuarios.append(novo_usuario)
    return novo_usuario

def listar_usuarios():
    return [usuario.to_dict() for usuario in usuarios]
    
def atualizar_usuario(id, nome, email):
    usuario = next((u for u in usuarios if u.id == id), None)
    if usuario:
        usuario.nome = nome
        usuario.email = email
        usuario.save()

def excluir_usuario(id):
    usuario = next((u for u in usuarios if u.id == id), None)
    if usuario:
        usuarios.remove(usuario)