from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres@localhost:5432/capstone')


def execute_query(query):
    db = engine.connect()
    result = db.execute(*query)
    db.close()
    return [dict(row) for row in result]
