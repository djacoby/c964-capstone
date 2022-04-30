import os

from sqlalchemy import create_engine
from decouple import config

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'DATABASE_URL').replace("postgres://", "postgresql://", 1)

engine = create_engine(SQLALCHEMY_DATABASE_URI)


def execute_query(query):
    db = engine.connect()
    result = db.execute(*query)
    db.close()

    return [dict(row) for row in result]
