from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres@localhost:5432/capstone')

connnection = engine.connect()


def get_db():
    return connnection


def disconnect_db():
    connnection.close()
