from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres@localhost:5432/capstone')

connection = engine.connect()


def get_db():
    return connection


def disconnect_db():
    connection.close()
