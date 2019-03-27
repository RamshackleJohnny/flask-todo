import os
import psycopg2
from flask import Flask, request, make_response, render_template

import flask_todo.db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


    @app.route('/')
    def index():
        connection = psycopg2.connect(database = "flask_todo")
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM list''')
        list = cursor.fetchall()
        connection.close()
        return render_template('index.html', list=list)

    @app.route('/new', methods=('GET', 'POST'))
    def ne():
        if request.method == 'POST':
            item = request.form['item']
            connection = psycopg2.connect(database = "flask_todo")
            cursor = connection.cursor()
            send_it = f''' INSERT INTO list (item,done) VALUES ('{item}',FALSE);'''
            cursor.execute(send_it)
            connection.commit()
            print("WE SENT IT")
            cursor.close()
            connection.close()
            print("Now that we sent it, its closed")

            return render_template('index.html')
        return render_template('new.html')


    @app.route('/delete')
    def dal():
        return render_template('delete.html')

    return app
