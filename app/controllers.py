from app.models import Usuario

def adicionar_usuario(nome, email):
    usuario_id = len(listar_usuarios()) + 1
    usuario = Usuario(id=usuario_id, nome=nome, email=email)
    listar_usuarios().append(usuario)
    return usuario

def listar_usuarios():
    return Usuario.query.all()

def atualizar_usuario(id, nome, email):
    usuario = Usuario.query.get(id)
    if usuario:
        usuario.nome = nome
        usuario.email = email
        usuario.save()

def excluir_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        usuario.delete()