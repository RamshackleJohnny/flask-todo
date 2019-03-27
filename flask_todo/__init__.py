import os

from flask import Flask, request, make_response, render_template

from flask_todo.db import get_db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask_todo.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from . import db
    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/new', methods=('GET', 'POST'))
    def ne():
        if request.method == 'POST':
            db = get_db()
            item = request.form['item']
            done = 'FALSE'
            error = None
            if error is None:
                db.execute(
                    'INSERT INTO list (item, done)'
                    ' VALUES (?, FALSE)',
                    (item)
                )
                db.commit()
            return render_template('index.html')
        return render_template('new.html')


    @app.route('/delete')
    def dal():
        return render_template('delete.html')





    return app
