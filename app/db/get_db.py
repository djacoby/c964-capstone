from sqlalchemy import create_engine
from decouple import config

DB_URL = config('DB_URL')
engine = create_engine(DB_URL)


def execute_query(query):
    db = engine.connect()
    result = db.execute(*query)
    db.close()
    return [dict(row) for row in result]
