from app.models import Usuario
from app.data import usuarios, salvar_usuarios

def adicionar_usuario(nome, email):
    existe = next((u for u in usuarios if u.email == email), None)
    if existe:
        raise Exception("Usuario com este email já existe")
    usuario_id = len(usuarios) + 1
    novo_usuario = Usuario(usuario_id, nome, email)
    usuarios.append(novo_usuario)
    salvar_usuarios()
    return novo_usuario

def listar_usuarios():
    return [usuario.to_dict() for usuario in usuarios]
    
def atualizar_usuario(id, nome, email):
    usuario = next((u for u in usuarios if u.id == id), None)
    if usuario:
        usuario.nome = nome
        usuario.email = email
        salvar_usuarios()
        return usuario
    else:
        raise Exception("Usuario não encontrado")

def excluir_usuario(id):
    usuario = next((u for u in usuarios if u.id == id), None)
    if usuario:
        usuarios.remove(usuario)
        salvar_usuarios()
        return usuario
    else:
        raise Exception("Usuario não encontrado")