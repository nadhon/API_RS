                API de Usuários – CRUD com Flask
_________________________________________________________________

Este repositório foi criado com a finalidade de entregar as atividades da residência, desenvolvendo uma API funcional utilizando Python e Flask.
_________________________________________________________________
A aplicação implementa um CRUD completo de usuários, com:

Armazenamento em uma lista Python (usuarios)

Respostas no formato JSON

Interface HTML simples e funcional

Suporte a métodos POST, PUT, DELETE (simulados via formulário)
_____________________________________________________________________________________________________________________________

                🚀 Funcionalidades da API
_____________________________________________________________________________________________________________________________

                    Criar usuários:
_____________________________________________________________________________________________________________________________

        Adiciona um novo usuário com nome e e-mail à lista Python.
_____________________________________________________________________________________________________________________________

                    Listar usuários

                    📋 Ver usuários (link que mostra a lista de usuarios cadastrados em json)
_____________________________________________________________________________________________________________________________

        Retorna todos os usuários cadastrados em formato JSON.
_____________________________________________________________________________________________________________________________

                    Editar usuários
_____________________________________________________________________________________________________________________________

        Permite atualizar o nome e o e-mail de um usuário existente, usando o ID informado.
_____________________________________________________________________________________________________________________________

Excluir usuários
_____________________________________________________________________________________________________________________________

Remove um usuário da lista com base no ID informado.
_____________________________________________________________________________________________________________________________

                    💻 Interface HTML
_____________________________________________________________________________________________________________________________

A interface foi feita com HTML puro, sem uso de JavaScript. Os formulários permitem:
_____________________________________________________________________________________________________________________________

                    Cadastrar novos usuários

                    Lista de usuarios 

                    Editar usuários existentes

                    Excluir usuários da lista
_________________________________________________________________

O método PUT e DELETE são simulados através do uso de um campo oculto _method e tratados no backend com @app.before_request.
_________________________________________________________________

                        🔙 Retorno em JSON
_________________________________________________________________

Todas as ações (criar, editar, excluir) retornam respostas no formato JSON, contendo:

_________________________________________________________________

Mensagens de sucesso ou erro

Dados do usuário afetado

📂 Estrutura do Projeto

📂app
    📂 routes
    📂 templates/ index.html
init.py          código principal para 
app.py           iniciar a api
controller.py    ordem de parametros para a utilização da api
data.py          aqui ficam armazenados os usuarios
routes.py        as rotas onde a mágica é feita e as rotas se comunicam.
run.py           roda as aplicações com percistencia
