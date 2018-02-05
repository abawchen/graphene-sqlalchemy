from app import create_app, db, DB_URL

app = create_app()

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

    from .models import Department

    hr = Department(name='HR')
    db.session.add(hr)

    engineering = Department(name='Engineering')
    db.session.add(engineering)

    db.session.commit()

