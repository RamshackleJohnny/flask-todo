import psycopg2
from psycopg2 import Error
import click
from flask.cli import with_appcontext

def init_db():
    try:
        connection = psycopg2.connect(database = "flask_todo")
        cursor = connection.cursor()
        create_table_query = '''CREATE TABLE list
            (created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            item           TEXT    NOT NULL,
            done         BOOLEAN NOT NULL); '''
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created")
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Can't do", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("Connection is closed")

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
