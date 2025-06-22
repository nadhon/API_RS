from flask import Flask, render_template 
from App.routes import blog

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blog.bp)

    return app