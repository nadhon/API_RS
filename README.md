Manda ver, Maguiaro! Aqui vai um modelo de `README.md` direto ao ponto, bem documentado e ideal pra qualquer dev front-end (ou back-end) que for usar tua API REST de usuários:

---

````markdown
# 🧠 API de Gerenciamento de Usuários

Esta é uma API REST simples feita com Flask, que simula um banco de dados utilizando um arquivo JSON (`usuarios.json`) como persistência de dados.

Ideal para projetos de estudo, integração com front-end (HTML, JS, React, etc) ou testes em ferramentas como Postman/Insomnia.

---

## 🚀 Como rodar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/nadhon/API_RS.git
````

2. Instale as dependências (caso não tenha o Flask):

```bash
pip install flask
```

3. Rode o projeto:

```bash
python run.py
```

---

## 📁 Estrutura do Projeto

```
📂 app/
│
├── __init__.py           # Cria e configura a aplicação Flask
├── app.py                # Entrada da API (pode ser mesclado com run.py)
├── controller.py         # Funções de controle (CRUD)
├── data.py               # Simula banco de dados com arquivo JSON
├── models.py             # Classe Usuario
├── routes/
│   └── routes.py         # Rotas da API (GET, POST, PUT, DELETE)
├── templates/
│   └── index.html        # Interface HTML (opcional)
│
├── usuarios.json         # Arquivo com dados persistentes
└── run.py                # Inicializa a aplicação
```

---

## 📬 Rotas da API

### 🔹 `GET /usuarios`

Retorna a lista de todos os usuários.

**Resposta:**

```json
{
  "usuarios": [
    { "id": 1, "nome": "João", "email": "joao@email.com" }
  ]
}
```

---

### 🔹 `POST /usuarios`

Adiciona um novo usuário.

**Corpo esperado (JSON ou formulário):**

```json
{
  "nome": "Joana",
  "email": "joana@email.com"
}
```

**Resposta:**

```json
{
  "usuario": { "id": 2, "nome": "Joana", "email": "joana@email.com" }
}
```

---

### 🔹 `PUT /usuarios/<id>`

Atualiza um usuário existente.

**Corpo:**

```json
{
  "nome": "Joana Silva",
  "email": "joana.silva@email.com"
}
```

**Resposta:**

```json
{ "message": "Usuário atualizado" }
```

---

### 🔹 `DELETE /usuarios/<id>`

Remove um usuário existente.

**Resposta:**

```json
{ "message": "Usuário excluído com sucesso!" }
```

---

## 💡 Compatibilidade com Formulários HTML

Formulários que simulam `PUT` ou `DELETE` via:

```html
<input type="hidden" name="_method" value="DELETE">
```

São suportados graças a este código no `app.py`:

```python
@app.before_request
def tratamento():
    if request.method == 'POST' and '_method' in request.form:
        metodo =  request.form['_method'].upper()
        if metodo in ['PUT', 'DELETE']:
            request.environ['REQUEST_METHOD'] = metodo
```

E há uma rota auxiliar:

```python
@app.route('/usuarios/excluir', methods=['DELETE', 'POST'])
```
---
caso queira remover a rota @app.before_request só trocar os 
post do código das rotas para sua funcionalidade e acrescentar 
o metodo: 
fetch('/usuarios/<id>', {
  method: 'DELETE'
})
.then(res => res.json())
.then(data => console.log(data));

---

## 🗃️ Persistência de Dados

* Todos os usuários são armazenados no arquivo `usuarios.json`
* A API carrega esses dados automaticamente ao iniciar
* Alterações (add, update, delete) são salvas imediatamente

---

## 👨‍💻 Desenvolvido por

Nadhon josé