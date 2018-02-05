#!/usr/bin/env python

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
#from schema import schema

DB_URL = 'postgres://{user}:{password}@{host}/{database}'.format(
    user='postgres',
    password='mysecretpassword',
    host='127.0.0.1:5432',
    database='postgres'
)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.debug = True


    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    #db = SQLAlchemy(app)


    #app.add_url_rule(
    #    '/graphql',
    #    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    #)

    return app

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

if __name__ == '__main__':
    app = create_app()
    app.run()

