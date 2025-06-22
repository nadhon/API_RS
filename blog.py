from curses import flash
from turtle import get_poly
from urllib import request
from flask import (Blueprint, flask, g, redirect, render_template, resquest, url_for)
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