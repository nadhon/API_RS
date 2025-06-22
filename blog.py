from flask import (Blueprint, flask, g, redirect, render_template, request, url_for, jsonify)
from werkzeug.exceptions import abort
from flaskr.auth import login_required 
from flaskr.db import get_db 

db =  Blueprint('blog',__name__)

@db.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)

@db.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        if not title:
            error = 'Title is required.'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
    return redirect(url_for('blog.index'))
def get_post(id, check_outhor=True):
    post = get_db().execute('SELECT p.id, title, body, created, author_id, username'
                            'FROM post p JOIN user u ON p.outhor_id'
                            'WHERE P.id = ?',
                            (id,)).fetchone()
    if post is None:
        abort(404, f"Post id {id} doesn't exist.")
    if check_outhor and post['author_id'] != g.user['id']:
        abort(403)
    
    return post

@db.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title =?, body = ?'
                'WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))
    return render_template('blog/update.html', post=post)

@db.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
@db.route('/exportar-json')
@login_required
def exportar_json():
    bd_conn = get_db()
    posts = bd_conn.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    data_to_save = {
        "mensagem": "Exportação manual de dados",
        "exportado_em": datetime.now().isoformat(),
        "posts": [
            {
                "id": post['id'],
                "title": post['title'],
                "body": post['body'],
                "created": post['created'].isoformat(),
                "author_id": post['author_id'],
                "username": post['username']
            } for post in posts 
            
        ]
    }
    json_path = os.path.join(os.path.dirname(__file__), 'exported_data.json')
    with open(json_path, 'w', encoding= 'utf -8') as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)
    flash('Exportação para JSON realizada com sucesso!')
    return redirect(url_for('blog.index'))