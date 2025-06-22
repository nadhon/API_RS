from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def create_app():
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
from app import routes 