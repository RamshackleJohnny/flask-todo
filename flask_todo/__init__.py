import os

from flask import Flask, request, make_response, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
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
            item = request.form['item']
            error = None
            db = get_db()
            db.execute(
                'INSERT INTO list (item, done)'
                ' VALUES (?, FALSE)',
                (item, done)
            )
            db.commit()
            return redirect('index.html')
        return render_template('new.html')


    @app.route('/delete')
    def dal():
        return render_template('delete.html')





    return app
