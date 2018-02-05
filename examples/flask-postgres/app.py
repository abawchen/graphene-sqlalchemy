#!/usr/bin/env python

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
#from schema import schema

app = Flask(__name__)
app.debug = True

DB_URL = 'postgres://{user}:{password}@{host}/{database}'.format(
    user='postgres',
    password='mysecretpassword',
    host='127.0.0.1:5432',
    database='postgres'
)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

default_query = '''
{
  allEmployees {
    edges {
      node {
        id,
        name,
        department {
          id,
          name
        },
        role {
          id,
          name
        }
      }
    }
  }
}'''.strip()


#app.add_url_rule(
#    '/graphql',
#    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
#)


@app.cli.command('resetdb')
def resetdb_command():
    """Destroys and creates the database + tables."""

    from sqlalchemy_utils import database_exists, create_database, drop_database
    if database_exists(DB_URL):
        print('Deleting database.')
        drop_database(DB_URL)
    if not database_exists(DB_URL):
        print('Creating database.')
        create_database(DB_URL)

    print('Creating tables.')
    from . import models
    db.create_all()
    print('Shiny!')

@app.cli.command('seeddb')
def seeddb_command():
    """Seed data."""

    from .import models
    pass

if __name__ == '__main__':
    app.run()

