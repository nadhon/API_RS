import json
import os
from app.models import Usuario

ARQUIVO_JSON = 'usuarios.json'

usuarios = []

def carregar_usuarios():
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, 'r') as f:
            dados = json.load(f)
            for usuario in dados:
                usuarios.append(Usuario(**usuario))

def salvar_usuarios():
    with open(ARQUIVO_JSON, 'w') as f:
        json.dump([usuario.to_dict() for usuario in usuarios], f)
